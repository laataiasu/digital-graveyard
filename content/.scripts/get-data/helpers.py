import re
import os
import shutil
import pandas as pd

def sanitize_filename(text):
    no_punc = re.sub(r'[^\w\s]', ' ', text)
    remove_extra_space = ' '.join(no_punc.split())
    return remove_extra_space

def create_output_dir(output_dir):
    """Creates a fresh output directory, removing the old one if it exists."""
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

def sync_to_blog(output_dir, dest_path_segment):
    """Syncs the output directory to the blog path if the environment variable is set."""
    blog_path = os.environ.get('BLOG_PATH')
    if blog_path:
        dest_path = os.path.join(blog_path, dest_path_segment)
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.move(output_dir, dest_path)
        print(f"Synced {output_dir} to {dest_path}")
    else:
        print("Skipping blog sync: BLOG_PATH environment variable is not set.")

def clean_isbn(val):
    """Cleans ISBN values from Goodreads CSV."""
    if pd.isna(val):
        return ""
    return str(val).replace('="', '').replace('"', '').strip()

def sanitize_text(text):
    """Sanitizes text fields, ensuring they are strings and stripped of whitespace."""
    if pd.isna(text):
        return ""
    return str(text).strip()
