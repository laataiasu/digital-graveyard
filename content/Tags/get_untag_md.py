import os
import shutil

def has_tags(file_path):
    """
    Return True if the file contains a line that starts with 'tag:' or 'tags:' (case‑insensitive).
    Adjust this if your tag syntax is different (e.g. YAML front‑matter).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip().lower()
            if stripped.startswith("tags:") or stripped.startswith("tag:"):
                return True
    return False

def move_md_without_tags_to_untags(base_dir):
    target_dir = os.path.join(base_dir, "untags")
    os.makedirs(target_dir, exist_ok=True)

    for root, _, files in os.walk(base_dir):
        for filename in files:
            if not filename.lower().endswith(".md"):
                continue

            file_path = os.path.join(root, filename)

            # Skip anything already inside the 'untags' folder
            if os.path.commonpath([file_path, target_dir]) == target_dir:
                continue

            if not has_tags(file_path):
                # If a file with the same name already exists in 'untags', append a counter
                dest_path = os.path.join(target_dir, filename)
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(target_dir, f"{base}_{counter}{ext}")
                        counter += 1

                shutil.move(file_path, dest_path)
                print(f"Moved: {file_path}  ->  {dest_path}")

if __name__ == "__main__":
    move_md_without_tags_to_untags(os.getcwd())
