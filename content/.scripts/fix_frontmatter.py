import os
import re
import yaml
import datetime
import subprocess

CONTENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATE_PATTERN = re.compile(r"(\d{4}-\d{2}-\d{2})")

def get_head_publish_true_files():
    """Get the exact list of files that had publish_external: true in git HEAD."""
    try:
        res = subprocess.run(
            ["git", "-c", "core.quotepath=false", "grep", "-l", "publish_external: true", "HEAD", "--", "content/"],
            cwd=os.path.dirname(CONTENT_DIR),
            capture_output=True,
            text=True
        )
        files = set()
        for line in res.stdout.splitlines():
            line = line.strip().replace("HEAD:", "").strip('"\'')
            # Convert to relative path from CONTENT_DIR
            if line.startswith("content/"):
                line = line[len("content/"):]
            files.add(os.path.normpath(line))
        return files
    except Exception as e:
        print(f"Warning: Could not fetch HEAD publish_external files from git: {e}")
        return set()

HEAD_PUBLISH_TRUE_FILES = get_head_publish_true_files()

def clean_title_str(val):
    if not val:
        return ""
    val = str(val).strip()
    # Strip markdown links e.g. [Title](url) -> Title
    m_link = re.match(r"^\[(.*?)\]\([^)]+\)$", val)
    if m_link:
        val = m_link.group(1).strip()
    # Strip wikilinks e.g. [[Title]] -> Title
    m_wiki = re.match(r"^\[\[(.*?)\]\]$", val)
    if m_wiki:
        val = m_wiki.group(1).strip()
    # Strip bold markdown e.g. **Title** -> Title
    m_bold = re.match(r"^\*\*(.*?)\*\*$", val)
    if m_bold:
        val = m_bold.group(1).strip()
    # Strip surrounding quotes and whitespace
    val = val.strip("\"'\n\r\t")
    return val

def get_file_date(filepath, content, existing_date=None):
    if existing_date is not None:
        if isinstance(existing_date, (datetime.date, datetime.datetime)):
            return existing_date.strftime("%Y-%m-%d")
        match = DATE_PATTERN.search(str(existing_date))
        if match:
            # Check year not 0000
            if not match.group(1).startswith("0000"):
                return match.group(1)
    filename = os.path.basename(filepath)
    match = DATE_PATTERN.search(filename)
    if match and not match.group(1).startswith("0000"):
        return match.group(1)
    match = DATE_PATTERN.search(content[:500])
    if match and not match.group(1).startswith("0000"):
        return match.group(1)
    mtime = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

APPROVED_FORMAT_TAGS = {
    # Media & Consumption
    "film", "anime", "drama", "youtube", "book", "manga", "sound",
    # Writing & Reflection
    "journal", "essay", "review", "reflection", "literature", "travelogue",
    # Knowledge & Technical
    "guide", "cheatsheet", "note", "interesting-terms",
    # Projects
    "project", "case-study",
    # Entities / Indexes
    "figure", "company", "software", "gadget", "country", "organization", "school", "religion"
}

TAG_MAPPINGS = {
    "tips": "guide",
    "tutorial": "guide",
    "refleksi": "reflection",
    "self-reflection": "reflection",
    "poetry": "literature",
    "lyrics": "literature",
    "orgnization": "organization",
    "classic-thinker": "figure",
    "modern-thinker": "figure",
    "public-intellectual": "figure",
    "pseudocomedy": "essay",
    "event": "journal",
    "travel": "travelogue",
    "travelog": "travelogue",
    "travel-log": "travelogue",
}

def infer_tag_from_path(rel_path):
    parts = rel_path.split(os.sep)
    top = parts[0]
    if top == "Watch":
        if "Anime" in parts:
            return ["anime"]
        return ["film"]
    elif top == "Read":
        if "Manga" in parts:
            return ["manga"]
        return ["book"]
    elif top == "Write":
        if len(parts) > 1 and parts[1] == "Journal":
            return ["journal"]
        return ["essay"]
    elif top == "Knowledge":
        if "Tech Tips" in rel_path or "Linux Tips" in rel_path:
            return ["guide"]
        return ["note"]
    elif top == "Projects":
        return ["project"]
    elif top == "Tags":
        if len(parts) > 1:
            sub = parts[1].lower()
            if sub in APPROVED_FORMAT_TAGS:
                return [sub]
        return []
    return []

def normalize_tags(raw_tags, rel_path=""):
    if not raw_tags:
        tags_list = []
    elif isinstance(raw_tags, str):
        tags_list = [t.strip() for t in raw_tags.split(",") if t.strip()]
    elif isinstance(raw_tags, (list, tuple, set)):
        tags_list = list(raw_tags)
    else:
        tags_list = [str(raw_tags)]
    
    clean = []
    for t in tags_list:
        if t is None:
            continue
        t_str = str(t).strip().lstrip("#").lower()
        mapped = TAG_MAPPINGS.get(t_str, t_str)
        if mapped in APPROVED_FORMAT_TAGS and mapped not in clean:
            clean.append(mapped)
            
    if not clean and rel_path:
        clean = infer_tag_from_path(rel_path)
        
    return clean

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

INLINE_TAG_REPLACEMENTS = [
    (r"(?<!\w)#Porn\b", "porn"),
    (r"(?<!\w)#porn\b", "porn"),
    (r"(?<!\w)#Bitcoin\b", "[[Bitcoin]]"),
    (r"(?<!\w)#bitcoin\b", "[[Bitcoin]]"),
    (r"(?<!\w)#Data\b", "[[Data]]"),
    (r"(?<!\w)#Currency\b", "[[Currency]]"),
    (r"(?<!\w)#muslim\b", "[[Muslim]]"),
    (r"(?<!\w)#Muslim\b", "[[Muslim]]"),
    (r'"#YOLO"', '"YOLO"'),
    (r"(?<!\w)#YOLO\b", "YOLO"),
    (r"(?<!\w)#literature\b", "literature"),
    (r"#lhkpn #kpk #compliance #anti-corruption #indonesia #public-official", "[[LHKPN]] [[KPK]] [[Compliance]] [[Anti-corruption]] [[Indonesia]] [[Public Official]]"),
    (r"#open-data #transparency #indonesia #power-network", "[[Open Data]] [[Transparency]] [[Indonesia]] [[Power Network]]"),
    (r"(?<!\w)#asalbukan02\b", "asalbukan02"),
]

def clean_inline_tags(body):
    code_blocks = []
    def save_cb(match):
        code_blocks.append(match.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"

    # Match fenced code blocks (``` or ~~~ with 3+ characters)
    body = re.sub(r"(?ms)^([`~]{3,})[^\n]*\n.*?\n\1", save_cb, body)
    body = re.sub(r"```[\s\S]*?```", save_cb, body)
    # Match inline code
    body = re.sub(r"`[^`\n]+`", save_cb, body)

    heading_links = []
    def save_hl(match):
        heading_links.append(match.group(0))
        return f"__HEADING_LINK_{len(heading_links)-1}__"
    body = re.sub(r"\[\[#[^\]]*\]\]", save_hl, body)

    for pattern, repl in INLINE_TAG_REPLACEMENTS:
        body = re.sub(pattern, repl, body)

    for i, hl in enumerate(heading_links):
        body = body.replace(f"__HEADING_LINK_{i}__", hl)

    for i, cb in enumerate(code_blocks):
        body = body.replace(f"__CODE_BLOCK_{i}__", cb)

    return body

def format_yaml_extra_value(val):
    if isinstance(val, bool):
        return "true" if val else "false"
    elif isinstance(val, (int, float)):
        return str(val)
    elif isinstance(val, (datetime.date, datetime.datetime)):
        return val.strftime("%Y-%m-%d")
    elif isinstance(val, list):
        items = []
        for x in val:
            if isinstance(x, str):
                x_clean = x.replace('"', '\\"')
                items.append(f'"{x_clean}"' if (":" in x or "#" in x or "," in x or "[" in x) else x_clean)
            elif isinstance(x, bool):
                items.append("true" if x else "false")
            else:
                items.append(str(x))
        return "[" + ", ".join(items) + "]"
    elif val is None:
        return "null"
    else:
        s = str(val).strip()
        s_escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        if (s == "0000-00-00" or 
            s.startswith("0000") or 
            any(c in s for c in [':', '#', '[', ']', '{', '}', ',', '"', "'"]) or 
            s.lower() in ("true", "false", "yes", "no", "null")):
            return f'"{s_escaped}"'
        return s_escaped

def build_fixed_content(full_content, filepath):
    """Return the fixed content for a file without writing it (used by --dry-run)."""
    rel_path = os.path.relpath(filepath, CONTENT_DIR)
    norm_rel = os.path.normpath(rel_path)

    parts = full_content.split("---", 2)
    has_fm = full_content.startswith("---") and len(parts) >= 3

    fm_data = {}
    body = full_content

    if has_fm:
        try:
            raw_fm = re.sub(r":\s*0000-00-00\b", ': "0000-00-00"', parts[1])
            parsed = yaml.safe_load(raw_fm)
            if isinstance(parsed, dict):
                fm_data = parsed
        except Exception:
            for line in parts[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm_data[k.strip()] = v.strip().strip('"\'')
        body = parts[2]

    # 1. Resolve Title
    raw_title = fm_data.get("title") or fm_data.get("series_title") or fm_data.get("manga_title")
    if raw_title:
        title = clean_title_str(str(raw_title))
    else:
        found_h1 = None
        for line in body.splitlines():
            line_s = line.strip()
            if line_s.startswith("# "):
                found_h1 = clean_title_str(line_s[2:])
                break
        if found_h1:
            title = found_h1
        else:
            filename = os.path.basename(filepath)
            name = os.path.splitext(filename)[0]
            name = re.sub(r"^\d{4}-\d{2}-\d{2}[-_]?", "", name).strip()
            title = name if name else os.path.splitext(filename)[0]

    # 2. Resolve Date
    date = get_file_date(filepath, body, fm_data.get("date"))

    # 3. Resolve Tags
    tags = normalize_tags(fm_data.get("tags"), rel_path)

    # 4. Resolve publish_external (STRICT PRIVACY: False unless originally true in git HEAD or explicitly set true)
    if norm_rel in HEAD_PUBLISH_TRUE_FILES or fm_data.get("publish_external") is True:
        # Strictly enforce privacy for journals, drafts, and personal links
        if "/Journal/" in rel_path or "\\Journal\\" in rel_path or "_draft" in rel_path or rel_path == "Write/Links.md":
            publish_external = False
        else:
            publish_external = True
    else:
        publish_external = False

    # Format standard primary fields
    tags_formatted = "[" + ", ".join(tags) + "]" if tags else "[]"
    safe_title = title.replace('\\', '\\\\').replace('"', '\\"')

    lines = [
        "---",
        f'title: "{safe_title}"',
        f'date: {date}',
        f'tags: {tags_formatted}',
        f'publish_external: {"true" if publish_external else "false"}'
    ]

    # Preserve additional custom/domain metadata cleanly
    standard_keys = {"title", "date", "tags", "publish_external"}
    for k, v in fm_data.items():
        if k in standard_keys:
            continue
        val_str = format_yaml_extra_value(v)
        lines.append(f"{k}: {val_str}")

    lines.append("---")
    new_fm = "\n".join(lines)

    # Clean body
    clean_body = clean_inline_tags(clean_h1_headings(body)).lstrip("\r\n")
    new_full_content = f"{new_fm}\n\n{clean_body}\n" if clean_body else f"{new_fm}\n"
    return new_full_content

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        full_content = f.read()
    new_full_content = build_fixed_content(full_content, filepath)
    if new_full_content != full_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_full_content)
        return True
    return False

def main():
    import sys
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    if dry_run:
        print("🏃 DRY RUN — no files will be modified.\n")

    def process_file_safe(filepath):
        if dry_run:
            import io
            with open(filepath, encoding="utf-8") as f:
                full_content = f.read()
            # simulate: build new content without writing
            new_full_content = build_fixed_content(full_content, filepath)
            return new_full_content != full_content
        return process_file(filepath)

    fixed_count = 0
    total_files = 0

    print(f"🔒 Loaded {len(HEAD_PUBLISH_TRUE_FILES)} explicitly public notes from HEAD.")

    for root, dirs, files in os.walk(CONTENT_DIR):
        rel_root = os.path.relpath(root, CONTENT_DIR)
        if any(part in rel_root.split(os.sep) for part in [".obsidian", "templates", ".scripts"]):
            continue

        for file in sorted(files):
            if file.endswith(".md"):
                total_files += 1
                filepath = os.path.join(root, file)
                if process_file_safe(filepath):
                    fixed_count += 1

    label = "Would update" if dry_run else "Updated"
    print(f"✅ Processed {total_files} files. {label} {fixed_count} files (strictly private by default).")

if __name__ == "__main__":
    main()
