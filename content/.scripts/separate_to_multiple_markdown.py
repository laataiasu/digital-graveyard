import re
import os
from pathlib import Path

# Input and output paths
input_file = 'backup.md'  # Replace with your actual file path
output_dir = 'output_notes'
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Read the input file
with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split by ---
entries = [e.strip() for e in content.split('---') if e.strip()]

# Regex for date and title
date_title_re = re.compile(r'(\d{4}-\d{2}-\d{2})(?:[^\d\w]*)(.*)?')

for i, entry in enumerate(entries):
    lines = entry.splitlines()
    title_line = next((line for line in lines if date_title_re.search(line)), None)

    if title_line:
        match = date_title_re.search(title_line)
        date = match.group(1)
        title = match.group(2).strip() if match.group(2) else date
    else:
        # Fallback if no date found (optional)
        date = 'unknown'
        title = 'untitled'

    # Sanitize filename
    safe_title = re.sub(r'[^\w\- ]', '', title).strip().replace(' ', '_')
    filename = f"{i+1:03d}_{safe_title}.md"

    # Construct frontmatter
    frontmatter = f"""---
date: {date}
tags:
- journal
title: {title}
---"""

    # Write file
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as out:
        out.write(f"{frontmatter}\n\n{entry}")
