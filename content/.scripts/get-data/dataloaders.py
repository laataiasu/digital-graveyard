import pandas as pd
import xml.etree.ElementTree as ET
from helpers import clean_isbn, sanitize_text

def load_goodreads_data(file_path):
    """Loads and cleans Goodreads data from a CSV file."""
    df = pd.read_csv(file_path, dtype=str)
    df.columns = [col.strip() for col in df.columns]
    df['ISBN'] = df['ISBN'].apply(clean_isbn)
    df['ISBN13'] = df['ISBN13'].apply(clean_isbn)
    # Convert date column and handle potential errors
    df['Date Added'] = pd.to_datetime(df['Date Added'], errors='coerce')
    for col in df.columns:
        if col != 'Date Added':
            df[col] = df[col].apply(sanitize_text)
    return df

def load_letterboxd_data(file_path):
    """Loads Letterboxd data from a CSV file."""
    return pd.read_csv(file_path, parse_dates=['Date'])

def load_mal_data(anime_path, manga_path):
    """Loads MyAnimeList data from XML files into a dictionary of DataFrames."""
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

    return {
        'Anime': to_df(xml_file=anime_path, pattern='anime'),
        'Manga': to_df(xml_file=manga_path, pattern='manga')
    }

def load_mydramalist_data(file_path):
    """Loads MyDramaList data from a CSV file."""
    df = pd.read_csv(file_path, quoting=1, engine='python')
    df[['Title', 'Type']] = df['Title'].str.split('\n', expand=True)
    return df

