"""
Normalizes source DataFrames into ierp media records and pushes them to the
ierp SQLite database via its CLI (`uv run ierp ingest-media`).

Field-mapping tables at the top are the single place to touch when a source
adds or renames columns.
"""

import json
import os
import subprocess
import tempfile
from typing import Optional

import pandas as pd

IERP_ROOT = os.environ.get("IERP_ROOT", os.path.expanduser("~/Projects/ierp"))

# get-data source key -> (ierp media_type, ierp source name)
SOURCE_MAP = {
    "hardcover": ("book", "hardcover"),
    "goodreads": ("book", "goodreads"),
    "letterboxd": ("film", "letterboxd"),
    "anilist_anime": ("anime", "anilist"),
    "anilist_manga": ("manga", "anilist"),
    "mydramalist": ("drama", "mydramalist"),
}

# Candidate column names per record field (first match wins).
FIELD_CANDIDATES = {
    "title": ("Title", "Name", "series_title", "manga_title"),
    "original_title": ("series_native_title", "native_title", "Original Title"),
    "year": ("Year", "year", "release_year", "series_season_year",
             "Year Published", "year_published"),
    "author": ("Author", "author"),
    "status": ("Reading Status", "status", "Progress"),
    "rating": ("My Rating", "Rating", "rating", "Score", "score"),
    "progress": ("Progress", "progress"),
}

# Candidate column names per date field.
DATE_CANDIDATES = {
    "started_at": ("Date Started", "started_at", "Start Date"),
    "finished_at": ("Date Read", "finished_at", "Finish Date"),
    "date_logged": ("Date Added", "Date", "date", "updated_at", "created_at"),
}

# Columns excluded from the `extra` dict (they map to real fields or are redundant).
_EXTRA_EXCLUDED = {"Title", "Name", "series_title", "manga_title"}


def _clean(v):
    """NaN/None -> None; integral floats -> int; everything else passthrough."""
    if v is None:
        return None
    try:
        if pd.isna(v):
            return None
    except (TypeError, ValueError):
        pass
    if isinstance(v, float) and v.is_integer():
        return int(v)
    return v


def _first(r: dict, candidates: tuple):
    """First non-empty value among candidate column names."""
    for col in candidates:
        v = r.get(col)
        if v is not None and str(v).strip() != "":
            return v
    return None


def _date_str(v) -> Optional[str]:
    v = _clean(v)
    if v is None:
        return None
    dt = pd.to_datetime(v, errors="coerce")
    return None if pd.isna(dt) else dt.strftime("%Y-%m-%d")


def normalize_records(source_key: str, df: pd.DataFrame) -> list:
    """Converts a source DataFrame into ierp ingest-media record dicts."""
    media_type, src = SOURCE_MAP.get(source_key, (source_key, source_key))
    records = []

    for _, row in df.iterrows():
        r = {k: _clean(v) for k, v in row.items()}
        title = _first(r, FIELD_CANDIDATES["title"])
        if not title or not str(title).strip():
            continue
        title = str(title).strip()

        review = _first(r, ("My Review", "my_comments", "notes"))
        records.append({
            "media_type": media_type,
            "title": title,
            "original_title": _first(r, FIELD_CANDIDATES["original_title"]),
            "year": _first(r, FIELD_CANDIDATES["year"]),
            "author": _first(r, FIELD_CANDIDATES["author"]),
            "source": src,
            "extra": {k: v for k, v in r.items() if v is not None and k not in _EXTRA_EXCLUDED},
            "status": _first(r, FIELD_CANDIDATES["status"]),
            "rating": _first(r, FIELD_CANDIDATES["rating"]),
            "progress": _first(r, FIELD_CANDIDATES["progress"]),
            "started_at": _date_str(_first(r, DATE_CANDIDATES["started_at"])),
            "finished_at": _date_str(_first(r, DATE_CANDIDATES["finished_at"])),
            "date_logged": _date_str(_first(r, DATE_CANDIDATES["date_logged"])),
            "review": (str(review).strip() or None) if review else None,
            "raw": {k: (str(v) if v is not None else None) for k, v in r.items()},
        })
    return records


def push_to_ierp(source_key: str, records: list) -> bool:
    """
    Writes records to a temp JSON file and pipes through `uv run ierp ingest-media`.
    Returns True on success; failures are printed, never raised (ingestion is
    best-effort so one broken source doesn't kill the whole get-data run).
    """
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
    except (subprocess.TimeoutExpired, OSError) as e:
        print(f"[ierp] Ingest error for {source_key}: {e}")
        return False
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
