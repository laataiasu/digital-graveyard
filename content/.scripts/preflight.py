# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Preflight privacy gate for Digital Graveyard → Digital Garden sync.

Rules enforced (per AGENTS.md):
  1. A public note (publish_external: true) must NEVER link to a private note
     (publish_external: false) — private titles must not leak into the public graph.
  2. Public notes must not mention employer names / identifiable orgs:
     Krom Bank, Accenture, Telkomsel, Neural Technologies.
  3. Notes whose source journal was AI-drafted (journal has `promoted:` and the
     published note carries the AI footer) are checked for the mandatory
     [[On AI Assistance]] disclosure link.

Usage:
    uv run content/.scripts/preflight.py            # report
    uv run content/.scripts/preflight.py --strict   # exit 1 on any finding
"""
import argparse
import os
import re
import sys
from pathlib import Path

import frontmatter

SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_DIR = SCRIPT_DIR.parent

SKIP_DIRS = {".obsidian", ".scripts", ".vscode", "templates"}

WIKILINK_RE = re.compile(r"(?<!\!)\[\[([^\]|#\n]+)(?:#[^\]|\n]+)?(?:\|[^\]\n]+)?\]\]")
CODEBLOCK_RE = re.compile(r"(?ms)^```[^\n]*\n.*?\n```")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")

EMPLOYER_PATTERNS = [
    r"\bKrom\s+Bank\b",
    r"\bAccenture\b",
    r"\bTelkomsel\b",
    r"\bNeural\s+Technologies\b",
]

AI_FOOTPRINT_RE = re.compile(r"\[\[On AI Assistance\]\]")


def iter_md_files():
    for root, dirs, _ in os.walk(CONTENT_DIR):
        rel = Path(root).relative_to(CONTENT_DIR)
        if any(part in SKIP_DIRS for part in rel.parts):
            dirs[:] = []
            continue
        for f in sorted(os.listdir(root)):
            if f.endswith(".md"):
                yield Path(root) / f


def resolve_target(target: str, known: dict[str, str]) -> str | None:
    """Resolve a wikilink target to a content-relative path, or None."""
    t = target.strip().lower()
    stem = os.path.splitext(os.path.basename(t))[0]
    return known.get(t) or known.get(stem)


def build_index() -> tuple[dict[str, str], dict[str, bool]]:
    """Return (target -> relpath, relpath -> is_public). Keyed by lowercase stem/title."""
    target_map: dict[str, str] = {}
    visibility: dict[str, bool] = {}
    for path in iter_md_files():
        rel = path.relative_to(CONTENT_DIR).as_posix()
        try:
            post = frontmatter.load(path)
        except Exception:
            post = frontmatter.Post("", metadata={})
        visibility[rel] = post.get("publish_external", False) is True
        stem = os.path.splitext(path.stem)[0].lower()
        target_map.setdefault(stem, rel)
        title = str(post.get("title") or "").strip().lower()
        if title:
            target_map.setdefault(title, rel)
        aliases = post.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        for a in aliases or []:
            target_map.setdefault(str(a).strip().lower(), rel)
    return target_map, visibility


def clean_body(post) -> str:
    body = CODEBLOCK_RE.sub("", post.content)
    return INLINE_CODE_RE.sub("", body)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true", help="exit 1 on any finding")
    args = ap.parse_args()

    target_map, visibility = build_index()

    leak_links: list[str] = []
    employer_hits: list[str] = []
    missing_ai_disclosure: list[str] = []
    public_count = 0
    scanned = 0

    for path in iter_md_files():
        rel = path.relative_to(CONTENT_DIR).as_posix()
        try:
            post = frontmatter.load(path)
        except Exception as e:
            print(f"⚠️  Could not parse {rel}: {e}")
            continue
        scanned += 1
        if post.get("publish_external", False) is not True:
            continue
        public_count += 1

        # 1. Public -> private wikilinks
        for target in WIKILINK_RE.findall(clean_body(post)):
            resolved = resolve_target(target, target_map)
            if resolved and not visibility.get(resolved, False):
                leak_links.append(f"{rel} -> [[{target.strip()}]] ({resolved} is private)")

        # 2. Employer mentions
        text = clean_body(post)
        for pat in EMPLOYER_PATTERNS:
            m = re.search(pat, text, re.IGNORECASE)
            if m:
                employer_hits.append(f"{rel}: mentions '{m.group(0)}'")

        # 3. AI-drafted pieces must disclose
        promoted_from = str(post.get("promoted_from_journal") or post.get("ai_assisted") or "")
        if promoted_from.lower() in {"true", "1"} and not AI_FOOTPRINT_RE.search(text):
            missing_ai_disclosure.append(rel)

    print("\n========================================")
    print("  🛂 PREFLIGHT PRIVACY GATE")
    print("========================================")
    print(f"📄 Scanned: {scanned} notes ({public_count} public)")
    checks = [
        ("🔗 Public→private link leaks", leak_links),
        ("🏢 Employer mentions in public notes", employer_hits),
        ("🤖 Missing [[On AI Assistance]] disclosure", missing_ai_disclosure),
    ]
    failed = False
    for label, items in checks:
        icon = "✅" if not items else "❌"
        print(f"{icon} {label}: {len(items)}")
        for it in items[:20]:
            print(f"   • {it}")
        if len(items) > 20:
            print(f"   ... and {len(items) - 20} more")
        failed = failed or bool(items)

    print("========================================")
    if failed:
        print(f"🚫 PREFLIGHT FAILED — fix findings before syncing.")
        return 1 if args.strict else 0
    print("✅ Preflight clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
