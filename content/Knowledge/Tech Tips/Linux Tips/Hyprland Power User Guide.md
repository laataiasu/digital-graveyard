---
title: "Hyprland Power User & macOS Workflow Guide"
date: 2026-09-01
tags: [guide]
publish_external: true
updated: 2026-09-01
---

# Hyprland Power User & macOS Workflow Guide

A definitive architectural guide to configuring **Hyprland on Linux (Wayland)** with a blended **macOS ergonomics + Vim efficiency + Rectangle tiling** setup, resilient background services, and zero-sleep AFK capabilities.

---

## 1. Ergonomic Philosophy & Navigation Hierarchy

The configuration blends three ergonomic paradigms:

1. **macOS Muscle Memory**: `⌘ Space` for Spotlight (Wofi), `⌘ Tab` window cycling, `⌘ ↩` / `⌘ T` for Ghostty terminal, `⌘ ⇧ 3/4/5` for Grim/Slurp screenshots, and `⌘ Q / ⌘ W` to close windows.
2. **Vim Home-Row Navigation**: Zero wrist movement from typing position using `Super + H/J/K/L` for spatial focus and `Super + Shift + H/J/K/L` for window swapping.
3. **Rectangle Window Management**: `⌘ ⌥ + Arrow Keys` or `Ctrl ⌥ + Arrow Keys` to snap windows into halves, corners, center, and maximized states.

---

## 2. Full Keybinding Matrix

### ⚡ Navigation & Spatial Movement
| Keybinding | Action | Description |
| :--- | :--- | :--- |
| `⌘ H` / `⌘ L` | **Focus Left / Right** | Home-row horizontal window focus |
| `⌘ K` / `⌘ J` | **Focus Up / Down** | Home-row vertical window focus |
| `⌘ ⇧ H` / `⌘ ⇧ L` | **Swap Left / Right** | Swap window positions horizontally |
| `⌘ ⇧ K` / `⌘ ⇧ J` | **Swap Up / Down** | Swap window positions vertically |
| `⌘ ⇧ Arrow Keys` | **Directional Focus** | Arrow-key spatial window focus |

---

### 📑 Tabbed Window Groups (Hyprland Tabs)
| Keybinding | Action | Description |
| :--- | :--- | :--- |
| `⌘ G` | **Toggle Group** | Turn focused window into a tabbed frame |
| `⌘ [` | **Previous Tab** | Cycle to previous tab in active group |
| `⌘ ]` | **Next Tab** | Cycle to next tab in active group |
| `⌘ ⇧ G` | **Extract Window** | Pop active tab out of the group into a tile |

---

### 🎛️ Modal Resize Mode (Vim Submap)
| Keybinding | Action | Description |
| :--- | :--- | :--- |
| `⌘ R` | **Enter Resize Mode** | Enters submap for rapid layout adjustment |
| `H / J / K / L` | **Adjust Proportions** | Shrink / expand active window dimensions |
| `Enter` / `Esc` | **Exit Resize Mode** | Lock window geometry and return to normal mode |

---

### 📐 Rectangle Window Snapping
| Shortcut (macOS / Classic) | Window Position |
| :--- | :--- |
| `⌘ ⌥ ←` / `⌃ ⌥ ←` | **Left Half** |
| `⌘ ⌥ →` / `⌃ ⌥ →` | **Right Half** |
| `⌘ ⌥ ↑` / `⌃ ⌥ ↑` | **Top Half** |
| `⌘ ⌥ ↓` / `⌃ ⌥ ↓` | **Bottom Half** |
| `⌘ ⌥ U` / `⌃ ⌥ U` | **Top-Left Corner** |
| `⌘ ⌥ I` / `⌃ ⌥ I` | **Top-Right Corner** |
| `⌘ ⌥ J` / `⌃ ⌥ J` | **Bottom-Left Corner** |
| `⌘ ⌥ K` / `⌃ ⌥ K` | **Bottom-Right Corner** |
| `⌘ ⌥ ↩` / `⌃ ⌥ ↩` | **Maximize (Retain Bar)** |
| `⌘ ⌥ F` / `⌃ ⌥ F` | **Fullscreen Mode** |
| `⌘ ⌥ C` / `⌃ ⌥ C` | **Center Window on Screen** |
| `⌘ ⌥ ⌫` / `⌃ ⌥ ⌫` | **Toggle Floating / Tiled** |

---

### 🚀 Launchers, Spaces & Scratchpads
| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `⌘ Space` | **Spotlight Launcher** | Fuzzy application search via Wofi |
| `⌘ \`` (Grave/Tilde) | **Dropdown Terminal** | Instant Quake-style dropdown scratchpad terminal |
| `⌘ M` / `⌘ ⇧ M` | **Minimize / Restore** | Send window to scratchpad / Restore scratchpad |
| `⌘ ⇧ Space` / `⌘ ⇧ V` | **Clipboard History** | Cliphist clipboard picker with auto-paste |
| `⌘ 1 .. 9` | **Switch Space** | Jump directly to Workspace 1..9 |
| `⌘ ⌃ 1 .. 9` | **Move to Space** | Move focused window to Workspace 1..9 |
| `⌃ ←` / `⌃ →` | **Relative Spaces** | Cycle to previous / next workspace |
| `3-Finger Swipe ↔` | **Trackpad Swipe** | Fluid touchpad gesture workspace switching |
| `⌘ ⇧ 3` / `4` / `5` | **Screenshot** | Fullscreen / Region selection / Focused window |
| `⌃ ⌘ Q` / `⌃ ⌘ L` | **Lock Screen** | Native macOS lock screen (`hyprlock`) |

---

## 3. Input & Trackpad Configuration

Optimized for high-precision trackpads with zero-lag response:

```ini
input {
    kb_layout = us
    kb_options = caps:escape
    repeat_rate = 35
    repeat_delay = 250
    follow_mouse = 1
    sensitivity = 0

    touchpad {
        natural_scroll = true
        disable_while_typing = false
        tap-to-click = true
        clickfinger_behavior = false
        middle_button_emulation = true
        tap-and-drag = true
        scroll_factor = 1.0
    }
}

# ── Trackpad Gestures (macOS Spaces) ──
gesture = 3, horizontal, workspace
gesture = 4, up, workspace, e-1
gesture = 4, down, workspace, e+1
```

---

## 4. 24/7 Always-On AFK & Daemon Hardening

To ensure background daemons (e.g. [[What I Built With Hermes Agent|Hermes Agent]], Tailscale, SSH servers) stay online indefinitely without sleep or network drops:

1. **Mask System Sleep Targets:**
   ```bash
   sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
   ```
2. **Ignore Laptop Lid Close:**
   `/etc/systemd/logind.conf.d/dont-suspend.conf`:
   ```ini
   [Login]
   HandleLidSwitch=ignore
   HandleLidSwitchExternalPower=ignore
   HandleLidSwitchDocked=ignore
   ```
3. **Disable Wi-Fi Power Savings:**
   `/etc/NetworkManager/conf.d/disable-wifi-powersave.conf`:
   ```ini
   [connection]
   wifi.powersave = 2
   ```
4. **Hypridle Configuration:**
   Keep session locking (`hyprlock`) and display blanking (`dpms off`), but avoid calling `systemctl suspend`.

---

## 5. Lua Configuration & `hyprconf2lua` Migration (v0.55+)

Hyprland v0.55+ natively supports complete Lua scripting via `~/.config/hypr/hyprland.lua`, superseding legacy `.conf` hyprlang files with programmatic flexibility, typed module helpers (`hl.*`), and dynamic submaps.

### Migration Tooling:
Use [`hyprconf2lua`](https://github.com/Prateek-squadron/hyprconf2lua) for automated AST conversion:
```bash
uv run --project /tmp/hyprconf2lua hyprconf2lua ~/.config/hypr/hyprland.conf -o ~/.config/hypr/hyprland.lua
```

### Compiler Verification:
Always verify config syntax before launching:
```bash
Hyprland --verify-config
```
Output:
```text
DEBUG ]: [cfg] Using lua config found at ~/.config/hypr/hyprland.lua
======== Config parsing result:
config ok
```

