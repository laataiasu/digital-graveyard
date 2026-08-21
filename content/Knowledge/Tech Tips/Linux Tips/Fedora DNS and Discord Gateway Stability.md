---
title: "Fedora DNS and Discord Gateway Stability"
date: 2026-08-21
tags: [guide, linux, fedora, dns, discord]
publish_external: false
---

## The problem

Hermes gateway (Discord bot) on my Fedora 44 workstation kept dropping slash
commands: I'd send `/reset` or `/model` from Discord DM or by @mentioning the
bot in a channel, and often nothing happened — no error, no response.

## Root cause chain

1. **Flaky DNS from the router.** The wifi connection used the router
   (`192.168.1.1`) as DNS server. It intermittently failed:
   `Cannot connect to host discord.com:443 [Temporary failure in name resolution]`.
2. **Zombie websocket windows.** Each DNS failure caused Discord gateway
   reconnects (`Discord Gateway WebSocket unhealthy (socket_closed)`) and
   heartbeats falling behind (`Can't keep up, shard websocket is 15.6s behind`).
   During those windows the bot *looked* connected but wasn't receiving events —
   slash interactions were delivered to a dead socket and vanished silently.
3. **Sync churn on every restart.** Every gateway restart re-synced ~64 slash
   commands to Discord's API, which has a tiny rate-limit bucket. Repeated
   restarts kept hitting 429s (100–263s backoffs). Not the direct cause of
   dropped commands (registered commands persist), but it made restarts
   unreliable as a fix.

## The fix (Fedora 44: systemd-resolved + NetworkManager)

Don't edit `/etc/resolv.conf` (stub, managed by systemd-resolved) and don't
touch shell startup files. Set DNS on the NetworkManager connection profile:

```bash
# Per-connection DNS override, persistent across reboots/reconnects
nmcli connection modify "TP-Link_C8B8" \
  ipv4.dns "1.1.1.1 8.8.8.8" \
  ipv4.ignore-auto-dns yes

# Re-activate
nmcli connection up "TP-Link_C8B8"

# Verify
resolvectl dns wlo1
resolvectl query discord.com
```

Then stop the sync churn — the commands were already registered on Discord's
side (verify with the API using the bot token), so disable per-restart sync:

```bash
echo 'DISCORD_COMMAND_SYNC_POLICY=off' >> ~/.hermes/.env
hermes gateway restart   # from a separate shell, not from inside the gateway
```

## Debugging tips that helped

- Gateway logs: `grep -E 'unhealthy|Can't keep up|name resolution|429' ~/.hermes/logs/gateway.log`
- Check what commands Discord *actually* has registered (not what the bot
  thinks): `GET /applications/<app_id>/commands` with the bot token. Plain
  `urllib` gets 403 (Cloudflare error 1010) — use aiohttp with a proper
  `DiscordBot` User-Agent.
- `resolvectl status` shows which DNS server each link actually uses.
- No global IPv6 on the wifi link (only link-local) — Discord over IPv6
  fails instantly (`curl -6` returns 000), so IPv4 is what matters here.
