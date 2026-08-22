import os
import glob
from pathlib import Path

def find_markdown_files(directory):
    """Find all .markdown files in directory and subdirectories."""
    markdown_files = []
    
    # Use glob to find all .markdown files recursively
    pattern = os.path.join(directory, "**", "*.markdown")
    markdown_files.extend(glob.glob(pattern, recursive=True))
    
    # Also look for .md files (common markdown extension)
    pattern = os.path.join(directory, "**", "*.md")
    markdown_files.extend(glob.glob(pattern, recursive=True))
    
    # Sort files for consistent ordering
    markdown_files.sort()
    
    return markdown_files

def read_markdown_file(filepath):
    """Read markdown file content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""

def merge_markdown_to_text(directory, output_path):
    """Merge all markdown files into a single text file."""
    markdown_files = find_markdown_files(directory)
    
    if not markdown_files:
        print("No markdown files found in the directory.")
        return False
    
    print(f"Found {len(markdown_files)} markdown files:")
    for file in markdown_files:
        print(f"  - {file}")
    
    try:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for i, filepath in enumerate(markdown_files):
                # Add separator between files
                if i > 0:
                    output_file.write("\n\n" + "="*80 + "\n\n")
                
                # Add file header
                relative_path = os.path.relpath(filepath, directory)
                output_file.write(f"FILE: {relative_path}\n")
                output_file.write("="*len(f"FILE: {relative_path}") + "\n\n")
                
                # Add file content
                content = read_markdown_file(filepath)
                if content:
                    output_file.write(content)
                    output_file.write("\n\n")
        
        return True
    except Exception as e:
        print(f"Error writing to output file: {e}")
        return False

def main():
    """Main function to merge markdown files into a single text file."""
    # Get directory from user input or use current directory
    directory = input("Enter directory path (or press Enter for current directory): ").strip()
    if not directory:
        directory = "."
    
    # Validate directory
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return
    
    # Get output filename
    output_filename = input("Enter output text filename (default: merged_markdown.txt): ").strip()
    if not output_filename:
        output_filename = "merged_markdown.txt"
    
    if not output_filename.endswith('.txt'):
        output_filename += '.txt'
    
    print(f"\nSearching for markdown files in: {os.path.abspath(directory)}")
    
    # Merge markdown files to text
    success = merge_markdown_to_text(directory, output_filename)
    
    if success:
        print(f"\n✓ Successfully created {output_filename}")
        print(f"File size: {os.path.getsize(output_filename)} bytes")
    else:
        print("Failed to create merged file.")

if __name__ == "__main__":
    main()