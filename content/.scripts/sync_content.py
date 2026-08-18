# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
import os
import shutil
import frontmatter

# Platform-specific directory paths
if os.name == 'nt':  # Windows
    SOURCE_DIR = "C:\\Users\\al\\Projects\\digital-graveyard\\content"
    DEST_DIR = "C:\\Users\\al\\Projects\\digital-garden\\content"
else:  # Linux/macOS
    SOURCE_DIR = "/home/al/Projects/digital-graveyard/content"
    DEST_DIR = "/home/al/Projects/digital-garden/content"

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
    INCLUDE_EXTENSIONS = {'.png', '.jpeg', '.jpg', '.html', '.svg', '.webp'}
    _, ext = os.path.splitext(filename)
    return ext.lower() in INCLUDE_EXTENSIONS

def sync_assets(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        # Skip hidden/internal directories
        rel_root = os.path.relpath(root, src_dir)
        if any(p in rel_root.split(os.sep) for p in [".obsidian", ".scripts"]):
            continue
        for file in files:
            if is_asset_file(file):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src_dir)
                dest_path = os.path.join(dest_dir, rel_path)

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(src_path, dest_path)

def sync_content():
    clean_destination()

    copied_count = 0
    for root, _, files in os.walk(SOURCE_DIR):
        rel_root = os.path.relpath(root, SOURCE_DIR)
        if any(p in rel_root.split(os.sep) for p in [".obsidian", "templates", ".scripts"]):
            continue

        for file in files:
            if not file.endswith(".md"):
                continue

            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, SOURCE_DIR)

            if has_publish_external(filepath):
                dst_file_path = os.path.join(DEST_DIR, rel_path)
                os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
                shutil.copy2(filepath, dst_file_path)
                copied_count += 1
                print(f"📄 Copied note: {rel_path}")

    print(f"\n✅ Successfully synced {copied_count} authorized public notes to digital-garden.")

if __name__ == "__main__":
    sync_content()
    sync_assets(SOURCE_DIR, DEST_DIR)
