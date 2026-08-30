---
title: "Remote Code Server and Cloudflare Tunnel"
date: 2026-08-27
tags: [guide]
publish_external: true
---

A complete setup for hosting a browser-accessible [[VS Code]] instance on [[Fedora]] via `code-server`, exposed securely to any remote machine or device using a free [[Cloudflare]] Tunnel.

---

## 1. Architecture Overview

- **`code-server`**: Runs locally on `127.0.0.1:8080` as a systemd user service.
- **`cloudflared`**: Connects the local port to Cloudflare edge network via HTTP/2 tunnel, providing public HTTPS without opening router ports or exposing static public IPs.
- **`systemd --user` with linger**: Keeps both services running continuously in the background even after logging out.

---

## 2. Service Configuration

### code-server
- **Config path**: `~/.config/code-server/config.yaml`
- **Settings**:
  ```yaml
  bind-addr: 127.0.0.1:8080
  auth: password
  password: <your_password>
  cert: false
  ```

### cloudflared systemd Service
- **Service path**: `~/.config/systemd/user/cloudflared.service`
- **Definition**:
  ```ini
  [Unit]
  Description=Cloudflare Tunnel for code-server
  After=network.target code-server.service
  Requires=code-server.service

  [Service]
  Type=simple
  ExecStart=/usr/local/bin/cloudflared --no-autoupdate tunnel --protocol http2 --url http://127.0.0.1:8080
  Restart=always
  RestartSec=5s

  [Install]
  WantedBy=default.target
  ```

---

## 3. Remote Access Guide

### Quick Access via Browser
1. Find the current tunnel URL:
   ```bash
   journalctl --user -u cloudflared -n 30 --no-pager | grep -o 'https://.*\.trycloudflare\.com'
   ```
2. Open the URL in any web browser on another PC, tablet, or phone.
3. Enter the configured password from `~/.config/code-server/config.yaml`.

### Upgrading to a Custom Domain (100% Free)
1. Go to [Cloudflare Zero Trust Dashboard](https://one.dash.cloudflare.com/) $\rightarrow$ **Networks** $\rightarrow$ **Tunnels**.
2. Create a named tunnel and route `code.yourdomain.com` to `http://localhost:8080`.
3. Install connector token on Fedora:
   ```bash
   sudo cloudflared service install <TUNNEL_TOKEN>
   ```

---

## 4. Useful Operations & Troubleshooting

| Task | Command |
| :--- | :--- |
| **Check code-server status** | `systemctl --user status code-server` |
| **Restart code-server** | `systemctl --user restart code-server` |
| **Check cloudflared status** | `systemctl --user status cloudflared` |
| **View live tunnel logs / URL** | `journalctl --user -u cloudflared -f` |
| **Kill stale port 8080 process** | `kill -9 $(pgrep -f code-server)` |

