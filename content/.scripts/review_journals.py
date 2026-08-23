#!/usr/bin/env python3
"""List unpromoted journals as a monthly review queue for the promotion workflow.

A journal is "promoted" when its frontmatter carries `promoted: "<Note Title>"`.
This script lists journals without that field, oldest first, with word counts —
pick one or two each month and run the Journal Promotion Workflow from AGENTS.md.

Usage:
    python3 content/.scripts/review_journals.py             # list all unpromoted
    python3 content/.scripts/review_journals.py --limit 10  # show only 10
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
JOURNAL_DIR = os.path.join(CONTENT_DIR, "Write", "Journal")

PROMOTED_RE = re.compile(r"^promoted:", re.MULTILINE)
DATE_RE = re.compile(r"(\d{4})/(\d{2})/(\d{4}-\d{2}-\d{2})")


def main():
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    entries = []
    total = 0
    for root, _, files in os.walk(JOURNAL_DIR):
        for file in sorted(files):
            if not file.endswith(".md"):
                continue
            total += 1
            fp = os.path.join(root, file)
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            if PROMOTED_RE.search(text):
                continue
            rel = os.path.relpath(fp, CONTENT_DIR)
            m = DATE_RE.search(rel.replace(os.sep, "/"))
            date = m.group(3) if m else "?"
            words = len(text.split())
            entries.append((date, words, rel))

    entries.sort()
    print(f"📓 {total} journals total, {len(entries)} not yet promoted.")
    print("")
    print(f"{'date':<12} {'words':>6}  path")
    print("-" * 72)
    shown = entries[:limit] if limit else entries
    for date, words, rel in shown:
        print(f"{date:<12} {words:>6}  {rel}")
    if limit and len(entries) > limit:
        print(f"… and {len(entries) - limit} more (drop --limit to see all).")
    print("")
    print("Next step: pick an entry and follow the Journal Promotion Workflow")
    print("in AGENTS.md (write a NEW note in content/Write/, then stamp the")
    print('journal frontmatter with `promoted: "<Title>"`).')


if __name__ == "__main__":
    main()