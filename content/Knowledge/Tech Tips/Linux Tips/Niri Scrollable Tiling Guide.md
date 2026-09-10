---
title: "Niri & Dank Material Shell (DMS) Power User Guide"
date: 2026-09-04
tags: [guide]
publish_external: true
updated: 2026-09-04
---

# Niri & Dank Material Shell (DMS) Power User Guide

A complete architectural and operational guide to running **Niri** on [[Linux]] ([[Wayland]]) paired with **Dank Material Shell (DMS)**, detailing the infinite scrollable ribbon paradigm, keyboard responsiveness tuning, and keybindings.

---

## 1. Paradigm Shift: Infinite Ribbon vs. Split Trees

Traditional dynamic tiling compositors like [[Hyprland Power User Guide|Hyprland]], Sway, or i3 use binary space partitioning (BSP / dwindle) or master-stack layouts. When opening multiple windows on a single monitor, windows are progressively halved into smaller, squished rectangles until they become illegible.

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
| `⌘ T` | **Terminal** | Spawns [[Ghostty]] |
| `⌘ D` | **Application Launcher** | Toggles DMS Material You application search |
| `⌘ V` | **Clipboard History** | Opens DMS clipboard history picker |
| `⌘ N` | **Control Center** | Toggles DMS quick settings & notification center |
| `⌘ ⇧ V` | **Toggle Floating** | Move window between tiling ribbon and floating layer |
| `⌘ ⌥ L` | **Lock Screen** | Engages DMS session lock |

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
