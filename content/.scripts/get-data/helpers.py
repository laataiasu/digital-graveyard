import os
import re
import shutil
import pandas as pd

# Default content root: /home/al/Projects/digital-graveyard/content
DEFAULT_CONTENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def sanitize_filename(text):
    """Sanitizes text for safe markdown filenames while preserving readability."""
    if not text:
        return "Untitled"
    # Replace invalid filename characters with spaces
    no_punc = re.sub(r'[^\w\s\-]', ' ', str(text))
    clean_name = ' '.join(no_punc.split())
    return clean_name.strip() or "Untitled"


def create_output_dir(output_dir):
    """Creates a fresh local output directory."""
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)


def sync_to_blog(output_dir, dest_path_segment):
    """
    Syncs the generated markdown files to the target content directory.
    Uses BLOG_PATH env var if set, otherwise defaults to the repository content folder.
    """
    base_path = os.environ.get('BLOG_PATH', DEFAULT_CONTENT_PATH)
    dest_path = os.path.join(base_path, dest_path_segment)
    
    os.makedirs(dest_path, exist_ok=True)
    
    # Copy/move files to destination
    copied_count = 0
    for item in os.listdir(output_dir):
        src_file = os.path.join(output_dir, item)
        dst_file = os.path.join(dest_path, item)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)
            copied_count += 1
            
    # Clean up temp output dir
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        
    print(f"Synced {copied_count} notes to {dest_path}")


def clean_isbn(val):
    """Cleans ISBN values."""
    if pd.isna(val):
        return ""
    return str(val).replace('="', '').replace('"', '').strip()


def sanitize_text(text):
    """Sanitizes text fields, ensuring they are strings and stripped of whitespace."""
    if pd.isna(text) or text is None:
        return ""
    return str(text).strip()
