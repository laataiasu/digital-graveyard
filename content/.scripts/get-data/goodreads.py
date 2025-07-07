import os
import pandas as pd
import re
import shutil
import string
from utils import sanitize_filename

# Load and clean the CSV
def clean_isbn(val):
    if pd.isna(val): return ""
    return str(val).replace('="', '').replace('"', '').strip()

def sanitize_text(text):
    if pd.isna(text):
        return ""
    return str(text).strip()


# Read and clean CSV
df = pd.read_csv("goodreads.csv", dtype=str)
df.columns = [col.strip() for col in df.columns]
df['ISBN'] = df['ISBN'].apply(clean_isbn)
df['ISBN13'] = df['ISBN13'].apply(clean_isbn)
for col in df.columns:
    df[col] = df[col].apply(sanitize_text)

# Recreate output folder (idempotent)
output_dir = "Goodreads"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

# Write .md files
for _, row in df.iterrows():
    title = sanitize_filename(row['Title'] or "untitled")
    filename = f"{title}.md"
    filepath = os.path.join(output_dir, filename)

    frontmatter = f"""---
title: "{row['Title']}"
author: "{row['Author']}"
date: "{row['Date Added']}"
tags: ["book"]
---

# {row['Title']}

**Author:** {row['Author']}  
**My Rating:** {row['My Rating']}  
**Date Read:** {row['Date Read']}  
**Bookshelves:** {row['Bookshelves']}

- author_lf: "{row['Author l-f']}"
- additional_authors: "{row['Additional Authors']}"
- isbn: "{row['ISBN']}"
- isbn13: "{row['ISBN13']}"
- publisher: "{row['Publisher']}"
- binding: "{row['Binding']}"
- pages: {row['Number of Pages'] or 0}
- year_published: {row['Year Published'] or 0}
- original_publication_year: {row['Original Publication Year'] or 0}
- date_read: "{row['Date Read']}"
- date_added: "{row['Date Added']}"
- my_rating: {row['My Rating'] or 0}
- average_rating: {row['Average Rating'] or 0}
- bookshelves: "{row['Bookshelves']}"
- exclusive_shelf: "{row['Exclusive Shelf']}"
- read_count: {row['Read Count'] or 0}
- owned_copies: {row['Owned Copies'] or 0}
- spoiler: "{row['Spoiler']}"
- private_notes: "{row['Private Notes']}"

## Review

{row['My Review']}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)

# Sync to BLOG_PATH if defined
blog_path = os.environ.get('BLOG_PATH')
if blog_path:
    dest_path = os.path.join(blog_path, 'Read', 'Goodreads')

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.move(output_dir, dest_path)
else:
    print("Environment variable BLOG_PATH is not set.")
