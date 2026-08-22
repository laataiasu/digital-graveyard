---
title: "Linux & Terminal Power User Guide"
date: 2026-08-18
tags: [guide]
publish_external: true
updated: 2026-08-19
---

# Linux & Terminal Power User Guide

A practical, referenceable guide to terminal ergonomics, modern CLI replacements, session multiplexing, fuzzy pipelines, [[Git]] acceleration, and low-latency mobile remote development.

---

## 1. Terminal Canvas (Kitty)

Kitty provides a GPU-accelerated OpenGL canvas with native Wayland integration, font ligature rendering, and rich media protocols.

### Essential Keyboard Shortcuts
| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Ctrl + Shift + e` | **URL Hints** | Highlights visible URLs with letter tags. Press the letter to open in browser. |
| `Ctrl + Shift + p` > `f` | **Path Hints** | Pick and insert any file path visible on screen into the active command. |
| `Ctrl + Shift + p` > `h` | **Hash Hints** | Pick and insert git commit hashes from screen buffer. |
| `Ctrl + Shift + u` | **Unicode Picker** | Interactive search and insert for emojis and Nerd Font glyphs. |
| `Ctrl + Shift + h` | **Scrollback Pager** | Dumps current terminal history into a pager for regex search. |

### Visual Tools
* **GPU Side-by-Side Diff**:
  ```bash
  alias kdiff='kitty +kitten diff'
  kdiff file_a.py file_b.py
  ```
* **Terminal Image Viewer**:
  ```bash
  kitty +kitten icat image.png
  ```

---

## 2. Session Multiplexing & Layouts (Zellij)

Zellij manages persistent terminal tabs, splits, floating panes, and workspace resurrection across reboots.

### Key Shortcuts & Modes
* `Ctrl + p` + `n`: Create new pane (auto-splits based on available geometry).
* `Ctrl + p` + `←/→/↑/↓` or `h/j/k/l`: Navigate between panes.
* `Ctrl + p` + `w`: Toggle floating pane mode.
* `Ctrl + t` + `n`: Open new tab.
* `Ctrl + o` + `d`: **Detach session** (leaves background servers, builds, and agents running).
* `zellij attach main`: Reconnect to the active session.

### Auto-Attaching on SSH Login
To ensure remote sessions automatically enter persistent multiplexing, configure `~/.zshrc`:
```zsh
if -n "$SSH_CONNECTION" && -z "$ZELLIJ"; then
  zellij attach -c main
fi
```

### Declarative Multi-Pane Layouts (`~/.config/zellij/layouts/dev.kdl`)
Spin up a standardized development workspace with a single command (`zellij --layout dev`):
```kdl
layout {
    pane split_direction="vertical" {
        pane size="65%" name="Editor / Primary" focus=true
        pane split_direction="horizontal" size="35%" {
            pane name="AI Agent / Terminal"
            pane name="Logs / Dev Server"
        }
    }
    pane size=1 borderless=true {
        plugin location="zellij:compact-bar"
    }
}
```

---

## 3. Modern Core CLI Replacements

Replace slow legacy Unix utilities with high-performance, syntax-aware tools:

| Legacy Tool | Modern Alternative | Key Advantage | Command / Alias |
| :--- | :--- | :--- | :--- |
| `cd` | **`zoxide`** | Frecency-based smart jumping across directory history | `z project-dir` |
| `cat` / `less` | **`bat`** | Syntax highlighting, line numbers, and Git change gutter | `bat main.py` |
| `du -sh` | **`dust`** | Instant hierarchical visual breakdown of disk consumption | `dust` |
| `top` / `htop` | **`btop`** | Rich TUI dashboard for CPU, memory, disks, and network I/O | `btop` |
| `find` | **`fd`** | Intuitive syntax, respects `.gitignore`, fast multithreading | `fd '\.py$'` |

### Shell Integration Aliases (`~/.zshrc`)
```zsh
# Smart directory jumping
eval "$(zoxide init zsh)"

# Syntax-aware pager
alias cat='bat --paging=never --style=plain'
alias preview='bat --style=numbers,changes'
```

---

## 4. Fuzzy Pipelines & Zsh Ergonomics

Combine `fzf`, `ripgrep`, and `fd` with global aliases to eliminate repetitive typing.

### Global Pipe Aliases
Append global aliases to `~/.zshrc` to pipe output into tools using single-letter flags:
```zsh
alias -g G='| rg'
alias -g J='| jq'
alias -g F='| fzf'
alias -g L='| less'
```

* **Usage Examples**:
  ```bash
  ps aux G python          # Search processes for 'python'
  cat data.json J          # Format and colorize JSON
  dnf list installed F     # Fuzzy search installed packages
  ```

### Interactive Process Killer (`fkill`)
```zsh
fkill() {
  local pid=$(ps -ef | sed 1d | fzf -m | awk '{print $2}')
  if [ "x$pid" != "x" ]; then
    echo $pid | xargs kill -${1:-9}
  fi
}
```

> [!TIP]
> **Shell History Supercharging**: Install **`atuin`** (`eval "$(atuin init zsh)"`) to replace default `Ctrl + R` with an encrypted, SQLite-backed interactive history search that records exit codes, execution duration, and directory context across multiple machines.

---

## 5. Git Power-User Acceleration

### Interactive Staging with `lazygit`
```bash
alias lg='lazygit'
```
* `Space`: Stage individual lines or hunks instead of entire files.
* `c`: Commit with formatted message.
* `P`: Push to upstream remote.
* `z`: Undo last Git operation.

> [!NOTE]
> Configure **`delta`** in `~/.gitconfig` as the default pager for side-by-side syntax-highlighted diffs inside both terminal Git and `lazygit`.

### Parallel Worktrees (Branching Without Stashing)
Avoid switching branches or stashing dirty working trees:
```bash
# Create and enter isolated worktree directory for a feature branch
git worktree add ../feature-branch feature-branch
cd ../feature-branch

# Remove worktree when merged
git worktree remove ../feature-branch
```

---

## 6. Mobile Remote Workflow & Network Ergonomics (Termius + Tailscale + Mosh)

Control full workstation environments and AI coding agents from a mobile device (iOS/Android Termius over Tailscale) with zero connection stalls.

### 1. Mosh (Mobile Shell) over UDP
Standard TCP SSH drops when mobile devices transition between Wi-Fi and cellular networks. Mosh runs over UDP:
* **Connection Roaming**: Automatically survives IP changes, sleep mode, and network dropouts.
* **Instant Local Echo**: Predicts typing and cursor movement locally, eliminating mobile network latency.
* **Termius Configuration**: Set host connection address to Tailscale IP/hostname and toggle **Use Mosh**.

### 2. SSH Connection Multiplexing (`ControlMaster`)
Eliminate handshake latency for repeated SSH, SCP, and Rsync connections by reusing existing sockets.

Add to `~/.ssh/config`:
```ssh-config
Host *
  ControlMaster auto
  ControlPath ~/.ssh/sockets/%r@%h-%p
  ControlPersist 4h
  ServerAliveInterval 60
  ServerAliveCountMax 3
```
*(Ensure socket directory exists: `mkdir -p ~/.ssh/sockets && chmod 700 ~/.ssh/sockets`)*

### 3. Background Push Alerts (`ntfy`)
Receive phone vibrations when background jobs or AI coding agents finish long tasks:
1. Subscribe to a private topic on the free **ntfy** mobile app.
2. Define a shell helper in `~/.zshrc`:
   ```zsh
   notify() {
     local msg="${1:-Task completed}"
     curl -s -d "$msg" "https://ntfy.sh/YOUR_PRIVATE_TOPIC" > /dev/null
   }
   ```
3. Attach to long-running tasks:
   ```bash
   agy "refactor module" && notify "AGY finished task!"
   ```

### 4. Termius Mobile Accessory Shortcuts
* **Keyboard Accessory Bar**: Add `Ctrl+C`, `Esc`, `Tab`, `|`, `~`, `_`, `Enter`.
* **One-Tap Snippets**: `agy`, `lazygit`, `up`, `fkill`, `git status`.

---

## 7. Background Automation & Process Resilience (`systemd --user`)

Replace fragile cron entries and manual loop scripts with managed user-space systemd units.

### Service Unit (`~/.config/systemd/user/task-sync.service`)
```ini
[Unit]
Description=User Background Sync Task

[Service]
Type=oneshot
ExecStart=%h/Projects/sync_git_repos.sh
```

### Timer Unit (`~/.config/systemd/user/task-sync.timer`)
```ini
[Unit]
Description=Daily Task Sync Timer

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

### Management Commands
```bash
systemctl --user daemon-reload
systemctl --user enable --now task-sync.timer
systemctl --user list-timers
```

### Preventing Sleep During Heavy Workloads (`systemd-inhibit`)
Prevent laptops or workstations from entering sleep/suspend states when closing the lid during long builds, model training, or data transfers:
```bash
systemd-inhibit --what=idle:sleep:handle-lid-switch --why="Running compilation" make build
```
