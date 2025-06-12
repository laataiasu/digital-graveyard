import os
import re
import yaml

def process_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match front matter
    front_matter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not front_matter_match:
        return  # No front matter, skip

    front_matter_str, body = front_matter_match.groups()
    try:
        front_matter = yaml.safe_load(front_matter_str)
    except yaml.YAMLError:
        print(f"YAML parse error in: {filepath}")
        return

    # Process tags
    if 'tags' in front_matter and isinstance(front_matter['tags'], list):
        front_matter['tags'] = [tag.lower() if isinstance(tag, str) else tag for tag in front_matter['tags']]

        # Dump new front matter
        new_front_matter_str = yaml.safe_dump(front_matter, sort_keys=False).strip()
        new_content = f"---\n{new_front_matter_str}\n---\n{body}"

        # Save file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

def process_directory(base_dir='.'):
    for root, _, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                process_markdown_file(filepath)

if __name__ == '__main__':
    process_directory('.')
