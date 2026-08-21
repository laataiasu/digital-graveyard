"""
Thin bridge from get-data to ierp. All normalization logic lives in ierp
(ierp/core/sources.py); this module only fetches rows from the source loaders
and hands them to ierp's ingestion endpoint.

Two transports, tried in order:
  1. HTTP POST to a running `ierp serve-ingest` (default http://127.0.0.1:8765)
  2. Fallback: `uv run ierp ingest-rows <source> <tmpfile>` subprocess
"""

import json
import os
import subprocess
import tempfile
import urllib.request
import urllib.error

IERP_ROOT = os.environ.get("IERP_ROOT", os.path.expanduser("~/Projects/ierp"))
IERP_INGEST_URL = os.environ.get("IERP_INGEST_URL", "http://127.0.0.1:8765")


def _post_http(source_key: str, rows: list) -> bool:
    """POST raw rows to the ierp ingest server. Returns False if unreachable."""
    try:
        req = urllib.request.Request(
            f"{IERP_INGEST_URL}/ingest/{source_key}",
            data=json.dumps(rows, default=str).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        print(f"[ierp] {body} ({source_key}: {len(rows)} rows)")
        return True
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:300]
        print(f"[ierp] HTTP {e.code} for {source_key}: {detail}")
        return False
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError):
        return False  # server not running -> try subprocess fallback


def _post_subprocess(source_key: str, rows: list) -> bool:
    """Fallback: pipe rows through `uv run ierp ingest-rows`."""
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(rows, f, ensure_ascii=False, default=str)
        tmp = f.name
    try:
        result = subprocess.run(
            ["uv", "run", "ierp", "ingest-rows", source_key, tmp],
            cwd=IERP_ROOT, capture_output=True, text=True, timeout=300,
        )
        if result.returncode != 0:
            print(f"[ierp] Ingest failed for {source_key}: {result.stderr.strip()[:500]}")
            return False
        print(f"[ierp] {result.stdout.strip()} ({source_key}: {len(rows)} rows)")
        return True
    except (subprocess.TimeoutExpired, OSError) as e:
        print(f"[ierp] Ingest error for {source_key}: {e}")
        return False
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def push_to_ierp(source_key: str, rows: list) -> bool:
    """Pushes RAW source rows to ierp. Best-effort; never raises."""
    if not rows:
        return True
    if _post_http(source_key, rows):
        return True
    return _post_subprocess(source_key, rows)
