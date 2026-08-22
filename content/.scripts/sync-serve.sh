#!/bin/bash
# Sync public notes to digital-garden, then serve Quartz with live reload.
set -euo pipefail

PROJECT_DIR="/home/al/Projects/digital-graveyard/content"
BLOG_DIR="/home/al/Projects/digital-garden"

uv run "$PROJECT_DIR/.scripts/sync_content.py"
cd "$BLOG_DIR"
npx quartz build --serve
