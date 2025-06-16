import os
import shutil
import frontmatter

SOURCE_DIR = "."
DEST_DIR = "/home/al/projects/ia_blog/content"

# Step 1: Clear the destination directory
if os.path.exists(DEST_DIR):
    shutil.rmtree(DEST_DIR)
os.makedirs(DEST_DIR, exist_ok=True)

# Step 2: Walk through source directory recursively
for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        if file.endswith(".md"):
            source_path = os.path.join(root, file)
            try:
                post = frontmatter.load(source_path)
            except Exception:
                continue

            if post.get("publish_external") is True:
                rel_dir = os.path.relpath(root, SOURCE_DIR)
                dest_dir_path = os.path.join(DEST_DIR, rel_dir)
                os.makedirs(dest_dir_path, exist_ok=True)

                if file == "index.md":
                    # Copy all files in the folder (excluding subdirectories)
                    for f in os.listdir(root):
                        src_file_path = os.path.join(root, f)
                        if os.path.isfile(src_file_path):  # Skip directories
                            dest_file_path = os.path.join(dest_dir_path, f)
                            shutil.copy2(src_file_path, dest_file_path)
                else:
                    dest_path = os.path.join(dest_dir_path, file)
                    shutil.copy2(source_path, dest_path)
