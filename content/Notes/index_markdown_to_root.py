import os
import shutil
import yaml
from utils import sanitize_filename

CURRENT_DIR = os.getcwd()

def extract_title_from_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not (lines and lines[0].strip() == '---'):
        return None  # No frontmatter
    try:
        end_index = lines.index('---\n', 1)
    except ValueError:
        return None  # No closing ---
    frontmatter = ''.join(lines[1:end_index])
    try:
        metadata = yaml.safe_load(frontmatter)
        return metadata.get('title')
    except yaml.YAMLError:
        return None

def process_folders():
    for item in os.listdir(CURRENT_DIR):
        folder_path = os.path.join(CURRENT_DIR, item)
        if os.path.isdir(folder_path):
            contents = os.listdir(folder_path)
            if contents == ['index.md']:
                index_path = os.path.join(folder_path, 'index.md')
                title = extract_title_from_frontmatter(index_path)
                if title:
                    safe_title = sanitize_filename(title)
                    new_path = os.path.join(CURRENT_DIR, f'{safe_title}.md')
                    shutil.move(index_path, new_path)
                    os.rmdir(folder_path)
                    print(f'Moved and renamed: {item}/index.md -> {safe_title}.md')
                else:
                    print(f'Skipping (no title): {item}')

if __name__ == "__main__":
    process_folders()
