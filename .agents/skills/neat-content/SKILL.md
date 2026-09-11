---
name: neat-content
description: >-
  Audit, tidy, and validate vault content hygiene, taxonomy, journal placement, entity links, and Quartz build status.
  Use when the user asks to "neat content", "tidy vault", or after ingesting new notes and guides.
---

# Vault Hygiene & Neat Content Workflow

A comprehensive runbook for keeping the Digital Graveyard vault clean, structurally compliant, and free of broken links or build issues.

---

## Procedure

### 1. Check Misplaced Notes & Enforce Journal Structure
* Audit root-level markdown files in `content/`. Any dated journal notes must live in `content/Write/Journal/YYYY/MM/YYYY-MM-DD.md`.
* Ensure date frontmatter conforms to `YYYY-MM-DD` (strip ISO datetime strings like `2026-09-01T22:22:47+07:00`).
* Ensure journals retain `tags: [journal]` and `publish_external: false`.

### 2. Enforce Tag Taxonomy vs. Wikilinks
* Only 1–2 format/archetype tags allowed per note (`guide`, `cheatsheet`, `note`, `essay`, `review`, `reflection`, `journal`, `travelogue`, `figure`, `company`, `software`, etc.).
* Strip topic/concept tags (e.g. `linux`, `hyprland`, `wayland`, `productivity`).
* Ensure topics/entities are embedded as wikilinks (`[[Linux]]`, `[[Wayland]]`) in the markdown prose instead.

### 3. Run Vault Health Audit
Execute:
```bash
python3 content/.scripts/check_vault.py --verbose
```
Repair any reported issues:
* Missing frontmatter fields (`title`, `date`, `publish_external`).
* Unapproved or excessive tags.
* Broken internal wikilinks.

### 4. Seed Missing Entity Stubs
When notes introduce new wikilinks to entities (Software, Companies, Figures), create corresponding seedling files to maintain a rich, unbroken graph:
* **Software**: `content/Knowledge/Entities/Software/<Name>.md`
* **Company**: `content/Knowledge/Entities/Company/<Name>.md`
* **Figure**: `content/Knowledge/Entities/Figure/<Name>.md`

Seedling template:
```yaml
---
title: "<Entity Name>"
date: YYYY-MM-DD
tags: [software] # or [company], [figure]
publish_external: true
status: seedling
---

# <Entity Name>
```

### 5. Build & Test Verification
Verify zero build or parser errors:
```bash
npx quartz build
npm test
```

### 6. Git Identity Verification
Always ensure the local repository identity is set to `laataiasu` before committing:
```bash
git config user.email # must output ichsanamal19@gmail.com
```
