---
title: "Multi-Platform Project State Management: Fedora Linux & Android PRoot Debian"
date: 2026-10-02
tags: [architecture, linux, android, git, state-management]
publish_external: false
---

# Multi-Platform Project State Management: Fedora Linux (x86_64) & Android PRoot Debian (aarch64)

## Executive Summary

Managing development state across a high-performance desktop workstation (**Fedora 44 x86_64**) and a mobile runtime environment (**Xiaomi 14T Pro with Termux PRoot Debian aarch64**) presents unique architectural challenges:
1. **CPU Architecture Divergence**: x86_64 vs. aarch64 prevents sharing precompiled wheels, virtual environments (`.venv`), `node_modules`, and binary caches.
2. **OS & Kernel Capabilities**: PRoot lacks Linux kernel namespace/cgroup isolation (no native Docker daemon), operates under `ptrace` emulation overhead, and must respect Android battery Doze mode (Wake-Lock Sandwich pattern).
3. **Multi-Repo Complexity**: Juggling ~10 discrete repositories across two active physical devices risks desynchronized working trees and branch divergence ("bala" split-brain states).
4. **Data Persistence**: Local SQLite databases (`events.db`, `atracker.sqlite`, `sansfinance.sqlite`) require atomic WAL checkpoints before synchronization to prevent database corruption.

---

## 1. Architectural Layers of "State"

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. Code & Working Trees   │ Git commits, uncommitted WIP, branches     │
├───────────────────────────┼────────────────────────────────────────────┤
│ 2. Toolchains & Runtimes  │ x86_64 vs aarch64 binaries, uv, bun, pkgs  │
├───────────────────────────┼────────────────────────────────────────────┤
│ 3. Application Data       │ SQLite DBs (events.db, atracker, etc.)     │
├───────────────────────────┼────────────────────────────────────────────┤
│ 4. Execution & Sessions   │ Background crons, terminal sessions, env   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Deep Dive: Layer-by-Layer Solutions

### Layer 1: Code & Working Tree Synchronization

#### A. Why Block-Level File Sync (Syncthing/Dropbox) Fails for Code
Continuous background file synchronizers treat files as opaque byte streams without awareness of Git locking semantics:
- Modifying `.git/index`, `refs/`, or pack files mid-operation corrupts the repository index.
- If you use Syncthing, you **must strictly ignore** `.git/`, `.venv/`, `node_modules/`, `target/`, and `*.sqlite`.

#### B. Mutagen (`mutagen.io`) — Low-Latency Code Sync Daemon
- **Mechanism**: Go-based bi-directional file synchronization daemon communicating over SSH (Tailscale).
- **Pros**:
  - Purpose-built for remote code synchronization.
  - Native 3-way reconciliation handles concurrent offline edits safely.
  - Granular ignore rules keep `.venv` and binary artifacts isolated per architecture.
- **Cons on Mobile**: Keeping the Mutagen daemon constantly running in PRoot keeps the CPU awake and breaks Android deep sleep unless scoped strictly to interactive sessions.

#### C. Git-Native Shadow WIP Synchronization (Recommended Pattern)
Instead of continuous filesystem daemons, use non-destructive Git shadow branches:
- **Save WIP State** (Machine A):
  ```bash
  git checkout -B "wip/$(hostname)" && git add -A && git commit -m "wip: autosync $(date -Iseconds)" && git push origin "wip/$(hostname)" --force
  ```
- **Resume WIP State** (Machine B):
  ```bash
  git fetch origin "wip/<source-device>" && git checkout "wip/<source-device>"
  # Optional: git reset --soft HEAD~1 to unstage back to working tree
  ```

#### D. Multi-Repo Orchestrators: `gita` vs `_scheduled_jobs/repos_status.py`
- **`gita`**: Python CLI tool (`pip install gita` / `uv tool install gita`). Displays color-coded branch relationships across all repos and supports context groups (e.g., `gita group add mobile ierp idx-bei portfolio-integration`).
- **Enhanced `repos-status`**: Your custom Python status checker can be extended with a `--save-wip` and `--load-wip` flag to make shadow synchronization a single command.

---

### Layer 2: Toolchains, Runtimes & Dotfiles

Fedora uses `dnf` and x86_64; PRoot Debian uses `apt` and aarch64. Synchronization must be **declarative**, not binary.

| Tool | Focus | Fedora (x86_64) | Android PRoot (aarch64) | Recommendation |
| :--- | :--- | :---: | :---: | :--- |
| **Chezmoi** | Dotfiles, secrets, shell scripts | Native | Native (single Go binary) | **Primary Choice**. Supports Go templates (`{{ if eq .chezmoi.arch "arm64" }}`). |
| **Mise (`mise-en-place`)** | Runtimes (`python`, `uv`, `bun`, `node`) | Native | Native (Rust binary) | **Primary Choice**. Universal `.mise.toml` across platforms. |
| **Devbox / Devenv** | Nix-based isolated environments | Native | High Friction | **Avoid in PRoot**. Nix hits PRoot `ptrace` and chroot sandbox limits. |
| **Devcontainers** | Docker container shells | Native | Unsupported | **Avoid in PRoot**. Docker daemon cannot run inside Android PRoot. |

#### Recommended Setup with Mise:
Manage CLI toolchains identically without container overhead:
```toml
# ~/.config/mise/config.toml
[tools]
python = "3.12"
uv = "latest"
bun = "latest"
ripgrep = "latest"
fd = "latest"
```

---

### Layer 3: SQLite & Application Data State

Current workflow uses Cloudflare R2 snapshots (`PRAGMA wal_checkpoint(TRUNCATE)` + S3 ETag verification):
- **Why Litestream is not recommended for mobile**: Litestream requires a persistent daemon streaming WAL frames. On mobile, this defeats the Wake-Lock Sandwich pattern and rapidly depletes battery.
- **Optimal Strategy**: Keep the on-demand R2 snapshot model, but make it friction-free:
  - Add pre-flight check in mobile crons (`event pull` prior to execution).
  - Add post-flight check in mobile crons (`event push` after data generation).
  - Add interactive shell aliases on laptop (`agy-start` runs `event pull && repos-status -p`).

---

### Layer 4: Execution & Session Architecture

Instead of treating both devices as symmetric general-purpose workstations, enforce a **strict role contract**:

1. **Workstation (Fedora 44)**:
   - Primary interactive development, AI agent sessions (`agy`), deep refactoring, GUI tools.
2. **Mobile (Xiaomi 14T Pro / PRoot)**:
   - Autonomous headless cron runner (`idx-bei`, `ierp`, `nichsedge.github.io`, `portfolio-integration`).
   - Battery-optimized via Wake-Lock Sandwich.
   - Remote client via Tailscale SSH when away from laptop.

---

## 3. Implementation Roadmap

1. **Adopt `mise` for Toolchains**:
   Replace disparate system package installs with `mise` across Fedora and PRoot to guarantee matching tool versions.
2. **Adopt `chezmoi` for Dotfiles**:
   Migrate `dotfiles-private` symlink scripts to `chezmoi` to leverage conditional templating for OS/architecture differences.
3. **Enhance `repos-status` with Shadow WIP Sync**:
   Add automated push/pull of `wip/<device>` branches to eliminate manual merge conflict resolution.
4. **Enforce Pre/Post-Flight Contracts**:
   Automate R2 database pulls and pushes at shell entry and exit points.
