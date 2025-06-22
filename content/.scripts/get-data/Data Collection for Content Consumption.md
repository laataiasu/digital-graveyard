# 📥 Data Collection for Content Consumption

Follow the steps below to gather your personal media consumption data from various platforms. Once downloaded and renamed as specified, copy the files into this directory.

---

## 📚 Goodreads (Books)

1. Visit: [Goodreads Import/Export](https://www.goodreads.com/review/import)
2. Download your data export (CSV file).
3. Rename the file to: `goodreads.csv`
4. Copy the file into this folder.

---

## 🎬 Letterboxd (Movies)

1. Visit: [Letterboxd Data Settings](https://letterboxd.com/settings/data/)
2. Download and extract the ZIP archive.
3. Locate the file named `ratings.csv`.
4. Copy `ratings.csv` into this folder.

---

## 📖 Manga & Anime (MyAnimeList)

1. Visit: [MyAnimeList Export](https://myanimelist.net/panel.php?go=export)
2. Download the export file.
3. Extract the contents.
4. Rename the files to:

   * `animelist.xml` (for anime)
   * `mangalist.xml` (for manga)
5. Copy both files into this folder.

---

## 🎭 Korean Drama (MyDramaList)

1. Use this formula in a Google Sheet:

   ```
   =IMPORTHTML("https://mydramalist.com/dramalist/Chanculus", "table", 1)
   ```

2. Wait for the table to load.

3. Export the sheet as CSV.

4. Rename the file to: `drama.csv`

5. Copy it into this folder.
