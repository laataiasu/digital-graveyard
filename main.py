import os
import shutil
import frontmatter

SOURCE_DIR = "content"
DEST_DIR = "/home/al/projects/ia_blog/content"

# Step 1: Clear the destination directory
if os.path.exists(DEST_DIR):
    shutil.rmtree(DEST_DIR)
os.makedirs(DEST_DIR, exist_ok=True)

# Step 2: Walk through source directory recursively
for root, _, files in os.walk(SOURCE_DIR):
    for file in files:
        if file.endswith(".md"):
            source_path = os.path.join(root, file)
            try:
                post = frontmatter.load(source_path)
            except:
                continue
            if post.get("publish_external") is True:
                # Maintain directory structure
                rel_path = os.path.relpath(source_path, SOURCE_DIR)
                dest_path = os.path.join(DEST_DIR, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(source_path, dest_path)