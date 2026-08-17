# AGENTS.md

Instructions, architecture notes, and workflows for AI Coding Assistants (Antigravity / agy / Gemini) pair-programming in **Digital Graveyard**.

---

## 📌 Repository Overview

**Digital Graveyard** is a **Quartz v4** static site deployment and personal digital garden.

* **Private Second Brain Repo**: `digital-graveyard` (`laataiasu/digital-graveyard`) — Contains all notes, personal reflections, study materials, and drafts.
* **Public Garden Repo**: `digital-garden` (`nichsedge/digital-garden`) — Public website containing only notes with `publish_external: true`.

---

## 🛠️ Development & Validation Commands

```bash
# Build static site locally
npx quartz build

# Local development server with hot-reload (http://localhost:8080)
npx quartz build --serve

# Type checking & Prettier code style checks
npm run check

# Auto-format all code and notes
npm run format

# Run core Quartz test suite
npm test

# Update Quartz from upstream (@jackyzha0/quartz)
npx quartz update
```

---

## 📂 Content Structure & Folder Conventions

All source content lives in `/content/`:

```
content/
├── Write/             # Essays, articles, philology, journals
│   └── Journal/       # Journal entries structured as YYYY/MM/YYYY-MM-DD.md
├── Knowledge/         # Academic history, tech tips, concept notes
├── Read/              # Book reviews and summaries
├── Watch/             # Film/TV series notes & reviews
├── Projects/          # Project research and notes
├── Personal/          # Personal notes
├── Tags/              # Tag index notes
├── assets/            # Static image assets (Obsidian wikilink compatible)
└── .scripts/          # Maintenance and synchronization scripts
```

---

## 🏷️ Frontmatter & Privacy Guidelines

Every Markdown file in `content/` must follow this standard YAML frontmatter block:

```yaml
---
title: "Natural Title Case"
date: YYYY-MM-DD
tags: [tag1, tag2, tag3]
publish_external: true
---
```

### Privacy & Publishing Rules
* **`publish_external: true`**: Post is eligible for synchronization to the public `digital-garden` site.
* **`publish_external: false`**: Note stays private in `digital-graveyard` and is **excluded** from `digital-garden`.
* **Personal & Sensitive Essays**: Personal reflections, deeply private journals, family details, or workplace disclosures must have `publish_external: false` (or live in `content/Write/_draft/`).
* **Never purge history on `digital-graveyard`**: Git history purges (`git filter-repo`) apply strictly to the public `digital-garden` repository if requested, **never** to `digital-graveyard`.

---

## 🤖 Workflows & Automation Scripts

### 1. Ingesting Raw Writing
Use the process writing workflow in `.agent/workflows/process-writing.md`:
* Generates natural Title Case title.
* Extracts 3–5 lowercase tags.
* Formats images as `content/assets/Write/[Title]/[slug]-N.ext`.
* Uses Obsidian wikilinks for image references: `![[slug-N.ext]]`.
* Saves post flat in `content/Write/[Title].md`.

### 2. Standardizing Frontmatter
Run the automated repair script:
```bash
python3 content/.scripts/fix_frontmatter.py
```

### 3. Syncing Public Notes to Digital Garden
Run the sync script:
```bash
uv run content/.scripts/sync_content.py
```
This script cleans `/home/al/Projects/digital-garden/content` and copies only notes where `publish_external: true` is set, along with referenced assets.

---

## ⚠️ Important Rules for AI Assistants

1. **Do Not Modify Core Quartz Engines**: Avoid modifying code inside `quartz/` unless specifically requested. Perform customizations in `quartz.config.ts`, `quartz.layout.ts`, or plugins in `quartz/plugins/`.
2. **Preserve User Writing**: Never alter the tone or meaning of raw user writing during ingestion or frontmatter standardization.
3. **Verify Builds**: Always run `npx quartz build` after making modifications to ensure site generation passes with 0 errors.
