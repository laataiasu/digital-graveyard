# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Orphan & stub report for Digital Graveyard.

Surfaces a concrete linking/promotion backlog:
  - Orphans: notes with zero inbound wikilinks (nobody links to them).
  - Stubs: public notes with fewer than STUB_WORDS words in the body.
  - Lonely publics: publishable notes that no other PUBLIC note links to
    (invisible on the public garden graph even if linked privately).

Usage:
    uv run content/.scripts/report_orphans.py             # summary counts
    uv run content/.scripts/report_orphans.py --verbose   # full listings
"""
import argparse
import os
import re
from collections import defaultdict
from pathlib import Path

import frontmatter

SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_DIR = SCRIPT_DIR.parent
SKIP_DIRS = {".obsidian", ".scripts", ".vscode", "templates"}

WIKILINK_RE = re.compile(r"(?<!\!)\[\[([^\]|#\n]+)(?:#[^\]|\n]+)?(?:\|[^\]\n]+)?\]\]"
CODEBLOCK_RE = re.compile(r"(?ms)^```[^\n]*\n.*?\n```")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")

STUB_WORDS = 100


def iter_md_files():
    for root, dirs, _ in os.walk(CONTENT_DIR):
        rel = Path(root).relative_to(CONTENT_DIR)
        if any(part in SKIP_DIRS for part in rel.parts):
            dirs[:] = []
            continue
        for f in sorted(os.listdir(root)):
            if f.endswith(".md"):
                yield Path(root) / f


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-v", "--verbose", action="store_true")
    ap.add_argument("--stub-words", type=int, default=STUB_WORDS)
    args = ap.parse_args()

    # index: stem/title/alias -> relpath
    target_map: dict[str, str] = {}
    posts: dict[str, frontmatter.Post] = {}
    for path in iter_md_files():
        rel = path.relative_to(CONTENT_DIR).as_posix()
        try:
            post = frontmatter.load(path)
        except Exception:
            continue
        posts[rel] = post
        target_map.setdefault(os.path.splitext(path.stem)[0].lower(), rel)
        t = str(post.get("title") or "").strip().lower()
        if t:
            target_map.setdefault(t, rel)
        aliases = post.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        for a in aliases or []:
            target_map.setdefault(str(a).strip().lower(), rel)

    inbound: dict[str, set] = defaultdict(set)
    public_inbound: dict[str, set] = defaultdict(set)

    def resolve(target: str) -> str | None:
        t = target.strip().lower()
        return target_map.get(t) or target_map.get(os.path.splitext(os.path.basename(t))[0])

    for rel, post in posts.items():
        is_public = post.get("publish_external", False) is True
        body = INLINE_CODE_RE.sub("", CODEBLOCK_RE.sub("", post.content))
        seen = set()
        for target in WIKILINK_RE.findall(body):
            r = resolve(target)
            if r and r not in seen:
                seen.add(r)
                inbound[r].add(rel)
                if is_public:
                    public_inbound[r].add(rel)

    orphans = sorted(r for r in posts if not inbound[r])
    lonely_publics = sorted(
        r for r, p in posts.items()
        if p.get("publish_external", False) is True and not public_inbound[r]
    )
    stubs = []
    for r, p in sorted(posts.items()):
        if p.get("publish_external", False) is not True:
            continue
        words = len(p.content.split())
        if words < args.stub_words:
            stubs.append((r, words))

    print("\n========================================")
    print("  🗺️  ORPHAN & STUB REPORT")
    print("========================================")
    print(f"📄 Notes scanned: {len(posts)}")
    print(f"🏝️  Orphans (0 inbound links anywhere): {len(orphans)}")
    print(f"👻 Public notes invisible on the public graph: {len(lonely_publics)}")
    print(f"🩹 Public stubs (< {args.stub_words} words): {len(stubs)}")

    if args.verbose:
        def show(title, items):
            print(f"\n--- {title} ({len(items)}) ---")
            for it in items:
                print(f"  • {it}")
        show("Orphans", orphans)
        show("Publicly invisible", lonely_publics)
        show("Stubs", [f"{r} ({w} words)" for r, w in stubs])
    print("========================================")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
