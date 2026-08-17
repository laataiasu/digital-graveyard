import os
import re
import yaml
import datetime

CONTENT_DIR = "/home/al/Projects/digital-graveyard/content"
DATE_PATTERN = re.compile(r"(\d{4}-\d{2}-\d{2})")

KNOWN_INLINE_TAG_REPLACEMENTS = {
    r"(?<!\w)#Bitcoin\b": "[[Bitcoin]]",
    r"(?<!\w)#Data\b": "[[Data]]",
    r"(?<!\w)#Currency\b": "[[Currency]]",
    r"(?<!\w)#Porn\b": "pornography",
    r"(?<!\w)#muslim\b": "[[Muslim]]",
    r"(?<!\w)#indonesia\b": "Indonesia",
    r"(?<!\w)#literature\b": "literature",
}

def clean_title_str(val):
    if not val:
        return ""
    val = val.strip()
    # Strip [[...]]
    m = re.match(r"^\[\[(.*?)\]\]$", val)
    if m:
        val = m.group(1)
    val = val.strip("\"'")
    return val

def clean_h1_headings(body):
    lines = body.splitlines()
    new_lines = []
    for line in lines:
        m = re.match(r"^(#+)\s+\[\[(.*?)\]\](.*)$", line)
        if m:
            hashes, heading, rest = m.groups()
            new_lines.append(f"{hashes} {heading}{rest}")
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

def replace_inline_tags(body):
    # Don't replace inside code blocks
    code_blocks = []
    def save_cb(match):
        code_blocks.append(match.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"

    body = re.sub(r"```[\s\S]*?```", save_cb, body)
    body = re.sub(r"`[^`]*`", save_cb, body)

    for pattern, repl in KNOWN_INLINE_TAG_REPLACEMENTS.items():
        body = re.sub(pattern, repl, body)

    for i, cb in enumerate(code_blocks):
        body = body.replace(f"__CODE_BLOCK_{i}__", cb)

    return body

def get_file_date(filepath, content, existing_date=None):
    if existing_date:
        match = DATE_PATTERN.search(str(existing_date))
        if match:
            return match.group(1)
    
    filename = os.path.basename(filepath)
    match = DATE_PATTERN.search(filename)
    if match:
        return match.group(1)
    
    match = DATE_PATTERN.search(content[:500])
    if match:
        return match.group(1)
    
    mtime = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        full_content = f.read()

    rel_path = os.path.relpath(filepath, CONTENT_DIR)
    is_draft = "_draft" in rel_path

    parts = full_content.split("---", 2)
    has_fm = full_content.startswith("---") and len(parts) >= 3

    fm_data = {}
    body = full_content

    if has_fm:
        try:
            parsed = yaml.safe_load(parts[1])
            if isinstance(parsed, dict):
                fm_data = parsed
        except Exception:
            # Simple line parser fallback
            for line in parts[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm_data[k.strip()] = v.strip()
        body = parts[2]
    
    # Clean Title
    title = fm_data.get("title")
    if title:
        title = clean_title_str(str(title))
    else:
        # Infer title from filename or H1
        filename = os.path.basename(filepath)
        name = os.path.splitext(filename)[0]
        name = re.sub(r"^\d{4}-\d{2}-\d{2}[-_]?", "", name).strip()
        title = name if name else os.path.splitext(filename)[0]
    
    # Safely escape title for YAML double-quoted string
    safe_title = title.replace('\\', '\\\\').replace('"', '\\"')

    # Clean Date
    date = get_file_date(filepath, body, fm_data.get("date"))

    # Clean Tags
    tags = fm_data.get("tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    elif not isinstance(tags, list):
        tags = []
    clean_tags = []
    for t in tags:
        if t is not None:
            t_str = str(t).strip().lower()
            if t_str and t_str not in clean_tags:
                clean_tags.append(t_str)

    # Clean publish_external
    publish_external = fm_data.get("publish_external")
    if is_draft or fm_data.get("draft") is True:
        publish_external = False
    elif publish_external is None:
        publish_external = True
    else:
        publish_external = bool(publish_external)

    # Clean body
    new_body = clean_h1_headings(body)
    new_body = replace_inline_tags(new_body)

    # Build new frontmatter
    # Format tags line
    tags_formatted = "[" + ", ".join(clean_tags) + "]" if clean_tags else "[]"
    
    new_fm_lines = [
        "---",
        f'title: "{safe_title}"',
        f'date: {date}',
        f'tags: {tags_formatted}',
        f'publish_external: {str(publish_external).lower()}',
        "---"
    ]
    new_fm = "\n".join(new_fm_lines)

    # Clean leading newlines on body
    new_body = new_body.lstrip("\r\n")
    new_full_content = f"{new_fm}\n\n{new_body}\n" if new_body else f"{new_fm}\n"

    if new_full_content != full_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_full_content)
        return True
    return False

def main():
    updated = 0
    total = 0
    for root, dirs, files in os.walk(CONTENT_DIR):
        rel_root = os.path.relpath(root, CONTENT_DIR)
        if rel_root.startswith(".obsidian") or rel_root.startswith("templates") or rel_root.startswith(".scripts"):
            continue
        for f in files:
            if f.endswith(".md"):
                total += 1
                fp = os.path.join(root, f)
                if process_file(fp):
                    updated += 1

    print(f"Total files checked: {total}. Updated: {updated}.")

if __name__ == "__main__":
    main()
