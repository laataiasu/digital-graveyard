import os
import yaml

TAGS_TO_ADD = {"software"}

def update_or_create_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) < 3:
            return  # Malformed frontmatter, skip
        _, frontmatter_text, body = parts
        try:
            frontmatter = yaml.safe_load(frontmatter_text) or {}
        except yaml.YAMLError:
            return  # Invalid YAML, skip
    else:
        frontmatter = {}
        body = content

    existing_tags = set(frontmatter.get('tags', [])) if isinstance(frontmatter.get('tags'), list) else set()
    new_tags = sorted(existing_tags | TAGS_TO_ADD)
    frontmatter['tags'] = new_tags

    # Reconstruct the file
    new_frontmatter_text = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    new_content = f"---\n{new_frontmatter_text}\n---\n{body.lstrip()}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Process all .md files in current directory
for filename in os.listdir('.'):
    if filename.endswith('.md'):
        update_or_create_frontmatter(filename)
