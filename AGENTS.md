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

## 🏷️ Taxonomy & Semantic Architecture (Tags vs. Links vs. Folders)

To prevent *tag pollution* and maintain a rich, high-signal knowledge graph in Quartz and Obsidian, adhere strictly to the following 3-tier division of labor:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. FOLDERS  (Where it lives)      → Broad domain & privacy  │
│    (Knowledge/, Write/, Read/, Watch/, Projects/, Personal/)│
├─────────────────────────────────────────────────────────────┤
│ 2. TAGS     (What KIND of note)   → Format / Archetype      │
│    (journal, essay, guide, book, film, review, note, moc)   │
├─────────────────────────────────────────────────────────────┤
│ 3. LINKS    (What it is ABOUT)    → Concepts & Entities     │
│    ([[Linux]], [[Git]], [[Nietzsche]], [[Postgres]])        │
└─────────────────────────────────────────────────────────────┘
```

### 1. Tags (`tags: [...]`): Strictly for Formats & Archetypes
Tags are reserved exclusively for the structural **format** or **archetype** of a note. Notes should generally have **1–2 tags max** selected strictly from the approved taxonomy:

* **Media & Consumption**: `film`, `anime`, `drama`, `youtube`, `book`, `manga`, `sound`
* **Writing & Reflection**: `journal`, `essay`, `review`, `reflection`, `literature`, `travelogue`
* **Knowledge & Technical**: `guide`, `cheatsheet`, `note`, `interesting-terms`
* **Projects**: `project`, `case-study`
* **Entities / Index Stubs**: `figure`, `company`, `software`, `gadget`, `country`, `place`, `organization`, `school`, `religion`

### 2. Wikilinks (`[[Concept]]`): Exclusively for Concepts, Topics, & Entities
* **Never tag topics or entities** (e.g. do **NOT** use `tags: [linux, devops, productivity, philosophy, muslim]`).
* Instead, link them naturally in the note body: `...a guide to [[Linux]] systems and [[DevOps]] automation...`
* **Why**: Wikilinks generate two-way backlinks, show up on Quartz interactive graphs, provide hover popovers, and can evolve into full atomic notes or Maps of Content (MOCs).

---

## 🏷️ Frontmatter & Privacy Guidelines

Every Markdown file in `content/` must follow this standard YAML frontmatter block:

```yaml
---
title: "Natural Title Case"
date: YYYY-MM-DD
tags: [format-tag]
publish_external: true
---
```

### Privacy & Publishing Rules
* **`publish_external: true`**: Post is eligible for synchronization to the public `digital-garden` site.
* **`publish_external: false`**: Note stays private in `digital-graveyard` and is **excluded** from `digital-garden`.
* **Personal & Sensitive Essays**: Personal reflections, deeply private journals, family details, or workplace disclosures must have `publish_external: false` (or live in `content/Write/_draft/`).
* **Asymmetric Linking for Private Content**: Notes with `publish_external: false` (journals, private notes, personal links) must **never** be linked outward from hub/MOC notes (e.g. `Travel.md`) or public pages. Instead, add the hub wikilink (e.g. `[[Travel]]`) **inside the private note itself**. This preserves local graph backlinks in Obsidian without leaking private note titles or creating broken links on the public garden.
* **Never purge history on `digital-graveyard`**: Git history purges (`git filter-repo`) apply strictly to the public `digital-garden` repository if requested, **never** to `digital-graveyard`.

---

## 🤖 Workflows & Automation Scripts

### 1. Ingesting Raw Writing
Use the process writing workflow in `.agent/workflows/process-writing.md`:
* Generates natural Title Case title.
* Assigns 1–2 approved format tags (e.g. [essay], [review]) and links concepts as wikilinks ([[Topic]]) in body.
* Formats images as `content/assets/Write/[Title]/[slug]-N.ext`.
* Uses Obsidian wikilinks for image references: `![[slug-N.ext]]`.
* Saves post flat in `content/Write/[Title].md`.

### 5. Journal Promotion Workflow (journal → reflection/essay)
Promoting a journal entry into a public note follows this exact loop:
1. **Check first**: skip any journal whose frontmatter already has `promoted: "<Note Title>"` — it has been published already. Never promote twice.
2. **Write a NEW file** in `content/Write/<Title>.md` (never edit the journal body). Frontmatter: real title, original journal date, `tags: [reflection]` or `[essay]`, `publish_external: true` only after safety review.
3. **Rewrite, don't copy**: strip diary framing, employer names (Krom Bank/Accenture/Telkomsel/Neural Technologies → genericize), identifiable people, and religiously provocative lines. Preserve the author's ideas and voice.
4. **AI-assistance footer** (mandatory when AI drafted the piece), at the end of the body:
   ```
   ---

   *Drafted with AI assistance from my personal journal (<YYYY-MM-DD>), then edited by me. See [[On AI Assistance]].*
   ```
   The [[On AI Assistance]] note is the public disclosure page — keep it linked.
5. **Stamp the source journal**: add `promoted: "<Published Note Title>"` to the journal's frontmatter so future reviews know it's already published.
6. Journals themselves always stay `publish_external: false`.

### 6. Standardizing Frontmatter
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

### 4. Media Notes (Books/Films/Anime/Manga/Dramas) — ierp-owned
Media consumption notes under `content/Read/` and `content/Watch/` plus `content/Write/Links.md` are **generated, not hand-written**. The source of truth is the ierp SQLite database (`~/Projects/ierp/ierp/events.db`).

* **Fetch + ingest** (all logic lives in ierp):
```bash
cd ~/Projects/ierp && uv run ierp sync [--source goodreads]
```
* **Regenerate garden notes from the DB**:
```bash
python3 ~/Projects/ierp/scripts/export_garden.py   # add --check for dry-run
```
* **Never hand-edit or hand-create media notes** — they are overwritten on export. To fix data, fix it in ierp (DB or `ierp` CLI) and re-export.
* The old `content/.scripts/get-data/` pipeline was removed; do not recreate it.
* **Do not edit ierp-generated files in place** — including `content/Read/`, `content/Watch/`, and `content/Write/Links.md`. They are regenerated views; any content fix (titles, tags, links, tables) must be made in the ierp source of truth (`~/Projects/ierp`) and re-exported via `python3 ~/Projects/ierp/scripts/export_garden.py`.
  * Exception: mechanical frontmatter hygiene (quoting titles, tag taxonomy) is safe on these files, since `fix_frontmatter.py` will re-apply it after every export — but never change *content* (body text, wikilinks, tables) in them.

---

## 🔑 Git Identity (IMPORTANT)

This repo commits as the **laataiasu** account — NOT the global default (nichsedge).

* Required identity: `laataiasu <ichsanamal19@gmail.com>` (already set in this repo's local `.git/config`).
* Global git config intentionally stays `Amal <muhammad.ichsanul19@gmail.com>` (nichsedge) for other repos. **Never change global git config to commit here.**
* Before committing, verify: `git config user.email` must print `ichsanamal19@gmail.com`. If it shows `muhammad.ichsanul19@gmail.com` (e.g. after a fresh clone), run `git_laataiasu` (zsh function in `~/.zshrc`) before committing.
* Never push commits authored as nichsedge from this repo.

---

## ⚠️ Important Rules for AI Assistants

1. **Do Not Modify Core Quartz Engines**: Avoid modifying code inside `quartz/` unless specifically requested. Perform customizations in `quartz.config.ts`, `quartz.layout.ts`, or plugins in `quartz/plugins/`.
2. **Preserve User Writing**: Never alter the tone or meaning of raw user writing during ingestion or frontmatter standardization.
3. **Verify Builds**: Always run `npx quartz build` after making modifications to ensure site generation passes with 0 errors.
