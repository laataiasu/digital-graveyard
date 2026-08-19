---
description: Smartly process user writing to generate title, tags, and save as a markdown file.
---

## Project Conventions

Before doing anything, understand the file/image structure used in this project:

- **Markdown files** live flat in `content/Write/[Post Title].md`  
  Example: `content/Write/Midsommar The Heaven for Everyone.md`
- **Images** live in `content/assets/Write/[Post Title]/[original-filename.ext]`  
  Example: `content/assets/Write/Midsommar The Heaven for Everyone/Entrance-Midsommar-8f48fc0.jpg`
- **Image references** inside markdown use **Obsidian wikilink syntax** with the filename only (no path):  
  `![[filename.jpg]]`  
  Quartz resolves the image automatically from `content/assets/`.

---

## Steps

1. **Ingest Content**
   - If the user provides a file path, read the file content.
   - If the user provides text directly, use that.
   - Keep track of the original file path if one was provided.

2. **Generate Metadata**
   - **Title**: A specific, descriptive, and engaging title based on the content. Use the post's own heading if present, or craft one from the content. Do NOT use slug-style titles — use natural title case (e.g. `Why I Vibecoded My Own Time Tracker`, not `why-i-vibecoded-my-own-time-tracker`).
   - **Tags**: Assign 1–2 approved format tags from the taxonomy (e.g. `[essay]`, `[review]`, `[journal]`, `[reflection]`, `[guide]`). Do NOT use topic or concept tags.
   - **Concept Links**: Ingest concepts/entities as Obsidian wikilinks (`[[Topic]]`, `[[Linux]]`, `[[Android]]`) directly within the text content.
   - **Date**: Use the date exist in filename/title or use current date in `YYYY-MM-DD` format.

3. **Process Images**
   - Scan the content for referenced images in either format:
     - Obsidian wikilink: `![[image.png]]`
     - Standard markdown: `![alt](path)`
   - Derive a **slug** from the title: lowercase, spaces replaced with hyphens, special characters removed.  
     Example: `Why I Vibecoded My Own Time Tracker` → `why-i-vibecoded-my-own-time-tracker`
   - For **each image found**, numbered sequentially (1, 2, 3…):
     - **New filename**: `[slug]-N.ext` (e.g. `why-i-vibecoded-my-own-time-tracker-1.png`)
     - **Target asset directory**: `content/assets/Write/[Title]/`
     - Move and rename the actual image file to `content/assets/Write/[Title]/[slug]-N.ext`.
     - Update the image reference in the markdown to Obsidian wikilink format using the **new filename only**:  
       `![[slug-N.ext]]`
   - If no images are found, skip this step.

4. **Create Markdown File**
   - **Target path**: `content/Write/[Title].md` (flat, no subdirectory)
   - **Frontmatter format** (follow this exactly):
     ```markdown
     ---
     title: "Post Title Here"
     date: YYYY-MM-DD
     tags: [essay]  # Use approved format tag(s)
     publish_external: true
     ---
     ```
   - **Content**: Append the user's writing (with updated image wikilinks) after the frontmatter.
   - Use the `write_to_file` tool to save the file.

5. **Cleanup Source**
   - If content was ingested from a file path (Step 1), delete the original source file using `run_command`.

6. **Finalize**
   - Notify the user of:
     - New file location: `content/Write/[Title].md`
     - Image(s) moved to: `content/assets/Write/[Title]/`
     - Generated metadata: Title, Tags