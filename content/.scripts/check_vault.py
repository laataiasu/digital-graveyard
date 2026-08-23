#!/usr/bin/env python3
"""
check_vault.py — Digital Graveyard Vault Health & Hygiene Checker

Audits the entire Quartz/Obsidian vault for:
1. Frontmatter completeness (title, date, publish_external).
2. Tag taxonomy compliance (strictly format/archetype tags per AGENTS.md).
3. Broken internal wikilinks ([[Note]] and ![[asset.png]]).
4. Mislocated files (e.g. journals outside content/Write/Journal/).
5. Empty / 0-byte files.

Usage:
    python3 content/.scripts/check_vault.py
    python3 content/.scripts/check_vault.py --verbose
"""

import os
import re
import sys
import yaml
import argparse

from collections import defaultdict

CONTENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VAULT_ROOT = os.path.dirname(CONTENT_DIR)

# Approved format/archetype tags per AGENTS.md taxonomy
APPROVED_TAGS = {
    # Media & Consumption
    "film", "anime", "drama", "youtube", "book", "manga", "sound",
    # Writing & Reflection
    "journal", "essay", "review", "reflection", "literature", "travelogue",
    # Knowledge & Technical
    "guide", "cheatsheet", "note", "interesting-terms",
    # Projects
    "project", "case-study",
    # Entities / Indexes
    "figure", "company", "software", "gadget", "country", "place", "organization", "school", "religion"
}

IGNORED_DIRS = {".obsidian", "templates", ".scripts", ".git"}
DATE_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK_REGEX = re.compile(r"(!)?\[\[([^\]|#\n]+)(?:#[^\]|\n]+)?(?:\|[^\]\n]+)?\]\]")

class VaultChecker:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.files = []
        self.titles = set()
        self.aliases = set()
        self.assets = set()
        
        # Tracking maps for collision detection
        self.stem_to_files = defaultdict(list)
        self.title_to_files = defaultdict(list)
        
        self.issues = {
            "empty_files": [],
            "missing_frontmatter": [],
            "invalid_date": [],
            "invalid_tags": [],
            "excessive_tags": [],
            "missing_publish_flag": [],
            "mislocated_files": [],
            "duplicate_titles": [],
            "duplicate_filenames": [],
            "broken_note_links": [],
            "broken_asset_links": [],
        }

    def scan_vault(self):
        for root, dirs, filenames in os.walk(CONTENT_DIR):
            dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
            rel_dir = os.path.relpath(root, CONTENT_DIR)
            
            for f in filenames:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, CONTENT_DIR)
                
                # Check 0-byte (ignore .gitkeep)
                if os.path.getsize(full_path) == 0:
                    if f != ".gitkeep":
                        self.issues["empty_files"].append(rel_path)
                    continue

                if f.endswith(".md"):
                    self.files.append((full_path, rel_path))
                    # Record filename stem as resolvable target
                    stem = os.path.splitext(f)[0]
                    stem_lower = stem.lower()
                    self.titles.add(stem_lower)
                    self.stem_to_files[stem_lower].append(rel_path)
                else:
                    self.assets.add(f.lower())

    def parse_frontmatter_and_aliases(self):
        for full_path, rel_path in self.files:
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()
            except Exception:
                continue

            if not content.startswith("---"):
                continue

            parts = content.split("---", 2)
            if len(parts) < 3:
                continue

            try:
                fm = yaml.safe_load(parts[1])
                if isinstance(fm, dict):
                    title = fm.get("title")
                    if title:
                        title_clean = str(title).strip().lower()
                        self.titles.add(title_clean)
                        self.title_to_files[title_clean].append(rel_path)
                    aliases = fm.get("aliases", [])
                    if isinstance(aliases, str):
                        aliases = [aliases]
                    if isinstance(aliases, list):
                        for a in aliases:
                            if a:
                                self.aliases.add(str(a).strip().lower())
            except Exception:
                pass

    def is_cross_media_collision(self, paths):
        # Cross-media tracker notes under Watch/ and Read/ are generated from ierp
        return all(p.startswith("Watch/") or p.startswith("Read/") for p in paths)

    def check_duplicates(self):
        # 1. Check duplicate filename stems (excluding index.md and cross-media trackers)
        for stem, paths in self.stem_to_files.items():
            if stem == "index" or self.is_cross_media_collision(paths):
                continue
            if len(paths) > 1:
                joined = " | ".join(paths)
                self.issues["duplicate_filenames"].append(f"Slug collision '{stem}' ({len(paths)} files): {joined}")

        # 2. Check duplicate frontmatter titles (excluding cross-media trackers)
        for title, paths in self.title_to_files.items():
            if self.is_cross_media_collision(paths):
                continue
            if len(paths) > 1:
                joined = " | ".join(paths)
                self.issues["duplicate_titles"].append(f"Title collision '{title}' ({len(paths)} files): {joined}")

    def check_file(self, full_path, rel_path):
        with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()

        # Check mislocated root notes
        parts = rel_path.split(os.sep)
        if len(parts) == 1 and parts[0] not in {"index.md", "404.md"}:
            self.issues["mislocated_files"].append(f"{rel_path} (Markdown file located directly in content/ root)")

        # Check mislocated journals (e.g. 2024-04-28*.md outside Journal/ folder)
        if re.match(r"^\d{4}-\d{2}-\d{2}", parts[-1]) and "Journal" not in parts:
            self.issues["mislocated_files"].append(f"{rel_path} (Dated note found outside Write/Journal/)")

        if not content.startswith("---"):
            self.issues["missing_frontmatter"].append(f"{rel_path} (Missing frontmatter header)")
            return

        fm_parts = content.split("---", 2)
        if len(fm_parts) < 3:
            self.issues["missing_frontmatter"].append(f"{rel_path} (Malformed frontmatter delimiter)")
            return

        raw_fm = fm_parts[1]
        body = fm_parts[2]

        try:
            fm = yaml.safe_load(raw_fm)
            if not isinstance(fm, dict):
                self.issues["missing_frontmatter"].append(f"{rel_path} (Frontmatter is not a mapping)")
                return
        except Exception as e:
            self.issues["missing_frontmatter"].append(f"{rel_path} (YAML parsing error: {e})")
            return

        # 1. Date Check
        date_val = str(fm.get("date", "")).strip()
        if not DATE_REGEX.match(date_val) or date_val.startswith("0000"):
            self.issues["invalid_date"].append(f"{rel_path} (Date: '{date_val}')")

        # 2. Publish External Check
        if "publish_external" not in fm or not isinstance(fm.get("publish_external"), bool):
            self.issues["missing_publish_flag"].append(f"{rel_path} (Missing or non-boolean publish_external)")

        # 3. Tags Check
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]
        elif not isinstance(tags, list):
            tags = []

        if len(tags) > 2:
            self.issues["excessive_tags"].append(f"{rel_path} ({len(tags)} tags: {tags})")

        unapproved = [t for t in tags if str(t).lower() not in APPROVED_TAGS]
        if unapproved:
            self.issues["invalid_tags"].append(f"{rel_path} (Unapproved tags: {unapproved})")

        # 4. Wikilinks Check (ignore codeblocks)
        clean_body = re.sub(r"(?ms)^```[^\n]*\n.*?\n```", "", body)
        clean_body = re.sub(r"`[^`\n]+`", "", clean_body)

        for is_asset, target in WIKILINK_REGEX.findall(clean_body):
            target = target.strip()
            if not target or target.startswith("http://") or target.startswith("https://"):
                continue
            
            target_norm = target.lower()
            if is_asset:
                asset_name = os.path.basename(target_norm)
                if asset_name not in self.assets:
                    self.issues["broken_asset_links"].append(f"{rel_path} -> ![[{target}]]")
            else:
                target_stem = os.path.splitext(os.path.basename(target_norm))[0]
                if target_norm not in self.titles and target_stem not in self.titles and target_norm not in self.aliases:
                    self.issues["broken_note_links"].append(f"{rel_path} -> [[{target}]]")

    def run(self):
        self.scan_vault()
        self.parse_frontmatter_and_aliases()
        self.check_duplicates()
        
        for full_path, rel_path in self.files:
            self.check_file(full_path, rel_path)

        total_issues = sum(len(v) for v in self.issues.values())

        print("\n========================================================")
        print("         🌱 DIGITAL GRAVEYARD VAULT AUDIT               ")
        print("========================================================")
        print(f"📊 Total Markdown Notes Scanned: {len(self.files)}")
        print(f"🖼️  Total Media Assets Tracked:   {len(self.assets)}")
        print("--------------------------------------------------------")

        headers = [
            ("empty_files", "🗑️  Empty / 0-byte Files"),
            ("missing_frontmatter", "⚠️  Missing / Broken Frontmatter"),
            ("invalid_date", "📅 Invalid Date Format"),
            ("missing_publish_flag", "🔒 Missing publish_external Flag"),
            ("invalid_tags", "🏷️  Unapproved Taxonomy Tags"),
            ("excessive_tags", "🏷️  Excessive Tags (> 2 tags)"),
            ("mislocated_files", "📂 Mislocated Files"),
            ("duplicate_titles", "👯 Duplicate Note Titles"),
            ("duplicate_filenames", "👯 Duplicate Filename Slugs"),
            ("broken_note_links", "🔗 Broken Note Wikilinks"),
            ("broken_asset_links", "🖼️  Broken Asset Embeds"),
        ]

        for key, label in headers:
            items = self.issues[key]
            count = len(items)
            icon = "✅" if count == 0 else "❌"
            print(f"{icon} {label}: {count}")
            if self.verbose and count > 0:
                for it in items[:15]:
                    print(f"   • {it}")
                if count > 15:
                    print(f"   ... and {count - 15} more.")

        print("--------------------------------------------------------")
        if total_issues == 0:
            print("🎉 VAULT HEALTH: 100% CLEAN! All notes conform to AGENTS.md.")
            print("========================================================\n")
            return 0
        else:
            print(f"⚠️  TOTAL ISSUES DETECTED: {total_issues}")
            print("💡 Run `python3 content/.scripts/fix_frontmatter.py` to auto-repair metadata.")
            print("========================================================\n")
            return 1

def main():
    parser = argparse.ArgumentParser(description="Audit Digital Graveyard vault hygiene.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print detailed issue list")
    args = parser.parse_args()

    checker = VaultChecker(verbose=args.verbose)
    exit_code = checker.run()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
