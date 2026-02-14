---
description: Smartly process user writing to generate title, tags, and save as a markdown file.
---

1.  **Ingest Content**:
    - If the user provides text directly, use that.
    - If the user provides a file path, read the file content.

2.  **Generate Metadata (Internal Thought Process)**:
    - **Title**: specific, descriptive, and engaging title based on the content.
    - **Tags**: Generate 3-5 relevant tags (lowercase).
    - **Slug**: Create a filename-safe slug from the title (e.g., `my-title.md`).
    - **Date**: Use the current date in YYYY-MM-DD format.

3.  **Create File**:
    - **Target Directory**: `/home/al/Projects/digital-graveyard/content/Write`
    - **Frontmatter**:
      ```markdown
      ---
      title: "[Title]"
      date: [YYYY-MM-DD]
      tags: [tag1, tag2, tag3]
      ---
      ```
    - **Action**: Use the `write_to_file` tool to save the new file with the generated filename in the target directory. The content should be the user's writing appended after the frontmatter.

4.  **Finalize**:
    - Notify the user of the new file location and the generated metadata (Title, Tags).
