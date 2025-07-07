import os
import pandas as pd
import yaml
from helpers import sanitize_filename, create_output_dir, sync_to_blog

def process_source(config):
    """Processes a single data source based on the provided configuration."""
    # Load data
    loader = config["loader"]
    loader_args = config.get("loader_args", {})
    df = loader(**loader_args) if loader_args else loader()

    # Prepare output directory
    output_dir = config["output_dir"]
    create_output_dir(output_dir)

    # Get configuration details
    title_column = config["title_column"]
    date_column = config.get("date_column")
    default_date = config.get("default_date")
    frontmatter_mapping = config.get("frontmatter_mapping", {})
    tags = config.get("tags", [])
    content_template = config.get("content_template", "")

    # Generate markdown files
    for _, row in df.iterrows():
        title = row.get(title_column, "")
        if pd.isna(title) or not title:
            continue

        # Sanitize filename
        filename = f"{sanitize_filename(title)}.md"
        filepath = os.path.join(output_dir, filename)

        # Prepare frontmatter
        frontmatter = {}
        if frontmatter_mapping == "all":
            frontmatter = row.to_dict()
            # Ensure title is set correctly even if the column name is different
            frontmatter['title'] = title
        else:
            for key, value_col in frontmatter_mapping.items():
                frontmatter[key] = row.get(value_col)

        if tags:
            frontmatter["tags"] = tags

        # Ensure date is present and correctly formatted
        date_to_format = None
        if date_column and date_column in row and pd.notna(row[date_column]):
            date_to_format = row[date_column]
        elif 'date' in frontmatter and pd.notna(frontmatter['date']):
            date_to_format = frontmatter['date']
        elif default_date:
            date_to_format = default_date

        if pd.notna(date_to_format):
            # Convert to datetime and format, coercing errors to NaT
            dt_date = pd.to_datetime(date_to_format, errors='coerce')
            if pd.notna(dt_date):
                frontmatter['date'] = dt_date.strftime('%Y-%m-%d')
            else:
                # Handle cases where conversion fails
                frontmatter['date'] = '1970-01-01'
        else:
            # Fallback if no date source is found
            frontmatter['date'] = '1970-01-01'

        # Generate content
        content = content_template.format(**row.to_dict()) if content_template else ""

        # Write file
        write_markdown_file(filepath, frontmatter, content)

    # Sync to blog if configured
    if "blog_sync_path" in config:
        sync_to_blog(output_dir, config["blog_sync_path"])

def write_markdown_file(filepath, frontmatter, content):
    """Writes a markdown file with frontmatter and content."""
    # Use yaml.dump for safe and clean frontmatter generation
    frontmatter_yaml = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    
    full_content = f"---\n{frontmatter_yaml}\n---\n\n{content}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)
