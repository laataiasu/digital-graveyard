import os

def rename_brackets_in_markdown(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md") and ("[" in filename or "]" in filename):
                old_path = os.path.join(dirpath, filename)
                new_filename = filename.replace("[", "(").replace("]", ")")
                new_path = os.path.join(dirpath, new_filename)
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')

# Replace with your target directory
rename_brackets_in_markdown(".")
