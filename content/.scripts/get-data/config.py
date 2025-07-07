
from dataloaders import (
    load_goodreads_data,
    load_letterboxd_data,
    load_mal_data,
    load_mydramalist_data,
)

DATA_SOURCES = {
    "goodreads": {
        "loader": load_goodreads_data,
        "loader_args": {"file_path": "goodreads.csv"},
        "output_dir": "Goodreads",
        "blog_sync_path": "Read/Goodreads",
        "title_column": "Title",
        "date_column": "Date Added",
        "tags": ["book"],
        "frontmatter_mapping": {
            "title": "Title",
            "author": "Author",
            "date": "Date Added",
            "author_lf": "Author l-f",
            "additional_authors": "Additional Authors",
            "isbn": "ISBN",
            "isbn13": "ISBN13",
            "publisher": "Publisher",
            "binding": "Binding",
            "pages": "Number of Pages",
            "year_published": "Year Published",
            "original_publication_year": "Original Publication Year",
            "date_read": "Date Read",
            "date_added": "Date Added",
            "my_rating": "My Rating",
            "average_rating": "Average Rating",
            "bookshelves": "Bookshelves",
            "exclusive_shelf": "Exclusive Shelf",
            "read_count": "Read Count",
            "owned_copies": "Owned Copies",
        },
        "content_template": """
# {Title}

**Author:** {Author}  
**My Rating:** {My Rating}  
**Date Read:** {Date Read}  
**Bookshelves:** {Bookshelves}

## Review

{My Review}
""",
    },
    "letterboxd": {
        "loader": load_letterboxd_data,
        "loader_args": {"file_path": "ratings.csv"},
        "output_dir": "Letterboxd",
        "blog_sync_path": "Watch/Letterboxd",
        "title_column": "Name",
        "date_column": "Date",
        "tags": ["film"],
        "frontmatter_mapping": {
            "title": "Name",
            "date": "Date",
            "year": "Year",
            "letterboxd_uri": "Letterboxd URI",
            "rating": "Rating",
        },
    },
    "mal_anime": {
        "loader": lambda: load_mal_data("animelist.xml", "mangalist.xml")["Anime"],
        "output_dir": "Anime",
        "blog_sync_path": "Watch/Anime",
        "title_column": "series_title",
        "default_date": "2016-01-01",
        "tags": ["anime", "film"],
        "frontmatter_mapping": "all",
    },
    "mal_manga": {
        "loader": lambda: load_mal_data("animelist.xml", "mangalist.xml")["Manga"],
        "output_dir": "Manga",
        "blog_sync_path": "Read/Manga",
        "title_column": "manga_title",
        "default_date": "2016-01-01",
        "tags": ["manga", "book"],
        "frontmatter_mapping": "all",
    },
    "mydramalist": {
        "loader": load_mydramalist_data,
        "loader_args": {"file_path": "drama.csv"},
        "output_dir": "Drama",
        "blog_sync_path": "Watch/Drama",
        "title_column": "Title",
        "default_date": "2016-01-01",
        "tags": ["film", "drama"],
        "frontmatter_mapping": {
            "title": "Title",
            "country": "Country",
            "year": "Year",
            "type": "Type",
            "score": "Score",
            "progress": "Progress",
        },
        "content_template": """
# {Title}

- **Country:** {Country}
- **Year:** {Year}
- **Type:** {Type}
- **Score:** {Score}
- **Progress:** {Progress}
""",
    },
}
