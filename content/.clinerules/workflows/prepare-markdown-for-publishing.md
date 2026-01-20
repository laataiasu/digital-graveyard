# Prepare Markdown for Publishing

<task name="Prepare Markdown for Publishing">
</task>

## Task Objective

Process markdown files to prepare them for publishing by analyzing content, suggesting appropriate filenames and tags, adding proper frontmatter with tags, and renaming files accordingly. The workflow scans the Tags directory to generate a list of available tags and suggests relevant tags based on content analysis.

**Inputs:** Markdown file path
**Output:** Improved markdown file with YAML frontmatter, tags added, renamed file
**Processing:** Analyze content → Suggest filename → Generate tags from Tags directory → Add frontmatter → Rename file → Save

## Detailed Sequence Steps

### Step 1: Read and Analyze Markdown Content

**Objective:** Extract key information from the markdown file to inform filename and tag suggestions.

**Process:**
1. Use the `read_file` command to read the specified markdown file
2. Analyze the content structure:
   - Extract the main title (first H1 heading if present, or infer from content)
   - Identify key headings (H2, H3) to understand content structure
   - Extract main topics, concepts, and themes from the body text
3. Determine the primary focus area and content type (e.g., project, personal, knowledge, write, read, watch)
4. Parse any existing frontmatter if present (YAML format between `---` markers)

**Expected Output:**
- Extracted title
- Key topics and themes identified
- Content focus area determined
- Existing tags (if any) noted

**Transition to Next Step:** Content analysis complete, ready for filename suggestion

### Step 2: Generate Filename Suggestion

**Objective:** Create a proper filename in kebab-case format based on the content analysis.

**Process:**
1. Take the extracted title or main topic
2. Convert to lowercase
3. Replace spaces and special characters with hyphens
4. Remove any special characters except hyphens
5. Check if the filename already exists in the current directory
6. If conflict detected, suggest alternatives by adding numbers or modifiers

**Naming Convention Examples:**
- "A Reflection on Standards" → "a-reflection-on-standards.md"
- "My Weekend Trip" → "my-weekend-trip.md"

**Expected Output:**
- Suggested filename in kebab-case format
- Confirmation of no conflicts OR alternative suggestions if conflicts exist

**Transition to Next Step:** Filename determined, ready to scan available tags

### Step 3: Scan Available Tags and Generate Suggestions

**Objective:** Retrieve all available tags from the Tags directory and suggest relevant ones based on content analysis.

**Process:**
1. Use the `list_files` command to scan the `Tags/` directory recursively
2. Extract all tag names from files and subdirectories
3. Create a comprehensive list of available tags
4. Analyze the content's topics and themes from Step 1
5. Match content themes with available tags to suggest relevant ones
6. Prioritize tags that:
   - Directly match content topics
   - Cover broader categories (e.g., "Computer Science" for programming content)
   - Include relevant sub-tags or related concepts

**Expected Output:**
- Complete list of all available tags (displayed in terminal)
- Suggested tags (3-5 tags recommended) based on content analysis
- Display of available tag categories for user reference

**Transition to Next Step:** Tag suggestions generated, ready to add to frontmatter

### Step 4: Create/Update Markdown Frontmatter

**Objective:** Add or update YAML frontmatter with tags and other metadata.

**Process:**
1. Check if the markdown file already has frontmatter (YAML block between `---` markers at the top)
2. If no frontmatter exists:
   - Create a YAML frontmatter section at the beginning of the file
   - Include standard fields: `---`, `title`, `date`, `tags`, `---`
3. If frontmatter exists:
   - Parse existing YAML content
   - Preserve existing fields
4. Add the suggested tags to the `tags` field
5. Include the determined filename or title in the frontmatter
6. Add the current date in YYYY-MM-DD format if not present

**Frontmatter Example:**
```yaml
---
title: "A Reflection on Standards"
date: 2026-01-20
tags: [standards, philosophy, reflection, personal]
---
```

**Expected Output:**
- Markdown content with proper YAML frontmatter
- Tags formatted as YAML array
- All necessary metadata included

**Transition to Next Step:** Frontmatter ready, file prepared for renaming

### Step 5: Rename the File

**Objective:** Rename the original markdown file to the suggested filename.

**Process:**
1. Use the `write_to_file` command to save the improved content to the new filename
2. Optionally delete or keep the original file (user's choice, but typically remove original)
3. Verify the file has been successfully renamed and saved
4. Confirm the new filename matches the kebab-case convention

**Expected Output:**
- File renamed to suggested filename
- Improved content saved to the new file
- Confirmation of successful rename

**Transition to Next Step:** File renamed, ready to finalize the workflow

### Step 6: Present Results and Confirm Completion

**Objective:** Display the results of the workflow and confirm successful completion.

**Process:**
1. Use the `attempt_completion` command to present the final results
2. Display the following information:
   - Original filename → New filename (renamed)
   - Tags added to frontmatter
   - File location of the improved markdown
3. Provide a summary of actions taken:
   - Content analysis results
   - Tag suggestions from available tags
   - Frontmatter structure
   - Rename confirmation

**Expected Output:**
- Clear confirmation of workflow completion
- Summary of all changes made
- File ready for publishing

**Expected Output Format:**
```
Workflow Complete: prepare-markdown-for-publishing

Input: [original filename]
Output: [new filename]

Changes Applied:
✓ Content analyzed and key topics identified
✓ Filename suggested: [kebab-case-filename.md]
✓ Tags added to frontmatter: [tag1, tag2, tag3]
✓ File renamed from [original] to [new filename]
✓ Frontmatter added with YAML format

The markdown file is now ready for publishing.

Available Tags Reference:
- [List of key tag categories and examples from Tags directory]
```

**End of Workflow:** Task completed successfully, markdown file prepared for publishing.

---

## Usage Example

**User Command:**
```
prepare markdown for publishing: "2026-01-20-my-observation.md"
```

**Cline's Actions:**
1. Read "2026-01-20-my-observation.md"
2. Analyze content, extract title and themes
3. Suggest new filename (e.g., "my-observation-on-digital-gardens.md")
4. Scan Tags directory for all available tags
5. Suggest relevant tags based on content
6. Add YAML frontmatter with tags
7. Rename file to suggested filename
8. Display results and confirmation

## Notes

- The workflow requires access to the `Tags/` directory to generate tag suggestions
- Files should be in markdown format (.md extension)
- Frontmatter follows YAML syntax with `---` delimiters
- Tags are stored as YAML array: `tags: [tag1, tag2, tag3]`
- Filenames should be in kebab-case (lowercase, hyphens instead of spaces)
- The workflow is designed for digital gardening and blogging workflows using markdown or Obsidian
