from dataloaders import (
    load_goodreads_data,
    load_letterboxd_data,
    load_anilist_data,
    load_mydramalist_data,
)

# User Profiles Configuration
PROFILES = {
    "goodreads_user_id": "74584614",
    "letterboxd_username": "PenyulTekowel",
    "anilist_username": "laataiasu",
    "mydramalist_username": "Chanculus",
}


def format_goodreads_body(row):
    """Dynamically formats Goodreads body omitting any empty or missing fields."""
    title = row.get("Title", "")
    lines = [f"# {title}\n"]

    date_added = str(row.get("Date Added", "")).split()[0] if row.get("Date Added") else ""
    date_read = str(row.get("Date Read", "")).split()[0] if row.get("Date Read") else ""

    fields = [
        ("Author", row.get("Author")),
        ("My Rating", row.get("My Rating")),
        ("Average Rating", row.get("Average Rating")),
        ("Pages", row.get("Number of Pages")),
        ("Year Published", row.get("Year Published")),
        ("Date Added", date_added),
        ("Date Read", date_read),
        ("Bookshelves", row.get("Bookshelves")),
        ("ISBN", row.get("ISBN")),
        ("ISBN13", row.get("ISBN13")),
    ]

    meta_lines = []
    for label, val in fields:
        if val is not None and str(val).strip() and str(val).strip() not in ["", "None", "nan", "0000-00-00"]:
            meta_lines.append(f"- **{label}:** {str(val).strip()}")

    if meta_lines:
        lines.append("\n".join(meta_lines))

    review = row.get("My Review")
    if review and str(review).strip() and str(review).strip() not in ["", "None", "nan"]:
        lines.append(f"\n\n## Review\n\n{str(review).strip()}")

    return "\n".join(lines)


def format_mydramalist_body(row):
    """Dynamically formats MyDramaList body omitting any empty fields."""
    title = row.get("Title", "")
    lines = [f"# {title}\n"]

    fields = [
        ("Country", row.get("Country")),
        ("Year", row.get("Year")),
        ("Type", row.get("Type")),
        ("Score", row.get("Score")),
        ("Progress", row.get("Progress")),
    ]

    meta_lines = []
    for label, val in fields:
        if val is not None and str(val).strip() and str(val).strip() not in ["", "None", "nan"]:
            meta_lines.append(f"- **{label}:** {str(val).strip()}")

    if meta_lines:
        lines.append("\n".join(meta_lines))

    return "\n".join(lines)


DATA_SOURCES = {
    "goodreads": {
        "description": "Goodreads (Books)",
        "loader": lambda: load_goodreads_data(user_id=PROFILES["goodreads_user_id"]),
        "output_dir": "_tmp_goodreads",
        "blog_sync_path": "Read/Goodreads",
        "title_column": "Title",
        "date_column": "Date Added",
        "tags": ["book"],
        "publish_external": False,
        "frontmatter_mapping": {
            "title": "Title",
            "author": "Author",
            "date": "Date Added",
        },
        "content_formatter": format_goodreads_body,
    },
    "letterboxd": {
        "description": "Letterboxd (Films)",
        "loader": lambda: load_letterboxd_data(username=PROFILES["letterboxd_username"]),
        "output_dir": "_tmp_letterboxd",
        "blog_sync_path": "Watch/Letterboxd",
        "title_column": "Name",
        "date_column": "Date",
        "default_date": "2020-01-01",
        "tags": ["film"],
        "publish_external": False,
        "frontmatter_mapping": {
            "title": "Name",
            "date": "Date",
            "year": "Year",
            "letterboxd_uri": "Letterboxd URI",
            "rating": "Rating",
        },
    },
    "anilist_anime": {
        "description": "AniList (Anime)",
        "loader": lambda: load_anilist_data(username=PROFILES["anilist_username"], media_type="ANIME"),
        "output_dir": "_tmp_anime",
        "blog_sync_path": "Watch/Anime",
        "title_column": "series_title",
        "default_date": "2016-01-01",
        "tags": ["anime", "film"],
        "publish_external": False,
        "frontmatter_mapping": "all",
    },
    "anilist_manga": {
        "description": "AniList (Manga)",
        "loader": lambda: load_anilist_data(username=PROFILES["anilist_username"], media_type="MANGA"),
        "output_dir": "_tmp_manga",
        "blog_sync_path": "Read/Manga",
        "title_column": "manga_title",
        "default_date": "2016-01-01",
        "tags": ["manga", "book"],
        "publish_external": False,
        "frontmatter_mapping": "all",
    },
    "mydramalist": {
        "description": "MyDramaList (Asian & Korean Drama)",
        "loader": lambda: load_mydramalist_data(username=PROFILES["mydramalist_username"]),
        "output_dir": "_tmp_drama",
        "blog_sync_path": "Watch/Drama",
        "title_column": "Title",
        "default_date": "2016-01-01",
        "tags": ["film", "drama"],
        "publish_external": False,
        "frontmatter_mapping": {
            "title": "Title",
            "country": "Country",
            "year": "Year",
            "type": "Type",
            "score": "Score",
            "progress": "Progress",
        },
        "content_formatter": format_mydramalist_body,
    },
}
