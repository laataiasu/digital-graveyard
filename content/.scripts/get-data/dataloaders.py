import os
import re
import json
import time
import urllib.parse
import xml.etree.ElementTree as ET
import pandas as pd
import requests
from bs4 import BeautifulSoup
from helpers import clean_isbn, sanitize_text, load_environment

# Ensure environment variables from ~/.secrets or .env are available
load_environment()

# Default Browser Headers
BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def retry_request(fetch_fn, max_retries=3, delay=2):
    """Executes a network function with retry logic."""
    for attempt in range(1, max_retries + 1):
        try:
            return fetch_fn()
        except Exception as e:
            if attempt == max_retries:
                raise e
            time.sleep(delay * attempt)


def load_hardcover_data(username="nichsedge", api_key=None):
    """
    Loads user books, ratings, and authors from Hardcover.app official GraphQL API.
    API token is free for all users at https://hardcover.app/account/api
    """
    token = api_key or os.environ.get("HARDCOVER_API_KEY")
    if not token:
        raise ValueError("HARDCOVER_API_KEY not found in environment or ~/.secrets. Set it in ~/.secrets or export HARDCOVER_API_KEY.")

    print(f"Fetching Hardcover books for user: {username}...")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}" if not token.startswith("Bearer ") else token,
        "User-Agent": "DigitalGraveyard/1.0",
    }

    # Clean GraphQL query matching Hardcover Hasura schema
    query = f"""
    query GetUserBooks {{
      user_books(where: {{user: {{username: {{_eq: "{username}"}}}}}}) {{
        id
        rating
        status_id
        created_at
        updated_at
        user_book_reads {{
          started_at
          finished_at
        }}
        edition {{
          title
          pages
          release_date
          isbn_10
          isbn_13
          publisher {{
            name
          }}
          book {{
            title
            description
            release_year
            rating
            contributions {{
              author {{
                name
              }}
            }}
          }}
        }}
      }}
    }}
    """

    payload = {"query": query}
    
    def do_post():
        return requests.post("https://api.hardcover.app/v1/graphql", json=payload, headers=headers, timeout=20)

    try:
        resp = retry_request(do_post)
        if resp.status_code != 200:
            raise ConnectionError(f"Hardcover API returned status {resp.status_code}")
        data = resp.json()
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Hardcover API: {e}") from e

    if "errors" in data:
        err_msg = ", ".join(e.get("message", "Unknown error") for e in data["errors"])
        raise ValueError(f"Hardcover GraphQL error: {err_msg}")

    user_books = data.get("data", {}).get("user_books", [])
    if not user_books:
        raise ValueError(f"No books retrieved from Hardcover for user: {username}")

    records = []
    for item in user_books:
        edition = item.get("edition") or {}
        book = edition.get("book") or {}
        title = edition.get("title") or book.get("title") or ""
        
        # Authors
        contributions = book.get("contributions") or []
        authors = [c.get("author", {}).get("name") for c in contributions if c.get("author", {}).get("name")]
        author_str = ", ".join(authors) if authors else ""

        # Status mapping: 1 = Want to Read, 2 = Currently Reading, 3 = Read
        status_map = {1: "to-read", 2: "currently-reading", 3: "read"}
        status_str = status_map.get(item.get("status_id"), "")

        # Dates
        created_at = item.get("created_at", "")
        date_added = created_at.split("T")[0] if created_at else ""

        reads = item.get("user_book_reads") or []
        date_read = ""
        if reads and isinstance(reads, list):
            last_read = reads[-1]
            finished = last_read.get("finished_at")
            if finished:
                date_read = finished.split("T")[0]

        pub_year = str(book.get("release_year") or edition.get("release_date") or "")[:4]

        records.append({
            "Title": title,
            "Author": author_str,
            "My Rating": item.get("rating"),
            "Average Rating": book.get("rating"),
            "Pages": edition.get("pages"),
            "Year Published": pub_year,
            "Date Added": date_added,
            "Date Read": date_read,
            "Bookshelves": status_str,
            "ISBN": clean_isbn(edition.get("isbn_10")),
            "ISBN13": clean_isbn(edition.get("isbn_13")),
        })

    print(f"Fetched {len(records)} books from Hardcover.")
    return pd.DataFrame(records)


def load_goodreads_data(user_id="74584614", shelf="#ALL#", file_path=None):
    """
    Loads Goodreads data directly from RSS feed with retries and fallback to local file.
    """
    if file_path and os.path.exists(file_path):
        print(f"Loading Goodreads data from local file: {file_path}")
        df = pd.read_csv(file_path, dtype=str)
        df.columns = [col.strip() for col in df.columns]
        df["ISBN"] = df["ISBN"].apply(clean_isbn)
        df["ISBN13"] = df["ISBN13"].apply(clean_isbn)
        df["Date Added"] = pd.to_datetime(df["Date Added"], errors="coerce")
        df["Date Added"] = df["Date Added"].fillna(pd.Timestamp.min)
        for col in df.columns:
            if col != "Date Added":
                df[col] = df[col].apply(sanitize_text)
        return df

    print(f"Fetching Goodreads data via RSS for user ID: {user_id}...")
    books = []
    page = 1
    encoded_shelf = urllib.parse.quote(shelf)

    while True:
        url = f"https://www.goodreads.com/review/list_rss/{user_id}?shelf={encoded_shelf}&page={page}"
        
        def do_get():
            return requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)

        try:
            resp = retry_request(do_get)
            if resp.status_code == 404:
                raise ValueError(f"Goodreads user ID '{user_id}' not found (HTTP 404). Check profile privacy/ID.")
            if resp.status_code != 200:
                raise ConnectionError(f"Goodreads RSS returned HTTP status {resp.status_code}")

            tree = ET.fromstring(resp.content)
            channel = tree.find("channel")
            items = channel.findall("item") if channel is not None else []
            if not items:
                break

            for item in items:
                def get_text(tag):
                    el = item.find(tag)
                    return el.text.strip() if el is not None and el.text else ""

                date_added_raw = get_text("user_date_added")
                date_read_raw = get_text("user_read_at")
                
                date_added = ""
                if date_added_raw:
                    try:
                        date_added = pd.to_datetime(date_added_raw).strftime("%Y-%m-%d")
                    except Exception:
                        date_added = date_added_raw

                date_read = ""
                if date_read_raw:
                    try:
                        date_read = pd.to_datetime(date_read_raw).strftime("%Y-%m-%d")
                    except Exception:
                        date_read = date_read_raw

                title = get_text("title")
                author = get_text("author_name")
                isbn = clean_isbn(get_text("isbn"))
                isbn13 = clean_isbn(get_text("isbn13"))
                rating = get_text("user_rating")
                avg_rating = get_text("average_rating")
                shelves = get_text("user_shelves")
                review = get_text("user_review")
                year_pub = get_text("book_published")
                num_pages = get_text(".//num_pages")

                books.append({
                    "Title": title,
                    "Author": author,
                    "Date Added": date_added,
                    "Date Read": date_read,
                    "My Rating": rating if rating and rating != "0" else "",
                    "Average Rating": avg_rating,
                    "Bookshelves": shelves,
                    "ISBN": isbn,
                    "ISBN13": isbn13,
                    "Number of Pages": num_pages,
                    "Year Published": year_pub,
                    "My Review": review,
                })

            if len(items) < 100:
                break
            page += 1
        except Exception as e:
            if page == 1:
                raise ConnectionError(f"Failed to fetch Goodreads books: {e}") from e
            print(f"Goodreads pagination notice on page {page}: {e}")
            break

    if not books:
        raise ValueError(f"No books retrieved from Goodreads for user ID: {user_id}. Profile might be private.")

    print(f"Fetched {len(books)} books from Goodreads.")
    df = pd.DataFrame(books)
    if not df.empty:
        df["Date Added"] = pd.to_datetime(df["Date Added"], errors="coerce")
        df["Date Added"] = df["Date Added"].fillna(pd.Timestamp.min)
    return df


def load_letterboxd_data(username="PenyulTekowel", file_path=None):
    """
    Loads Letterboxd data by scraping user rated films or from local ratings.csv file.
    """
    if file_path and os.path.exists(file_path):
        print(f"Loading Letterboxd data from local file: {file_path}")
        return pd.read_csv(file_path, parse_dates=["Date"])

    print(f"Fetching Letterboxd ratings for user: {username}...")
    try:
        from curl_cffi import requests as c_requests
        session = c_requests.Session(impersonate="chrome120")
    except ImportError:
        session = requests.Session()
        session.headers.update(BROWSER_HEADERS)

    films = []
    page = 1
    while True:
        url = f"https://letterboxd.com/{username}/films/ratings/page/{page}/"
        
        def do_get():
            return session.get(url, timeout=15)

        try:
            resp = retry_request(do_get)
            if resp.status_code == 404:
                raise ValueError(f"Letterboxd profile '{username}' not found (HTTP 404).")
            if resp.status_code != 200:
                raise ConnectionError(f"Letterboxd returned HTTP status {resp.status_code}")

            soup = BeautifulSoup(resp.text, "html.parser")
            griditems = soup.find_all("li", class_="griditem")
            if not griditems:
                break

            for li in griditems:
                react_el = li.find(attrs={"data-item-name": True}) or li.find("div", class_="film-poster")
                if not react_el:
                    continue

                full_display_name = react_el.get("data-item-full-display-name", "")
                item_name = react_el.get("data-item-name", "")
                item_link = react_el.get("data-item-link", "")
                
                year = None
                year_match = re.search(r"\((\d{4})\)", full_display_name)
                if year_match:
                    year = int(year_match.group(1))
                    name = re.sub(r"\s*\(\d{4}\)", "", full_display_name).strip()
                else:
                    name = item_name or full_display_name

                rating = None
                rating_el = li.find("span", class_=re.compile(r"rated-"))
                if rating_el:
                    for c in rating_el.get("class", []):
                        if c.startswith("rated-"):
                            try:
                                rating = int(c.split("-")[1]) / 2.0
                            except ValueError:
                                pass

                letterboxd_uri = f"https://letterboxd.com{item_link}" if item_link else ""

                films.append({
                    "Name": name,
                    "Year": year,
                    "Letterboxd URI": letterboxd_uri,
                    "Rating": rating,
                    "Date": None,
                })

            pagination = soup.find("div", class_="pagination")
            if not pagination:
                break
            pages = pagination.find_all("li", class_="paginate-page")
            if pages:
                try:
                    last_page = int(pages[-1].text.strip())
                    if page >= last_page:
                        break
                except ValueError:
                    pass

            page += 1
            time.sleep(0.3)
        except Exception as e:
            if page == 1:
                raise ConnectionError(f"Failed to fetch Letterboxd ratings: {e}") from e
            print(f"Letterboxd pagination note on page {page}: {e}")
            break

    if not films:
        raise ValueError(f"No rated films found for Letterboxd user: {username}.")

    print(f"Fetched {len(films)} rated films from Letterboxd.")
    return pd.DataFrame(films)


def load_anilist_data(username="laataiasu", media_type="ANIME"):
    """
    Loads Anime or Manga data directly from AniList official GraphQL API.
    """
    print(f"Fetching AniList {media_type} for user: {username}...")
    query = """
    query ($userName: String, $type: MediaType) {
      MediaListCollection(userName: $userName, type: $type) {
        lists {
          name
          entries {
            id
            status
            score(format: POINT_10_DECIMAL)
            progress
            progressVolumes
            repeat
            priority
            notes
            startedAt { year month day }
            completedAt { year month day }
            updatedAt
            createdAt
            media {
              id
              idMal
              title {
                romaji
                english
                native
              }
              type
              format
              status
              description
              episodes
              chapters
              volumes
              seasonYear
            }
          }
        }
      }
    }
    """
    payload = {
        "query": query,
        "variables": {"userName": username, "type": media_type.upper()},
    }
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    
    def do_post():
        return requests.post("https://graphql.anilist.co", json=payload, headers=headers, timeout=20)

    try:
        resp = retry_request(do_post)
        if resp.status_code != 200:
            raise ConnectionError(f"AniList GraphQL API returned HTTP {resp.status_code}")
        data = resp.json()
    except Exception as e:
        raise ConnectionError(f"Failed to connect to AniList API: {e}") from e

    if "errors" in data:
        err_msg = ", ".join(e.get("message", "Unknown error") for e in data["errors"])
        raise ValueError(f"AniList GraphQL error: {err_msg}")

    lists = data.get("data", {}).get("MediaListCollection", {}).get("lists", [])
    records = []

    for lst in lists:
        for entry in lst.get("entries", []):
            media = entry.get("media", {})
            title_dict = media.get("title", {})
            title = title_dict.get("romaji") or title_dict.get("english") or title_dict.get("native") or ""
            
            completed_at = entry.get("completedAt", {})
            c_year = completed_at.get("year")
            c_month = completed_at.get("month")
            c_day = completed_at.get("day")
            finish_date = f"{c_year:04d}-{c_month:02d}-{c_day:02d}" if (c_year and c_month and c_day) else "0000-00-00"

            started_at = entry.get("startedAt", {})
            s_year = started_at.get("year")
            s_month = started_at.get("month")
            s_day = started_at.get("day")
            start_date = f"{s_year:04d}-{s_month:02d}-{s_day:02d}" if (s_year and s_month and s_day) else "0000-00-00"

            raw_status = entry.get("status", "")
            status_map = {
                "COMPLETED": "Completed",
                "CURRENT": "Watching" if media_type == "ANIME" else "Reading",
                "PLANNING": "Plan to Watch" if media_type == "ANIME" else "Plan to Read",
                "DROPPED": "Dropped",
                "PAUSED": "On-Hold",
                "REPEATING": "Rewatching" if media_type == "ANIME" else "Rereading",
            }
            clean_status = status_map.get(raw_status, raw_status.title())

            record = {
                "series_animedb_id": media.get("idMal") or media.get("id"),
                "series_title": title,
                "series_type": media.get("format") or "",
                "series_episodes": media.get("episodes") if media_type == "ANIME" else media.get("chapters"),
                "my_id": entry.get("id"),
                "my_watched_episodes": entry.get("progress"),
                "my_start_date": start_date,
                "my_finish_date": finish_date,
                "my_score": entry.get("score"),
                "my_status": clean_status,
                "my_times_watched": entry.get("repeat", 0),
                "my_comments": entry.get("notes"),
                "my_priority": "LOW",
                "manga_title": title,
                "title": title,
            }
            records.append(record)

    print(f"Fetched {len(records)} AniList {media_type} entries.")
    return pd.DataFrame(records)


def load_mydramalist_data(username="Chanculus", file_path=None):
    """
    Loads MyDramaList data by scraping public dramalist page or from local CSV file.
    """
    if file_path and os.path.exists(file_path):
        print(f"Loading MyDramaList data from local file: {file_path}")
        df = pd.read_csv(file_path, quoting=1, engine="python")
        df[["Title", "Type"]] = df["Title"].str.split("\n", expand=True)
        return df

    print(f"Fetching MyDramaList for user: {username}...")
    url = f"https://mydramalist.com/dramalist/{username}"
    
    def do_get():
        return requests.get(url, headers=BROWSER_HEADERS, timeout=20)

    try:
        resp = retry_request(do_get)
        if resp.status_code == 404:
            raise ValueError(f"MyDramaList user '{username}' not found (HTTP 404).")
        if resp.status_code != 200:
            raise ConnectionError(f"MyDramaList returned HTTP status {resp.status_code}")

        soup = BeautifulSoup(resp.text, "html.parser")
        tables = soup.find_all("table", class_="mdl-style-table")
        records = []

        for table in tables:
            for tr in table.find_all("tr"):
                tds = tr.find_all("td")
                if len(tds) < 6:
                    continue

                title_a = tds[0].find("a", class_="title")
                title = title_a.text.strip() if title_a else tds[0].text.strip()
                title = re.sub(r"\s*(Korean|Japanese|Chinese|Taiwanese|Thai|Hong Kong)\s*(Movie|Drama|Special)$", "", title, flags=re.IGNORECASE).strip()

                country = tds[1].text.strip() if len(tds) > 1 else ""
                year = tds[2].text.strip() if len(tds) > 2 else ""
                d_type = tds[3].text.strip() if len(tds) > 3 else ""
                score = tds[4].text.strip() if len(tds) > 4 else ""
                progress = tds[5].text.strip() if len(tds) > 5 else ""

                try:
                    score_val = float(score)
                except ValueError:
                    score_val = score

                try:
                    year_val = int(year)
                except ValueError:
                    year_val = year

                records.append({
                    "Title": title,
                    "Country": country,
                    "Year": year_val,
                    "Type": d_type,
                    "Score": score_val,
                    "Progress": progress,
                })

        if not records:
            raise ValueError(f"No dramalist tables found for MyDramaList user '{username}'. List might be empty or private.")

        print(f"Fetched {len(records)} MyDramaList entries.")
        return pd.DataFrame(records)
    except Exception as e:
        raise ConnectionError(f"Failed to fetch MyDramaList: {e}") from e
