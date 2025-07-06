import os
import shutil
import frontmatter

SOURCE_DIR = "/home/al/projects/digital-graveyard/content"
DEST_DIR = "/home/al/projects/ia_blog/content"

def has_publish_external(path):
    try:
        post = frontmatter.load(path)
        return post.get('publish_external', False) is True
    except Exception as e:
        print(f"⚠️ Error reading frontmatter in {path}: {e}")
        return False

def clean_destination():
    if os.path.exists(DEST_DIR):
        print(f"🧹 Deleting existing DEST_DIR: {DEST_DIR}")
        shutil.rmtree(DEST_DIR)
    os.makedirs(DEST_DIR, exist_ok=True)

def is_asset_file(filename):
    # File extensions to exclude (common for content files)
    EXCLUDE_EXTENSIONS = {'.md', '.markdown'}
    _, ext = os.path.splitext(filename)
    return ext.lower() not in EXCLUDE_EXTENSIONS

def sync_assets(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if is_asset_file(file):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src_dir)
                dest_path = os.path.join(dest_dir, rel_path)

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} -> {dest_path}")

def sync_content():
    clean_destination()

    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue

            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, SOURCE_DIR)
            src_folder = os.path.dirname(filepath)
            rel_folder = os.path.relpath(src_folder, SOURCE_DIR)
            dst_folder = os.path.join(DEST_DIR, rel_folder)

            foldername = os.path.basename(src_folder)
            filename_wo_ext = os.path.splitext(file)[0]

            if has_publish_external(filepath):
                # Special case: top-level index.md — copy file only
                if rel_path == "index.md":
                    dst_file_path = os.path.join(DEST_DIR, "index.md")
                    os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
                    shutil.copy2(filepath, dst_file_path)
                    print(f"📄 Copied top-level index.md -> {dst_file_path}")
                elif file == "index.md" or filename_wo_ext == foldername:
                    try:
                        shutil.copytree(src_folder, dst_folder, dirs_exist_ok=True)
                        print(f"📁 Copied folder: {src_folder} -> {dst_folder}")
                    except Exception as e:
                        print(f"❌ Failed to copy folder: {src_folder} -> {dst_folder}\n   {e}")
                else:
                    dst_file_path = os.path.join(DEST_DIR, rel_path)
                    os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
                    shutil.copy2(filepath, dst_file_path)
                    print(f"📄 Copied file: {filepath} -> {dst_file_path}")

if __name__ == "__main__":
    sync_content()
    sync_assets(SOURCE_DIR, DEST_DIR)
