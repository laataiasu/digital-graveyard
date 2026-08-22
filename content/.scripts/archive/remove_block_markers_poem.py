import os
import re

def process_markdown(content):
    # Extract frontmatter if it exists
    frontmatter_match = re.match(r'(?s)^---\n.*?\n---\n', content)
    frontmatter = frontmatter_match.group(0) if frontmatter_match else ''
    body = content[len(frontmatter):] if frontmatter else content

    # Remove all code block markers like ``` or ```text, ```python, etc.
    body = re.sub(r'^```.*\n?', '', body, flags=re.MULTILINE)

    # Replace all newlines with markdown hard line breaks (2 spaces + newline)
    body = body.replace('\n', '  \n')

    return frontmatter + body

# Process all .md files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.md'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = process_markdown(content)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Processing complete.")
