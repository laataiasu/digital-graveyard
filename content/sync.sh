#!/bin/bash
set -euo pipefail

PROJECT_DIR="/home/al/Projects/digital-graveyard/content"
SYNC_SCRIPT="$PROJECT_DIR/sync_content.py"
BLOG_DIR="/home/al/Projects/digital-garden"

uv run "$SYNC_SCRIPT"
cd "$BLOG_DIR"
npx quartz build --serve