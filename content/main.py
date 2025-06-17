import os
import shutil
import frontmatter

SOURCE_DIR = "."
DEST_DIR = "/home/al/projects/ia_blog/content"


def should_publish(folder):
    """Check if any .md file in the folder has publish_external: true"""
    for file in os.listdir(folder):
        if file.endswith(".md"):
            try:
                post = frontmatter.load(os.path.join(folder, file))
                if post.get("publish_external") is True:
                    return True
            except Exception:
                continue
    return False


def copy_folder_contents(src_dir, dest_dir):
    """Copy all files from src_dir (excluding subfolders) to dest_dir"""
    os.makedirs(dest_dir, exist_ok=True)
    for item in os.listdir(src_dir):
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)
        if os.path.isfile(src_item):
            shutil.copy2(src_item, dest_item)


def is_folder_main_file(filename, folder_name):
    """Check if file is 'index.md' or matches folder name (e.g. about/about.md)"""
    base, _ = os.path.splitext(filename)
    return filename == "index.md" or base == folder_name


def main():
    if os.path.exists(DEST_DIR):
        shutil.rmtree(DEST_DIR)
    os.makedirs(DEST_DIR, exist_ok=True)

    for root, dirs, files in os.walk(SOURCE_DIR):
        if not any(f.endswith(".md") for f in files):
            continue

        rel_dir = os.path.relpath(root, SOURCE_DIR)
        folder_name = os.path.basename(root)
        dest_path = os.path.join(DEST_DIR, rel_dir)

        for file in files:
            if not file.endswith(".md"):
                continue

            src_file = os.path.join(root, file)
            try:
                post = frontmatter.load(src_file)
            except Exception:
                continue

            if post.get("publish_external") is True:
                if is_folder_main_file(file, folder_name):
                    copy_folder_contents(root, dest_path)
                else:
                    os.makedirs(dest_path, exist_ok=True)
                    shutil.copy2(src_file, os.path.join(dest_path, file))

                break  # Only one publish_external needed per folder


if __name__ == "__main__":
    main()