import os
import re
import yaml

def update_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to match YAML frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n?(.*)', content, re.DOTALL)

    if frontmatter_match:
        frontmatter_str, body = frontmatter_match.groups()
        frontmatter = yaml.safe_load(frontmatter_str) or {}
    else:
        # No frontmatter found, initialize
        frontmatter = {}
        body = content

    if 'publish_external' not in frontmatter:
        frontmatter['publish_external'] = True
        new_frontmatter = yaml.dump(frontmatter, sort_keys=False).strip()
        new_content = f"---\n{new_frontmatter}\n---\n{body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
    else:
        print(f"Already set: {filepath}")

def process_markdown_files():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                update_frontmatter(filepath)

if __name__ == "__main__":
    process_markdown_files()
