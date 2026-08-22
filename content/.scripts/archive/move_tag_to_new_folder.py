import os
import shutil
import re
import frontmatter

SOURCE_DIR = "Write"
DEST_SUBDIR = "Philology"
DEST_DIR = os.path.join(SOURCE_DIR, DEST_SUBDIR)

def ensure_dest():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

def extract_asset_paths(markdown_content):
    # Match ![alt](file) and [text](file)
    pattern = r'!\[[^\]]*\]\(([^)]+)\)|\[[^\]]+\]\(([^)]+)\)'
    matches = re.findall(pattern, markdown_content)
    return [m[0] if m[0] else m[1] for m in matches]

def move_asset_and_update_link(md_dir, rel_path):
    asset_abs = os.path.normpath(os.path.join(md_dir, rel_path))
    if not os.path.exists(asset_abs):
        print(f"  ⚠ Asset not found: {asset_abs}")
        return rel_path  # Leave unchanged

    filename = os.path.basename(asset_abs)
    new_path = os.path.join(DEST_DIR, filename)

    if os.path.abspath(asset_abs) != os.path.abspath(new_path):
        if not os.path.exists(new_path):
            shutil.move(asset_abs, new_path)
            print(f"  ✅ Moved asset: {rel_path} → {DEST_SUBDIR}/{filename}")
        else:
            print(f"  ⚠ Skipped (already exists): {filename}")
    return filename  # Relative filename only

def process_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)

    if "literature" not in post.get("tags", []):
        return

    print(f"\n📄 Processing: {file_path}")
    md_dir = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    new_md_path = os.path.join(DEST_DIR, filename)

    asset_paths = extract_asset_paths(post.content)
    updated_content = post.content

    for asset_path in asset_paths:
        new_asset_name = move_asset_and_update_link(md_dir, asset_path)
        # Replace all instances of the original asset path with just the filename
        updated_content = updated_content.replace(asset_path, new_asset_name)

    post.content = updated_content

    with open(new_md_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    os.remove(file_path)
    print(f"  ✅ Moved markdown to: {new_md_path}")

def main():
    ensure_dest()
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                if DEST_SUBDIR in os.path.relpath(full_path, SOURCE_DIR):
                    continue  # Skip files already in philology/
                process_markdown(full_path)

if __name__ == "__main__":
    main()
