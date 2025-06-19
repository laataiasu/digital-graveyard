import os
from pathlib import Path
import re

MIN_DATE = "2001-01-01"

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for existing frontmatter
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n?', content, re.DOTALL)

    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        if 'date:' not in frontmatter:
            # Add date to existing frontmatter
            updated_frontmatter = f"date: {MIN_DATE}\n" + frontmatter
            new_content = f"---\n{updated_frontmatter}\n---\n" + content[frontmatter_match.end():]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added date to frontmatter: {file_path}")
    else:
        # No frontmatter — add it to the top
        new_content = f"---\ndate: {MIN_DATE}\n---\n\n{content}"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Created frontmatter with date: {file_path}")

def main():
    for md_file in Path('.').rglob('*.md'):
        process_markdown_file(md_file)

if __name__ == "__main__":
    main()
