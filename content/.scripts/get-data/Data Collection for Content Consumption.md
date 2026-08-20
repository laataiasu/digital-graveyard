---
title: "📥 Data Collection for Content Consumption"
date: 2026-08-20
tags: [guide]
publish_external: false
---

# 📥 Data Collection for Content Consumption

This system automatically fetches and syncs personal media consumption data directly from online platforms into your digital garden markdown notes. **Zero manual CSV exports, XML downloads, or Google Sheets are required.**

---

## 🚀 Quickstart

Run the automated ingestion script with `uv`:

```bash
cd content/.scripts/get-data

# 1. Pre-flight check (test connectivity & counts without modifying files):
uv run main.py --check

# 2. Fetch & sync all 5 platforms at once:
uv run main.py
```

Or fetch a specific platform:

```bash
# Goodreads (Books)
uv run main.py --source goodreads

# Letterboxd (Films & Ratings)
uv run main.py --source letterboxd

# AniList (Anime)
uv run main.py --source anilist_anime

# AniList (Manga)
uv run main.py --source anilist_manga

# MyDramaList (Asian & Korean Drama)
uv run main.py --source mydramalist
```

---

## 🛡️ Reliability & Early Warning Features

1. **Pre-flight Health Check (`--check` / `--dry-run`)**: Test endpoints, user profiles, and record counts in 20 seconds without touching your Markdown notes.
2. **Exponential Backoff & Retries**: Automatically retries transient network or server timeouts up to 3 times.
3. **Data Integrity Guarantee**: If an endpoint fails or returns 0 records, existing vault notes are protected and **never** deleted or overwritten with empty data.
4. **Summary & Non-Zero Exit Codes**: Clear diagnostics table at the end of each run, exiting with `code 1` if any source fails (for CI or scheduled tasks).

---

## 📦 Connected Data Sources

| Source | Target Folder | Method / Protocol | Username / Profile ID |
| :--- | :--- | :--- | :--- |
| **Goodreads** | `content/Read/Goodreads/` | Paginated RSS Feed | `74584614` |
| **Letterboxd** | `content/Watch/Letterboxd/` | Automated Scraper (`curl_cffi`) | `PenyulTekowel` |
| **AniList (Anime)** | `content/Watch/Anime/` | Official GraphQL API | `laataiasu` |
| **AniList (Manga)** | `content/Read/Manga/` | Official GraphQL API | `laataiasu` |
| **MyDramaList** | `content/Watch/Drama/` | Table Parser | `Chanculus` |

---

## ⚙️ Configuration & Customization

- Profile IDs and usernames are configured in [`config.py`](file:///home/al/Projects/digital-graveyard/content/.scripts/get-data/config.py) under the `PROFILES` dictionary.
- Output mapping, frontmatter rules, and Markdown templates are defined per source in `DATA_SOURCES`.
- Optional: Set `BLOG_PATH` if syncing to a non-standard content directory:
  ```bash
  export BLOG_PATH="/path/to/custom/content"
  ```