import os
import shutil
import pandas as pd

# Read and split title/type
df = pd.read_csv("drama.csv", quoting=1, engine='python')
df[['Title', 'Type']] = df['Title'].str.split('\n', expand=True)

# Recreate Drama folder (ensures idempotency)
output_dir = "Drama"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

# Select only needed columns
cols = ['Title', 'Country', 'Year', 'Type', 'Score', 'Progress']
df_selected = df[cols]

# Write markdown files
for _, row in df_selected.iterrows():
    # Sanitize filename
    filename = "".join([c if c.isalnum() or c in " ._-" else "_" for c in row['Title']]).strip()
    filepath = os.path.join(output_dir, f"{filename}.md")
    
    # Frontmatter and content
    frontmatter = (
        "---\n"
        f"title: \"{row['Title']}\"\n"
        f"country: \"{row['Country']}\"\n"
        f"year: {row['Year']}\n"
        f"type: \"{row['Type']}\"\n"
        f"score: {row['Score']}\n"
        f"progress: \"{row['Progress']}\"\n"
        "---\n"
    )

    content = f"# {row['Title']}\n\n"
    content += f"- **Country:** {row['Country']}\n"
    content += f"- **Year:** {row['Year']}\n"
    content += f"- **Type:** {row['Type']}\n"
    content += f"- **Score:** {row['Score']}\n"
    content += f"- **Progress:** {row['Progress']}\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + "\n" + content)

# Sync to BLOG_PATH
blog_path = os.environ.get('BLOG_PATH')
if blog_path:
    dest_path = os.path.join(blog_path, 'Watch', 'Drama')
    
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.move(output_dir, dest_path)
else:
    print("Environment variable BLOG_PATH is not set.")
