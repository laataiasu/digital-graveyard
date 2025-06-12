import os
import re

def title_case(text):
    return text.replace('-', ' ').title()

def has_frontmatter(content):
    return content.lstrip().startswith('---')

def process_file(filepath):
    filename = os.path.basename(filepath)
    match = re.match(r'(\d{4}-\d{2}-\d{2})(?:-(.*))?\.md$', filename)
    if not match:
        print(f"Skipping (filename doesn't match): {filename}")
        return

    date = match.group(1)
    raw_title = match.group(2)
    title = title_case(raw_title) if raw_title else date

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if has_frontmatter(content):
        print(f"Skipping (already has frontmatter): {filepath}")
        return

    frontmatter = f"""---
title: "{title}"
date: {date}
tags: ["journal"]
---

"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

    print(f"Updated: {filepath}")

def process_all_markdown_files():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                process_file(filepath)

if __name__ == "__main__":
    process_all_markdown_files()
