#!/usr/bin/env python3
"""Fill hollow hub notes with curated sections built from their real backlinks.

For each hub note that is still an empty stub (frontmatter + heading only), this script:
  1. Finds every note in content/ whose body links to the hub ([[HubName]], [[HubName|alias]], [[HubName#anchor]]).
  2. Keeps ONLY sources with `publish_external: true` (privacy: private notes are never linked from public pages).
  3. Groups them by format tag into curated sections and rewrites the hub body.

Hubs that already contain real writing (more than just the heading) are never touched.

Usage:
    python3 content/.scripts/build_hubs.py            # fill all configured hubs
    python3 content/.scripts/build_hubs.py --dry-run  # preview what would be written
"""

import os
import re
import sys
import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")

# Top hub notes by inbound link count (measured across the vault).
HUBS = [
    "content/Knowledge/Concepts/Finance/Decentralized Finance.md",
    "content/Knowledge/Concepts/Systems & Tech/Data.md",
    "content/Knowledge/Entities/Country/China.md",
    "content/Knowledge/Concepts/Philosophy/Allah.md",
    "content/Knowledge/Concepts/Philosophy/Woman.md",
    "content/Knowledge/Entities/Religion/Islam.md",
    "content/Knowledge/Entities/Social Media/Twitter.md",
    "content/Knowledge/Concepts/Systems & Tech/Music.md",
    "content/Knowledge/Entities/Social Media/Facebook.md",
    "content/Knowledge/Concepts/Finance/Quant.md",
    "content/Knowledge/Entities/School/Universitas Indonesia.md",
    "content/Knowledge/Places/Semarang.md",
    "content/Knowledge/Concepts/Finance/Gambling.md",
    "content/Knowledge/Concepts/Finance/Investment.md",
    "content/Knowledge/Concepts/Psychology/Anxiety.md",
    "content/Knowledge/Entities/Social Media/Tiktok.md",
    "content/Knowledge/Concepts/Psychology/Suicide.md",
    "content/Knowledge/Entities/Country/Japan.md",
    "content/Knowledge/Concepts/Systems & Tech/Meme.md",
    "content/Knowledge/Entities/Figure/Friedrich Nietzsche.md",
    "content/Knowledge/Entities/Software/ChatGPT.md",
]

SECTION_ORDER = [
    ("Essays & reflections", {"essay", "review", "reflection", "literature", "travelogue"}),
    ("Books & manga", {"book", "manga"}),
    ("Films & series", {"film", "anime", "drama", "youtube"}),
    ("Knowledge notes", {"note", "guide", "cheatsheet", "interesting-terms", "figure",
                         "company", "software", "gadget", "country", "organization",
                         "school", "religion"}),
    ("Projects", {"project", "case-study"}),
    ("Sounds", {"sound"}),
]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        data = yaml.safe_load(parts[1])
        return (data if isinstance(data, dict) else {}), parts[2]
    except Exception:
        return {}, parts[2]


def is_stub(body):
    """A stub is a body with only the H1 heading and whitespace."""
    stripped = re.sub(r"^#\s+.*$", "", body.strip(), count=1)
    return stripped.strip() == ""


def scan_sources():
    """Return list of (relpath, title, tags, publish_external, body)."""
    sources = []
    for root, dirs, files in os.walk(CONTENT_DIR):
        dirs[:] = [d for d in dirs if d not in {".obsidian", ".scripts", ".stfolder", "templates"}]
        for file in sorted(files):
            if not file.endswith(".md"):
                continue
            fp = os.path.join(root, file)
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            fm, body = parse_frontmatter(text)
            title = str(fm.get("title") or os.path.splitext(file)[0])
            tags = fm.get("tags") or []
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",") if t.strip()]
            pub = fm.get("publish_external") is True
            sources.append((os.path.relpath(fp, REPO_ROOT), title, set(tags), pub, body))
    return sources


def build_hub_body(hub_relpath, sources):
    hub_path = os.path.join(REPO_ROOT, hub_relpath)
    stem = os.path.splitext(os.path.basename(hub_path))[0]
    pattern = re.compile(r"\[\[" + re.escape(stem) + r"(\]\]|\||#)", re.IGNORECASE)

    sections = {name: [] for name, _ in SECTION_ORDER}
    total = 0
    for relpath, title, tags, pub, body in sources:
        if not pub or relpath == hub_relpath:
            continue
        if not pattern.search(body):
            continue
        total += 1
        placed = False
        for sec_name, sec_tags in SECTION_ORDER:
            if tags & sec_tags:
                sections[sec_name].append((title, relpath))
                placed = True
                break
        if not placed:
            sections["Knowledge notes"].append((title, relpath))

    lines = [f"# {stem}", ""]
    lines.append(f"{total} public notes in this garden link here. "
                 "This page is a curated map of those threads.")
    for sec_name, _ in SECTION_ORDER:
        items = sorted(set(sections[sec_name]), key=lambda x: x[0].lower())
        if not items:
            continue
        lines += ["", f"## {sec_name}", ""]
        for title, _ in items:
            lines.append(f"- [[{title}]]")
    lines += ["", "---", "", "*Auto-curated from inbound links by "
              "`content/.scripts/build_hubs.py`. Edit freely — rerunning the script "
              "will not overwrite manual changes.*", ""]
    return "\n".join(lines)


def main():
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    sources = scan_sources()
    filled = skipped_content = missing = 0

    for hub_rel in HUBS:
        hub_path = os.path.join(REPO_ROOT, hub_rel)
        if not os.path.exists(hub_path):
            print(f"⚠️  missing hub (check path): {hub_rel}")
            missing += 1
            continue
        with open(hub_path, "r", encoding="utf-8") as f:
            text = f.read()
        fm, body = parse_frontmatter(text)
        if not is_stub(body):
            skipped_content += 1
            print(f"⏭️  has content, skipping: {hub_rel}")
            continue

        new_body = build_hub_body(hub_rel, sources)
        fm_text = text.split("---", 2)[1]
        new_text = f"---{fm_text}---\n{new_body}"
        if dry_run:
            n_links = new_body.count("- [[")
            print(f"  would fill: {hub_rel} ({n_links} curated links)")
        else:
            with open(hub_path, "w", encoding="utf-8") as f:
                f.write(new_text)
            print(f"✅ filled: {hub_rel} ({new_body.count('- [[')} curated links)")
        filled += 1

    print(f"\n📄 {filled} hubs {'would be' if dry_run else ''} filled, "
          f"{skipped_content} skipped (already have content), {missing} missing.")


if __name__ == "__main__":
    main()