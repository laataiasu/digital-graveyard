import os

def strip_extension(filename):
    return os.path.splitext(filename)[0]

def create_markdown_for_files():
    folder_path = os.getcwd()
    folder_name = os.path.basename(folder_path)

    # Files to exclude: .md and .py
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(f) and not f.endswith(('.md', '.py'))
    ]

    created_md_basenames = []

    for file in files:
        base_name = strip_extension(file)
        md_filename = f"{base_name}.md"
        with open(md_filename, 'w') as md_file:
            md_file.write(f"# {base_name}\n\n")
        created_md_basenames.append(base_name)

    # Write index file using Obsidian-style links
    index_filename = f"{folder_name}.md"
    with open(index_filename, 'w') as index_file:
        index_file.write(f"# {folder_name}\n\n")
        index_file.write("## Files\n\n")
        for name in created_md_basenames:
            index_file.write(f"- [[{name}]]\n")

    print(f"Created {len(created_md_basenames)} .md files (excluding .md and .py).")
    print(f"Main index: {index_filename}")

if __name__ == "__main__":
    create_markdown_for_files()
