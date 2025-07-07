import xml.etree.ElementTree as ET
import pandas as pd
import os
import shutil
from utils import sanitize_filename
import yaml

def to_df(xml_file, pattern):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data_list = []
    for item in root.findall(pattern):
        dct = {}
        for element in item:
            dct[element.tag] = element.text
        data_list.append(dct)
    return pd.DataFrame(data_list)

animelist = to_df(xml_file='animelist.xml', pattern='anime')
mangalist = to_df(xml_file='mangalist.xml', pattern='manga')

def write_markdown(folder, title, date, frontmatter_dict, content=""):
    if pd.isna(title) or not title:
        return

    filename = sanitize_filename(title) + ".md"
    filepath = os.path.join(folder, filename)

    # Ensure date is included in frontmatter if provided
    if date and "date" not in frontmatter_dict:
        frontmatter_dict["date"] = str(date)

    # Use yaml.dump to handle various value types safely
    frontmatter_yaml = yaml.dump(frontmatter_dict, sort_keys=False, allow_unicode=True).strip()
    frontmatter = f"---\n{frontmatter_yaml}\n---\n\n{content}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)

# Idempotent folder creation: always delete and recreate
for folder, df, title_col in [
    ("Anime", animelist, 'series_title'),
    ("Manga", mangalist, 'manga_title')
]:
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder, exist_ok=True)
    for _, row in df.iterrows():
        title = row.get(title_col, '').replace('"', '')
        date = '2016-01-01'
        frontmatter_dict = {col: row[col] for col in df.columns if col != title_col}
        frontmatter_dict['title'] = title
        frontmatter_dict['date'] = date

        if folder == 'Anime':
            tag = ["anime", "film"]
        elif folder == 'Manga':
            tag = ["manga", "book"]
        frontmatter_dict['tags'] = tag
        write_markdown(folder, title, date, frontmatter_dict)

# Move to BLOG_PATH if set, idempotently
blog_path = os.environ.get('BLOG_PATH')
if blog_path:
    for src_folder, subfolder in [("Anime", os.path.join('Watch', 'Anime')), ("Manga", os.path.join('Read', 'Manga'))]:
        dest_path = os.path.join(blog_path, subfolder)
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.move(src_folder, dest_path)
else:
    print("Environment variable BLOG_PATH is not set.")
