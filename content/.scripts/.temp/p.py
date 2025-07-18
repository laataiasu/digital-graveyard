import pandas as pd
import os
import re
from pathlib import Path

def slugify(text):
    return re.sub(r'[^a-z0-9\-]', '', re.sub(r'\s+', '-', text.lower()))

# Load Excel file
excel_file = "Journal.xlsx"
df = pd.read_excel(excel_file)

# Output folder
output_dir = "markdown_notes"
Path(output_dir).mkdir(exist_ok=True)

for _, row in df.iterrows():
    date = str(row['date']).split(' ')[0]  # Keep only YYYY-MM-DD
    title = str(row['title']).strip()
    slug_title = slugify(title)
    filename = f"{date}-{slug_title}.md"
    filepath = os.path.join(output_dir, filename)

    # YAML frontmatter
    frontmatter = f"""---
title: "{title}"
date: {date}
source: "{str(row.get('source', '')).strip()}"
tags: [{str(row.get('tags', '')).strip()}]
url: "{str(row.get('url', '')).strip()}"
---

"""

    # Markdown body
    body = f"""## Details
{str(row.get('detail', '')).strip()}

## Notes
{str(row.get('notes', '')).strip()}

## Code
{str(row.get('code', '')).strip()}
"""

    # Write file
    with open(filepath, 'w', encoding='utf-8') as mdfile:
        mdfile.write(frontmatter + body)

print(f"Markdown files created in '{output_dir}' from '{excel_file}'")
