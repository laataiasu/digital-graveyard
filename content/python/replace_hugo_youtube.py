import os
import re

def replace_youtube_embeds(directory):
    # Matches YouTube shortcode with optional extra parameters
    pattern = re.compile(r'\{\{<\s*youtube\s+id=[“"]([^”"]+)[”"][^>]*>}}')

    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(subdir, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace all matching patterns
                new_content = pattern.sub(r'![[https://youtu.be/\1]]', content)

                if content != new_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {filepath}")

# Use current directory or specify a path
replace_youtube_embeds(".")
