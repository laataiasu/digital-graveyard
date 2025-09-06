#!/bin/bash
set -euo pipefail

PYTHON_BIN="/home/al/Projects/sandbox-hub/.venv/bin/python"
PROJECT_DIR="/home/al/Projects/digital-graveyard/content"
SYNC_SCRIPT="$PROJECT_DIR/sync_content.py"
BLOG_DIR="/home/al/Projects/digital-garden"

"$PYTHON_BIN" "$SYNC_SCRIPT"
cd "$BLOG_DIR"
npx quartz build --serve