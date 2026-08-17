import os
import glob
import re
import datetime

CONTENT_DIR = "/home/al/Projects/digital-graveyard/content"
DATE_PATTERN = re.compile(r"(\d{4}-\d{2}-\d{2})")

def get_clean_title(filepath, content):
    # Try finding an H1 heading in content first
    for line in content.splitlines():
        line_s = line.strip()
        if line_s.startswith("# "):
            title = line_s[2:].strip().replace('"', '\\"')
            if title:
                return title
    
    # Fallback to filename
    filename = os.path.basename(filepath)
    name = os.path.splitext(filename)[0]
    # Strip date prefix if present
    name = re.sub(r"^\d{4}-\d{2}-\d{2}[-_]?", "", name).strip()
    if not name:
        name = os.path.splitext(filename)[0]
    return name.replace('"', '\\"')

def get_file_date(filepath, content):
    filename = os.path.basename(filepath)
    match = DATE_PATTERN.search(filename)
    if match:
        return match.group(1)
    
    match = DATE_PATTERN.search(content[:500])
    if match:
        return match.group(1)
    
    # Fallback to file mtime
    mtime = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    modified = False

    if not content.startswith("---"):
        # Missing frontmatter entirely
        title = get_clean_title(filepath, content)
        date = get_file_date(filepath, content)
        frontmatter = f"---\ntitle: \"{title}\"\ndate: {date}\ntags: []\n---\n\n"
        new_content = frontmatter + content
        modified = True
    else:
        parts = content.split("---", 2)
        if len(parts) < 3:
            # Malformed frontmatter
            title = get_clean_title(filepath, content)
            date = get_file_date(filepath, content)
            frontmatter = f"---\ntitle: \"{title}\"\ndate: {date}\ntags: []\n---\n\n"
            new_content = frontmatter + content
            modified = True
        else:
            fm_lines = parts[1].strip().splitlines()
            fm_dict_keys = [line.split(":")[0].strip() for line in fm_lines if ":" in line]

            new_fm_lines = list(fm_lines)
            
            if "title" not in fm_dict_keys:
                title = get_clean_title(filepath, content)
                new_fm_lines.insert(0, f'title: "{title}"')
                modified = True
            
            if "date" not in fm_dict_keys:
                date = get_file_date(filepath, content)
                new_fm_lines.append(f"date: {date}")
                modified = True

            if "tags" not in fm_dict_keys:
                new_fm_lines.append("tags: []")
                modified = True

            if modified:
                new_fm = "\n".join(new_fm_lines)
                new_content = f"---\n{new_fm}\n---" + parts[2]

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def main():
    fixed_count = 0
    total_files = 0

    for root, dirs, files in os.walk(CONTENT_DIR):
        # Skip templates and obsidian settings
        rel_root = os.path.relpath(root, CONTENT_DIR)
        if rel_root.startswith(".obsidian") or rel_root.startswith("templates"):
            continue

        for file in files:
            if file.endswith(".md"):
                total_files += 1
                filepath = os.path.join(root, file)
                if process_file(filepath):
                    fixed_count += 1

    print(f"Processed {total_files} files. Updated frontmatter for {fixed_count} files.")

if __name__ == "__main__":
    main()
