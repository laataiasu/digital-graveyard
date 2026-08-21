"""
Normalizes source DataFrames into ierp media records and pushes them to the
ierp SQLite database via its CLI (`uv run ierp ingest-media`).
"""

import json
import os
import shutil
import subprocess
import tempfile
import pandas as pd

IERP_ROOT = os.environ.get("IERP_ROOT", os.path.expanduser("~/Projects/ierp"))

# media_type per get-data source key
SOURCE_MEDIA_TYPE = {
    "hardcover": "book",
    "goodreads": "book",
    "letterboxd": "film",
    "anilist_anime": "anime",
    "anilist_manga": "manga",
    "mydramalist": "drama",
}

SOURCE_NAME = {
    "hardcover": "hardcover",
    "goodreads": "goodreads",
    "letterboxd": "letterboxd",
    "anilist_anime": "anilist",
    "anilist_manga": "anilist",
    "mydramalist": "mydramalist",
}


def _clean(v):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None
    if pd.isna(v):
        return None
    if isinstance(v, float) and v.is_integer():
        return int(v)
    return v


def _date_str(v):
    v = _clean(v)
    if v is None:
        return None
    dt = pd.to_datetime(v, errors="coerce")
    if pd.isna(dt):
        return None
    return dt.strftime("%Y-%m-%d")


def normalize_records(source_key: str, df: pd.DataFrame) -> list:
    """Converts a source DataFrame into ierp ingest-media record dicts."""
    media_type = SOURCE_MEDIA_TYPE.get(source_key, source_key)
    src = SOURCE_NAME.get(source_key, source_key)
    records = []

    for _, row in df.iterrows():
        r = {k: _clean(v) for k, v in row.items()}
        title = r.get("Title") or r.get("Name") or r.get("series_title") or r.get("manga_title")
        if not title or not str(title).strip():
            continue
        title = str(title).strip()

        external_id = r.get("Id") or r.get("Book Id") or r.get("letterboxd_uri") or \
                      r.get("series_id") or r.get("manga_id") or r.get("URL") or \
                      r.get("Letterboxd URI") or r.get("url")
        url = r.get("URL") or r.get("Letterboxd URI") or r.get("url") or \
              (external_id if isinstance(external_id, str) and external_id.startswith("http") else None)

        rec = {
            "media_type": media_type,
            "title": title,
            "original_title": r.get("series_native_title") or r.get("native_title") or r.get("Original Title"),
            "year": r.get("Year") or r.get("year") or r.get("release_year") or r.get("series_season_year") or r.get("Year Published") or r.get("year_published"),
            "author": r.get("Author") or r.get("author"),
            "source": src,
            "extra": {k: v for k, v in r.items() if v is not None and k not in (
                "Title", "Name", "series_title", "manga_title")},
            "status": r.get("Reading Status") or r.get("status") or r.get("Progress"),
            "rating": r.get("My Rating") or r.get("Rating") or r.get("rating") or r.get("Score") or r.get("score"),
            "progress": r.get("Progress") or r.get("progress"),
            "started_at": _date_str(r.get("Date Started") or r.get("started_at") or r.get("Start Date")),
            "finished_at": _date_str(r.get("Date Read") or r.get("finished_at") or r.get("Finish Date")),
            "date_logged": _date_str(r.get("Date Added") or r.get("Date") or r.get("date") or
                                     r.get("updated_at") or r.get("created_at")),
            "review": (str(r.get("My Review")).strip() or None) if r.get("My Review") else None,
            "raw": {k: (str(v) if v is not None else None) for k, v in r.items()},
        }
        records.append(rec)
    return records


def push_to_ierp(source_key: str, records: list) -> bool:
    """Writes records to a temp JSON file and pipes through `uv run ierp ingest-media`."""
    if not records:
        return True
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(records, f, ensure_ascii=False, default=str)
        tmp = f.name
    try:
        result = subprocess.run(
            ["uv", "run", "ierp", "ingest-media", tmp],
            cwd=IERP_ROOT, capture_output=True, text=True, timeout=300,
        )
        if result.returncode != 0:
            print(f"[ierp] Ingest failed for {source_key}: {result.stderr.strip()[:500]}")
            return False
        print(f"[ierp] {result.stdout.strip()} ({source_key}: {len(records)} records)")
        return True
    except Exception as e:
        print(f"[ierp] Ingest error for {source_key}: {e}")
        return False
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
