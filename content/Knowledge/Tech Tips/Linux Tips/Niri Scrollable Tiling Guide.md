---
title: "Niri & Dank Material Shell (DMS) Power User Guide"
date: 2026-09-04
tags: [guide, linux, wayland]
publish_external: true
updated: 2026-09-14
---

# Niri & Dank Material Shell (DMS) Power User Guide

> [!NOTE] Workstation Primary Desktop Environment
> As of **2026-09-14**, **Niri** (paired with Dank Material Shell) is the primary daily-driver desktop environment on Fedora. [[Hyprland Power User Guide|Hyprland]] and standalone daemons (`waybar`, `mako`, `cliphist`, `hyprpaper`) have been decommissioned and pruned. Stock **GNOME Wayland** is retained as an emergency fallback desktop environment.

A complete architectural and operational guide to running **Niri** on [[Linux]] ([[Wayland]]) paired with **Dank Material Shell (DMS)**, detailing the infinite scrollable ribbon paradigm, keyboard responsiveness tuning, keybindings, and emergency recovery procedures.

---

## 1. Paradigm Shift: Infinite Ribbon vs. Split Trees

Traditional dynamic tiling compositors like [[Hyprland Power User Guide|Hyprland (Deprecated)]], Sway, or i3 use binary space partitioning (BSP / dwindle) or master-stack layouts. When opening multiple windows on a single monitor, windows are progressively halved into smaller, squished rectangles until they become illegible.

**Niri** replaces split trees with an **infinite horizontal ribbon**:

1. **Natural Widths**: Windows retain their optimal width (e.g. 50% or 33% of the screen) and never get squished.
2. **Horizontal Flow**: Opening new applications appends them to the ribbon to the right. Navigating left and right smoothly pans the viewport.
3. **Overview Matrix (`⌘ O`)**: A native bird's-eye view zooming out to inspect all active columns and dynamic workspaces at once.
4. **Column Stacking**: Windows within the same column can either stack vertically or convert into a tabbed group (`⌘ W`).

---

## 2. Desktop Shell Architecture: DMS (Quickshell)

Instead of stitching together multiple standalone daemons (`waybar`, `dunst`/`mako`, `rofi`/`wofi`, `swaylock`), Niri is paired with **Dank Material Shell (DMS)**, a unified Wayland shell built on Quickshell and Qt6:

* **Top Bar & Flyouts**: Interactive quick toggles for Wi-Fi, Bluetooth, Audio sinks, and power profiles.
* **Notification Daemon**: Native D-Bus notification handler (`org.freedesktop.Notifications`) with action popups and history.
* **Material You Dynamic Theming**: DMS dynamically generates and exports color schemes to `~/.config/niri/dms/colors.kdl`.
* **Integrated Sub-Configs**:
  * `dms/colors.kdl` — Material You active/inactive borders, focus rings, and tab indicators.
  * `dms/layout.kdl` — Window geometry corner radii (12px rounded corners) and borders.
  * `dms/wpblur.kdl` — Layer rules for background blur on wallpapers.
  * `dms/alttab.kdl` — Recent windows switcher styling.

---

## 3. Keybinding Matrix

### ⚡ Window & Ribbon Navigation
| Keybinding | Action | Description |
| :--- | :--- | :--- |
| `⌘ H` / `⌘ L` | **Focus Left / Right** | Pan focus between columns on the ribbon |
| `⌘ J` / `⌘ K` | **Focus Down / Up** | Move focus between stacked windows in a column |
| `⌘ ⌃ H` / `⌘ ⌃ L` | **Move Column Left / Right** | Shift column position horizontally on the ribbon |
| `⌘ ⌃ J` / `⌘ ⌃ K` | **Move Window Down / Up** | Shift window position vertically inside a column |
| `⌘ Home` / `⌘ End` | **First / Last Column** | Jump directly to the start or end of the ribbon |
| `⌘ O` | **Toggle Overview** | Zoomed-out workspace overview matrix |
| `⌘ Q` | **Close Window** | Close active application window |

---

### 📑 Column Organization & Stacking
| Keybinding | Action | Description |
| :--- | :--- | :--- |
| `⌘ [` / `⌘ ]` | **Consume / Expel** | Pull window into active column or expel it out |
| `⌘ ,` | **Consume Below** | Pull right-side window underneath current window |
| `⌘ .` | **Expel Below** | Push bottom window out into its own column |
| `⌘ W` | **Toggle Tabbed Mode** | Switch column between vertical stack and tabbed view |

---

### 📐 Column Sizing & Presets
| Keybinding | Action | Description |
| :--- | :--- | :--- |
| `⌘ R` | **Cycle Preset Widths** | Toggles between 33%, 50%, and 67% screen widths |
| `⌘ ⇧ R` | **Cycle Widths Back** | Cycles preset widths in reverse order |
| `⌘ -` / `⌘ =` | **Adjust Width ±10%** | Fine-tune focused column width |
| `⌘ F` | **Maximize Column** | Expands column width while keeping gaps |
| `⌘ M` | **Maximize to Edges** | True edge-to-edge maximizing (zero gaps) |
| `⌘ ⇧ F` | **Fullscreen** | Standard Wayland fullscreen covering bar and panels |

---

### 🎛️ Shell & System Integrations (DMS)
| Keybinding | Action | Description |
| :--- | :--- | :--- |
| `⌘ T` / `⌘ ↩` | **Terminal** | Spawns [[Ghostty]] |
| `⌘ Space` / `⌘ D` | **Application Launcher** | Toggles DMS Material You application search |
| `⌘ ⇧ T` | **Tailscale VPN Menu** | Interactive Tailscale VPN manager, peer picker & diagnostics |
| `⌘ V` | **Clipboard History** | Opens DMS clipboard history picker |
| `⌘ B` | **Web Browser** | Launches Google Chrome |
| `⌘ E` | **File Manager** | Opens Nautilus in a new window |
| `⌘ N` | **Control Center** | Toggles DMS quick settings, notifications & Night Light |
| `⌘ ⌥ ⌫` | **Toggle Floating** | Toggle focused window between tiling ribbon and floating layer |
| `⌘ /` / `⌘ ⇧ /` | **Hotkey Overlay** | Native full-screen keybinding cheat sheet overlay |
| `⌘ ⌥ L` | **Lock Screen** | Engages DMS session lock |
| `⌘ ⇧ Q` | **Power Menu** | Toggles DMS session & power menu (Shutdown, Restart, Lock) |

---

## 4. Input & Keyboard Delay Tuning

For high-speed typing and responsive window navigation, Niri's input latency is tuned to match workstation standards:

```kdl
input {
    keyboard {
        numlock
        repeat-delay 250   // 250ms delay before repeating
        repeat-rate 35     // 35 repeats per second
    }

    touchpad {
        tap
        natural-scroll
    }
}
```

---

## 5. Live Diagnostics & CLI Management

Niri and DMS offer native IPC tools for validation and troubleshooting:

```bash
# Validate Niri configuration syntax
niri validate

# Live-reload Niri configuration without restarting session
niri msg action load-config-file

# Inspect connected displays and resolutions
niri msg outputs

# DMS IPC commands
dms ipc call launcher toggle       # Trigger launcher
dms ipc call clipboard toggle      # Trigger clipboard history
dms ipc call control-center toggle # Trigger quick settings
dms doctor                         # Run complete health and font check
```

---

## 6. Emergency Recovery & Safety Fallback: Stock GNOME Wayland

To ensure the workstation is resilient against compositor bugs, broken configurations, or graphics driver updates, **stock GNOME Wayland** (`gnome-session-wayland-session`) is permanently installed as an out-of-the-box fallback environment.

### When to Use GNOME Fallback
1. **Niri Configuration Syntax Errors**: If an invalid KDL node prevents Niri from launching during graphical login.
2. **GPU Driver / DRM Issues**: If an experimental kernel or Mesa driver update causes Wayland protocol regressions with scrollable tiling.
3. **Complex Multi-Monitor / Projector Scenarios**: Presenting on external projectors or non-standard display matrices that require GNOME's native GUI display settings.

### How to Switch to GNOME
1. **From Active Session**: Trigger the power menu (`⌘ ⇧ Q`) or open a terminal and run:
   ```bash
   loginctl terminate-user "$USER"
   ```
2. **At GDM Login Screen**:
   - Click user account (**Amal**).
   - Click the **Gear icon (⚙️)** in the bottom-right corner of the screen.
   - Select **GNOME** (or **GNOME on Wayland**) instead of Niri.
   - Enter your password to log in.
3. **From Virtual TTY (Headless Rescue)**:
   If the display server is completely unresponsive:
   - Press `Ctrl + Alt + F3` to access TTY3.
   - Log in with workstation credentials.
   - Verify Niri configuration and logs:
     ```bash
     niri validate
     journalctl --user -u niri -n 50 --no-pager
     ```
   - Roll back recent edits in `~/.config/niri/config.kdl` if needed, then return to GDM with `Ctrl + Alt + F1`.
