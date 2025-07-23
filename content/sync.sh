#!/bin/bash
set -euo pipefail

PYTHON_BIN="/home/al/miniconda3/bin/python"
PROJECT_DIR="/home/al/Projects/digital-graveyard/content"
SYNC_SCRIPT="$PROJECT_DIR/sync_content.py"
BLOG_DIR="/home/al/Projects/ia_blog"

"$PYTHON_BIN" "$SYNC_SCRIPT"
cd "$BLOG_DIR"
npx quartz build --serve