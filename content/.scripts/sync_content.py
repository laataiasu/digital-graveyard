# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Sync public notes (publish_external: true) from digital-graveyard to digital-garden.

Usage:
    uv run content/.scripts/sync_content.py            # sync
    uv run content/.scripts/sync_content.py --check    # dry-run: report only, no writes
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

import frontmatter

SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = SCRIPT_DIR.parent                      # .../digital-graveyard/content
DEST_DIR = SOURCE_DIR.parents[1] / "digital-garden" / "content"

SKIP_DIRS = {".obsidian", ".scripts", ".vscode", "templates"}
ASSET_EXTENSIONS = {".png", ".jpeg", ".jpg", ".html", ".svg", ".webp"}


def has_publish_external(path: Path) -> bool:
    try:
        post = frontmatter.load(path)
        return post.get("publish_external", False) is True
    except Exception as e:
        print(f"⚠️ Error reading frontmatter in {path}: {e}")
        return False


def iter_content_dirs():
    for root, dirs, _ in os.walk(SOURCE_DIR):
        rel = Path(root).relative_to(SOURCE_DIR)
        if any(part in SKIP_DIRS for part in rel.parts):
            dirs[:] = []
            continue
        yield Path(root), dirs


def clean_destination(dry_run: bool):
    if DEST_DIR.exists():
        if dry_run:
            print(f"🧹 [dry-run] Would delete: {DEST_DIR}")
        else:
            print(f"🧹 Deleting existing DEST_DIR: {DEST_DIR}")
            shutil.rmtree(DEST_DIR)
    if not dry_run:
        DEST_DIR.mkdir(parents=True, exist_ok=True)


def sync_notes(dry_run: bool) -> int:
    copied = 0
    for root, _ in iter_content_dirs():
        for file in sorted(os.listdir(root)):
            if not file.endswith(".md"):
                continue
            src = root / file
            rel = src.relative_to(SOURCE_DIR)
            if has_publish_external(src):
                copied += 1
                if dry_run:
                    print(f"📄 [dry-run] Would copy note: {rel}")
                else:
                    dst = DEST_DIR / rel
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                    print(f"📄 Copied note: {rel}")
    return copied


def sync_assets(dry_run: bool) -> int:
    copied = 0
    for root, _ in iter_content_dirs():
        for file in sorted(os.listdir(root)):
            src = root / file
            if not src.is_file() or src.suffix.lower() not in ASSET_EXTENSIONS:
                continue
            copied += 1
            if dry_run:
                continue
            dst = DEST_DIR / src.relative_to(SOURCE_DIR)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    if not dry_run:
        print(f"🖼️  Synced {copied} asset files.")
    return copied


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="dry-run: report what would change")
    ap.add_argument("--skip-preflight", action="store_true", help="bypass the privacy preflight gate")
    args = ap.parse_args()

    if not args.skip_preflight:
        print("🛂 Running privacy preflight gate...")
        r = subprocess.run(
            ["uv", "run", str(SCRIPT_DIR / "preflight.py"), "--strict"],
            cwd=str(SCRIPT_DIR.parent.parent),
        )
        if r.returncode != 0:
            print("🚫 Sync aborted: preflight found privacy issues. Fix them or use --skip-preflight.")
            sys.exit(1)

    clean_destination(args.check)
    notes = sync_notes(args.check)
    assets = sync_assets(args.check)
    if args.check:
        print(f"\n🔍 Dry-run: {notes} notes + {assets} assets would be synced.")
    else:
        print(f"\n✅ Successfully synced {notes} authorized public notes to digital-garden.")


if __name__ == "__main__":
    main()
