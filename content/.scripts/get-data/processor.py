import os
import re
import datetime
import pandas as pd
import yaml
from helpers import sanitize_filename, create_output_dir, sync_to_blog, DEFAULT_CONTENT_PATH


def clean_val(v):
    """Cleans values for frontmatter."""
    if pd.isna(v) or v is None:
        return None
    if isinstance(v, float) and v.is_integer():
        return int(v)
    return v


def format_yaml_value(val):
    """Formats values for Obsidian standard YAML frontmatter."""
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
    elif val is None or str(val).strip() in ["", "None", "nan"]:
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


def process_source(config, dry_run=False):
    """
    Processes a single data source based on the provided configuration.
    Returns the count of processed notes.
    """
    # Load data
    loader = config["loader"]
    loader_args = config.get("loader_args", {})
    df = loader(**loader_args) if loader_args else loader()

    if df is None or df.empty:
        raise ValueError("Loader returned 0 records.")

    if dry_run:
        print(f"🔎 [Dry-run] Successfully fetched {len(df)} records (no files written).")
        return len(df)

    # Prepare temporary output directory
    output_dir = config["output_dir"]
    create_output_dir(output_dir)

    # Destination directory to check for existing files / preserved dates
    blog_path = os.environ.get('BLOG_PATH', DEFAULT_CONTENT_PATH)
    dest_dir = os.path.join(blog_path, config.get("blog_sync_path", ""))

    # Configuration details
    title_column = config["title_column"]
    date_column = config.get("date_column")
    default_date = config.get("default_date", "2016-01-01")
    frontmatter_mapping = config.get("frontmatter_mapping", {})
    tags = config.get("tags", [])
    publish_external = config.get("publish_external", False)
    content_template = config.get("content_template", "")

    processed_count = 0
    for _, row in df.iterrows():
        title = row.get(title_column, "")
        if pd.isna(title) or not str(title).strip():
            continue

        title_str = str(title).strip()
        filename = f"{sanitize_filename(title_str)}.md"
        filepath = os.path.join(output_dir, filename)
        existing_filepath = os.path.join(dest_dir, filename) if os.path.exists(dest_dir) else None

        # Check existing file for date preservation if incoming date is missing/default
        existing_date = None
        if existing_filepath and os.path.exists(existing_filepath):
            try:
                with open(existing_filepath, "r", encoding="utf-8") as ef:
                    content_str = ef.read()
                    date_match = re.search(r"^date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", content_str, re.MULTILINE)
                    if date_match:
                        existing_date = date_match.group(1)
            except Exception:
                pass

        # Prepare frontmatter
        frontmatter = {}
        if frontmatter_mapping == "all":
            for col, val in row.items():
                frontmatter[col] = clean_val(val)
            frontmatter["title"] = title_str
        else:
            for key, value_col in frontmatter_mapping.items():
                frontmatter[key] = clean_val(row.get(value_col))

        # Always ensure title is clean string
        frontmatter["title"] = title_str

        # Date handling
        date_to_format = None
        if date_column and date_column in row and pd.notna(row[date_column]):
            date_to_format = row[date_column]
        elif existing_date:
            date_to_format = existing_date
        elif "date" in frontmatter and pd.notna(frontmatter["date"]):
            date_to_format = frontmatter["date"]
        elif default_date:
            date_to_format = default_date

        if pd.notna(date_to_format):
            dt_date = pd.to_datetime(date_to_format, errors="coerce")
            if pd.notna(dt_date) and dt_date != pd.Timestamp.min:
                frontmatter["date"] = dt_date.strftime("%Y-%m-%d")
            elif existing_date:
                frontmatter["date"] = existing_date
            else:
                frontmatter["date"] = default_date
        else:
            frontmatter["date"] = existing_date or default_date

        # Set tags and privacy flag
        if tags:
            frontmatter["tags"] = tags
        frontmatter["publish_external"] = publish_external

        # Format content
        content_formatter = config.get("content_formatter")
        if callable(content_formatter):
            try:
                content = content_formatter(row)
            except Exception as e:
                print(f"Formatter error for {title_str}: {e}")
                content = ""
        elif content_template:
            row_dict = {k: ("" if pd.isna(v) or v is None else v) for k, v in row.to_dict().items()}
            try:
                content = content_template.format(**row_dict)
            except KeyError:
                content = ""
        else:
            content = ""

        write_markdown_file(filepath, frontmatter, content)
        processed_count += 1

    print(f"Generated {processed_count} markdown files.")

    # Sync to blog
    if "blog_sync_path" in config:
        sync_to_blog(output_dir, config["blog_sync_path"])

    return processed_count


def write_markdown_file(filepath, frontmatter, content):
    """Writes a markdown file with Obsidian-standard frontmatter and markdown body."""
    title = str(frontmatter.get("title", "")).strip()
    safe_title = title.replace('\\', '\\\\').replace('"', '\\"')

    date = frontmatter.get("date", "2016-01-01")
    if isinstance(date, (datetime.date, datetime.datetime)):
        date_str = date.strftime("%Y-%m-%d")
    else:
        date_str = str(date).split()[0] if date else "2016-01-01"

    tags = frontmatter.get("tags", [])
    tags_formatted = "[" + ", ".join(tags) + "]" if tags else "[]"

    publish_external = "true" if frontmatter.get("publish_external", False) else "false"

    lines = [
        "---",
        f'title: "{safe_title}"',
        f'date: {date_str}',
        f'tags: {tags_formatted}',
        f'publish_external: {publish_external}',
    ]

    standard_keys = {"title", "date", "tags", "publish_external"}
    for k, v in frontmatter.items():
        if k in standard_keys:
            continue
        if v is not None and str(v).strip() not in ["", "None", "nan"]:
            val_str = format_yaml_value(v)
            lines.append(f"{k}: {val_str}")

    lines.append("---")
    fm_text = "\n".join(lines)

    full_content = f"{fm_text}\n\n{content.strip()}\n" if content.strip() else f"{fm_text}\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)
