---
description: Audit, tidy, and validate vault content hygiene, taxonomy, journal placement, entity links, and Quartz build status.
---

# Vault Hygiene & Neat Content Workflow

Use this workflow whenever the user asks to "neat content", "tidy vault", or after ingesting new notes/guides.

---

## Steps

1. **Check Misplaced Notes & Enforce Journal Structure**:
   - Check if any root-level markdown files exist directly in `content/` or dated notes exist outside `content/Write/Journal/YYYY/MM/`.
   - Relocate dated daily journals to `content/Write/Journal/YYYY/MM/YYYY-MM-DD.md`.
   - Normalize frontmatter dates to strict `YYYY-MM-DD` (strip ISO timestamps and timezone offsets).
   - Ensure journals maintain `tags: [journal]` and `publish_external: false`.

2. **Taxonomy & Tag Enforcement**:
   - Check frontmatter `tags`: strictly 1–2 format/archetype tags from `AGENTS.md` (e.g. `[guide]`, `[essay]`, `[note]`, `[review]`, `[journal]`, `[reflection]`).
   - Remove topical or entity tags (e.g. `linux`, `crypto`, `productivity`, `wayland`).
   - Retain concepts and topics as Obsidian wikilinks (`[[Topic]]`) in the note body.

3. **Audit Vault Health**:
   - Run the health checker:
     ```bash
     python3 content/.scripts/check_vault.py --verbose
     ```
   - Resolve any reported frontmatter errors, invalid dates, unapproved tags, or broken links.

4. **Seed Missing Entity Stubs**:
   - For broken internal wikilinks pointing to software, companies, or figures, create seedling entity notes in `content/Knowledge/Entities/Software/` or `content/Knowledge/Entities/Company/`:
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

5. **Build & Test Verification**:
   - Run `npx quartz build` to confirm 0 build errors.
   - Run `npm test` to ensure core Quartz tests pass.

6. **Git Identity Check**:
   - Verify `git config user.email` prints `ichsanamal19@gmail.com` (`laataiasu`) before committing.
