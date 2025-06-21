import os
import re
import shutil
import pandas as pd

def sanitize_filename(name, max_length=100):
    if pd.isna(name) or not name:
        return "untitled"
    name = re.sub(r'[\\/*?:"<>|]', "", str(name))
    name = re.sub(r'\s+', '_', name)
    return name[:max_length]

def recreate_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder, exist_ok=True)

def move_to_blog_path(local_folder, blog_subfolder):
    blog_path = os.environ.get('BLOG_PATH')
    if blog_path:
        dest_path = os.path.join(blog_path, blog_subfolder)
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.move(local_folder, dest_path)
        return True
    else:
        print("Environment variable BLOG_PATH is not set.")
        return False

def write_markdown(filepath, frontmatter, content=""):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        if content:
            f.write("\n" + content)