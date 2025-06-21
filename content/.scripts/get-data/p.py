import pandas as pd
from utils import sanitize_filename, recreate_folder, move_to_blog_path, write_markdown

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

output_dir = "Goodreads"
recreate_folder(output_dir)

for _, row in df.iterrows():
    title = sanitize_filename(row['Title'])
    filename = f"{title}.md"
    filepath = os.path.join(output_dir, filename)

    frontmatter = f"""---
title: "{row['Title']}"
author: "{row['Author']}"
date: "{row['Date Added']}"
my_rating: {row['My Rating'] or 0}
bookshelves: "{row['Bookshelves']}"
isbn: "{row['ISBN']}"
isbn13: "{row['ISBN13']}"
---
"""
    content = f"""# {row['Title']}

**Author:** {row['Author']}
**My Rating:** {row['My Rating']}
**Date Read:** {row['Date Read']}
**Bookshelves:** {row['Bookshelves']}

## Review

{row['My Review']}
"""
    write_markdown(filepath, frontmatter, content)

move_to_blog_path(output_dir, 'Read/Goodreads')