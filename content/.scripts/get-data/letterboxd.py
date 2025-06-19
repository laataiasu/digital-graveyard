import pandas as pd
import os
import shutil

# Load data
df = pd.read_csv('ratings.csv', parse_dates=['Date'])

# Create a fresh 'Letterboxd' folder
if os.path.exists('Letterboxd'):
    shutil.rmtree('Letterboxd')
os.makedirs('Letterboxd', exist_ok=True)

# Generate markdown files
for idx, row in df.iterrows():
    # Sanitize filename
    filename = f"{row['Name'].replace('/', '_').replace(':', '-')}.md"
    filepath = os.path.join('Letterboxd', filename)

    # Prepare frontmatter
    frontmatter = (
        f"---\n"
        f"title: \"{row['Name']}\"\n"
        f"date: {row['Date'].date()}\n"
        f"year: {row['Year']}\n"
        f"letterboxd_uri: {row['Letterboxd URI']}\n"
        f"rating: {row['Rating']}\n"
        f"---\n"
    )

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)

# Move to BLOG_PATH if set
blog_path = os.environ.get('BLOG_PATH')
if blog_path:
    dest_path = os.path.join(blog_path, 'Watch', 'Letterboxd')

    # Remove existing destination if it exists
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.move('Letterboxd', dest_path)
else:
    print("Environment variable BLOG_PATH is not set.")
