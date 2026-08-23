#!/usr/bin/env python3
"""Mark near-empty Knowledge notes as `status: seedling` and write a triage report.

A "seed" is a Knowledge note with no real content yet (<= 10 lines total —
frontmatter plus at most a heading). These are mostly bulk-created course
skeletons and placeholder concept pages. Tagging them makes them machine-
identifiable for later triage (fill, merge, or delete) without touching
`publish_external` or any body text.

The report is written to content/.scripts/seed-triage.md.

Usage:
    python3 content/.scripts/tag_seeds.py            # apply + write report
    python3 content/.scripts/tag_seeds.py --dry-run  # preview only
"""

import os
import sys
from collections import Counter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
KNOWLEDGE_DIR = os.path.join(REPO_ROOT, "content", "Knowledge")
REPORT_PATH = os.path.join(SCRIPT_DIR, "seed-triage.md")

SEED_MAX_LINES = 10


def is_seed(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    if len(lines) > SEED_MAX_LINES:
        return False
    return "status: seedling" not in "".join(lines)


def add_status(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    if not lines or lines[0].strip() != "---":
        return False
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            lines.insert(i, "status: seedling\n")
            break
    else:
        return False
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return True


def main():
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    seeds = []
    for root, dirs, files in os.walk(KNOWLEDGE_DIR):
        for file in sorted(files):
            if not file.endswith(".md"):
                continue
            fp = os.path.join(root, file)
            if is_seed(fp):
                seeds.append(os.path.relpath(fp, REPO_ROOT))

    if not dry_run:
        for rel in seeds:
            add_status(os.path.join(REPO_ROOT, rel))

    by_area = Counter("/".join(s.split(os.sep)[1:3]) for s in seeds)
    report = []
    report.append("# Knowledge seed triage")
    report.append("")
    report.append(f"{len(seeds)} near-empty notes (<= {SEED_MAX_LINES} lines) in `content/Knowledge/` "
                  "are marked `status: seedling`. Triage options per note: fill it with real "
                  "content, merge it into an existing note, or delete it. Regenerate this "
                  "report with `python3 content/.scripts/tag_seeds.py`.")
    report.append("")
    report.append("## By area")
    report.append("")
    for area, count in by_area.most_common():
        report.append(f"- `{area}` — {count}")
    report.append("")
    report.append("## Full list")
    report.append("")
    for s in sorted(seeds):
        report.append(f"- [ ] `{s}`")

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n")

    label = "Would mark" if dry_run else "Marked"
    print(f"🌱 {label} {len(seeds)} Knowledge notes as `status: seedling`.")
    print("📊 Top areas:")
    for area, count in by_area.most_common(8):
        print(f"   {count:>4}  {area}")
    print(f"📝 Report: {os.path.relpath(REPORT_PATH, REPO_ROOT)}")


if __name__ == "__main__":
    main()