#!/usr/bin/env python3
"""Backfill placeholder dates (2001-01-01, 2016-01-01) with real creation dates from git history.

For each markdown file whose frontmatter carries a placeholder date, this script asks git
for the commit that first added the file (`git log --diff-filter=A`) and rewrites the
frontmatter date with it. Files with no git history are left untouched and reported.

Usage:
    python3 content/.scripts/backfill_dates.py            # apply
    python3 content/.scripts/backfill_dates.py --dry-run  # preview only
"""

import os
import re
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")

PLACEHOLDERS = {"2001-01-01", "2016-01-01"}
DATE_LINE_RE = re.compile(r"^(date:\s*)(?:\"|')?(2001-01-01|2016-01-01)(?:\"|')?\s*$")


def git_first_add_date(rel_path):
    """Return YYYY-MM-DD of the commit that first added rel_path, or None."""
    try:
        res = subprocess.run(
            ["git", "-c", "core.quotepath=false", "log", "--diff-filter=A", "--format=%as", "-1", "--", rel_path],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        out = res.stdout.strip()
        return out if out else None
    except Exception:
        return None


def backfill_file(filepath):
    """Try to replace a placeholder date in filepath's frontmatter. Returns old, new or None."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    # Locate frontmatter block (must start at line 0 with '---')
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None

    rel_path = os.path.relpath(filepath, REPO_ROOT)
    changed = False
    old_date = new_date = None
    for i in range(1, end):
        m = DATE_LINE_RE.match(lines[i])
        if m:
            old_date = m.group(2)
            real = git_first_add_date(rel_path)
            if real and real != old_date:
                lines[i] = f"date: {real}\n"
                new_date = real
                changed = True
            break

    if not changed:
        return None

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return old_date, new_date


def main():
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    if dry_run:
        print("🏃 DRY RUN — no files will be modified.\n")

    scanned = fixed = no_history = 0
    by_old = {}
    examples_no_history = []

    for root, dirs, files in os.walk(CONTENT_DIR):
        dirs[:] = [d for d in dirs if d not in {".obsidian", ".scripts", ".stfolder"}]
        for file in sorted(files):
            if not file.endswith(".md"):
                continue
            scanned += 1
            filepath = os.path.join(root, file)

            # Detect placeholder without touching anything yet
            has_placeholder = False
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    head = f.read(2048)
            except OSError:
                continue
            for ph in PLACEHOLDERS:
                if re.search(rf"^date:\s*[\"']?{ph}[\"']?\s*$", head, re.MULTILINE):
                    has_placeholder = True
                    break
            if not has_placeholder:
                continue

            rel_path = os.path.relpath(filepath, REPO_ROOT)
            if dry_run:
                real = git_first_add_date(rel_path)
                if real:
                    fixed += 1
                    by_old[ph_of(head)] = by_old.get(ph_of(head), 0) + 1
                    print(f"  would fix: {rel_path} -> {real}")
                else:
                    no_history += 1
                    if len(examples_no_history) < 10:
                        examples_no_history.append(rel_path)
                continue

            result = backfill_file(filepath)
            if result:
                old_d, new_d = result
                fixed += 1
                by_old[old_d] = by_old.get(old_d, 0) + 1
            else:
                # placeholder present but no git history found
                no_history += 1
                if len(examples_no_history) < 10:
                    examples_no_history.append(rel_path)

    print(f"\n📄 Scanned {scanned} markdown files.")
    print(f"🔧 {'Would fix' if dry_run else 'Fixed'} {fixed} placeholder dates: "
          + ", ".join(f"{k}→real ({v})" for k, v in sorted(by_old.items())))
    print(f"🚫 Skipped {no_history} files with placeholders but no git add-date available.")
    if examples_no_history:
        print("   Examples:")
        for p in examples_no_history:
            print(f"     - {p}")


def ph_of(head):
    for ph in PLACEHOLDERS:
        if re.search(rf"^date:\s*[\"']?{ph}[\"']?\s*$", head, re.MULTILINE):
            return ph
    return "?"


if __name__ == "__main__":
    main()