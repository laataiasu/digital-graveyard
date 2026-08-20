# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "beautifulsoup4>=4.12.0",
#     "pandas>=2.2.0",
#     "requests>=2.31.0",
# ]
# ///

import os
import re
import pandas as pd
import requests
from dataloaders import load_mydramalist_data


def export_kdrama_to_trakt_csv(username="Chanculus", output_file="trakt_kdrama_import.csv"):
    """
    Fetches all KDramas/Movies from MyDramaList and exports a clean CSV formatted for Trakt.tv.
    """
    df = load_mydramalist_data(username=username)
    if df.empty:
        print("❌ No MyDramaList records found.")
        return

    trakt_records = []

    for _, row in df.iterrows():
        raw_type = str(row.get("Type", "")).lower()
        title = str(row.get("Title", "")).strip()
        year = row.get("Year")
        score = row.get("Score")
        progress = str(row.get("Progress", "")).strip()

        # Map to Trakt media type: 'show' or 'movie'
        media_type = "movie" if "movie" in raw_type or "film" in raw_type else "show"

        # Trakt ratings are 1-10 integers or floats
        try:
            rating = round(float(score), 1) if score and not pd.isna(score) and float(score) > 0 else ""
        except ValueError:
            rating = ""

        # Determine watch status based on progress (e.g. 16/16 -> completed/watched)
        status = "watched"
        if "/" in progress:
            parts = progress.split("/")
            if len(parts) == 2 and parts[0] != parts[1] and parts[0] == "0":
                status = "plan_to_watch"

        trakt_records.append({
            "Title": title,
            "Year": year if pd.notna(year) else "",
            "Type": media_type,
            "Rating": rating,
            "Status": status,
            "Progress": progress,
            "Source": "MyDramaList",
        })

    out_df = pd.DataFrame(trakt_records)
    
    # Save standard CSV
    out_path = os.path.abspath(output_file)
    out_df.to_csv(out_path, index=False, encoding="utf-8")
    
    print(f"\n✅ Successfully exported {len(out_df)} items to Trakt CSV:")
    print(f"   📁 File: {out_path}")
    print("\nSample rows:")
    print(out_df.head(5)[["Title", "Year", "Type", "Rating", "Status"]].to_string(index=False))


if __name__ == "__main__":
    export_kdrama_to_trakt_csv()
