import os

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Check if file has YAML frontmatter
    if len(lines) < 1 or lines[0].strip() != "---":
        return  # Skip files without frontmatter

    # Check if 'draft:' already present
    if any(line.strip().startswith("draft:") for line in lines):
        return

    # Insert 'draft: true' after the opening '---'
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":  # Closing frontmatter
            lines.insert(i, "draft: true\n")
            break
    else:
        # If no closing frontmatter found, insert at line 1
        lines.insert(1, "draft: true\n")

    # ✅ Write updated file (correctly indented and reopened in write mode)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"Updated: {file_path}")

def walk_directory(root="."):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".md"):
                process_markdown_file(os.path.join(dirpath, filename))

if __name__ == "__main__":
    walk_directory(".")
