---
title: "What I Built with Hermes Agent"
date: 2026-08-22
tags: [guide]
publish_external: true
---

I run [Hermes Agent](https://github.com/NousResearch/hermes-agent) — an open-source personal AI agent by Nous Research — as a permanent resident on my Fedora workstation. It's not a chat window I open occasionally; it's a background service wired into my Discord and Telegram, with terminal access, persistent memory, skills, and its own scheduler. This note is a tour of what that actually looks like in practice, for anyone curious about living with a personal agent.

## The setup

Hermes runs as a systemd user service (the "gateway") that stays connected to my messaging platforms. I talk to it from Discord DMs or Telegram the same way I'd text a colleague — from my phone, from bed, from anywhere — and it acts on the same machine where all my projects live.

The pieces that matter:

- **Gateways**: Discord + Telegram adapters, so the same brain answers wherever I am.
- **Persistent memory**: it remembers my preferences across sessions — which git identity to use per repo, that I want `uv` instead of pip, how I like commits written.
- **Skills**: reusable procedural knowledge (how to audit my OS, how to summarize a YouTube video, how to handle my ERP database) loaded on demand.
- **Cron**: native scheduled jobs that can run scripts *or* full agent reasoning on a schedule, delivering results back to a chat.
- **Terminal + file access**: when I ask for something, it actually does it — edits files, runs commands, commits and pushes.

## What it does day to day

### Scheduled automation

Two long-running jobs deliver to a private Discord channel:

- **Weekly GitHub sync** (Sundays): sweeps my local repos and pushes anything left uncommitted.
- **Monthly portfolio integration** (daily data-quality pass at 02:30): keeps my portfolio site's data fresh, with checks before publishing.

Because the cron jobs are just shell entry points into `~/.hermes/scripts/`, they survive reboots via systemd and notify me on failure instead of dying silently.

### Debugging partner with root access

The best example: my Discord bot kept silently dropping slash commands. Instead of me grepping logs manually, I described the symptom and the agent traced the whole chain — flaky router DNS causing gateway reconnects, zombie websockets eating events, and command-sync rate limits masking the real problem — then applied a persistent fix via NetworkManager and documented the entire playbook. Full write-up: [[Fedora DNS and Discord Gateway Stability]].

That's the pattern I keep seeing: an agent with log access, memory of past incidents, and permission to actually fix things turns multi-hour debugging sessions into a single conversation.

### Personal data infrastructure

My structured personal data lives in a small SQLite-backed "personal ERP" project. The agent manages it through a CLI — logging events, querying history — and exports derived views (garden notes, portfolio data) from it. The agent knows this architecture across every session, so "log that I finished X" or "regenerate the garden export" is one sentence, not a procedure I have to re-explain.

### Cross-session continuity

Sessions persist. I can start work at my desktop CLI, go out, and continue the same thread from Telegram — the agent pulls context from session history instead of making me repeat myself. For someone who thinks in fragments at odd hours, this removed most of the friction from capturing ideas.

## What surprised me

- **Memory beats prompt engineering.** After correcting the agent twice ("use uv, never bare pip"), it just stopped asking. The correction compounds forever.
- **Chat-as-ops is real.** Approving a fix from my phone while away from the desk changed how often maintenance actually happens — from "someday" to immediately.
- **Skills are the leverage point.** Anything I do more than twice becomes a saved procedure, so quality goes up each repetition instead of staying flat.

## Notes

- Everything sensitive stays local: the agent works on-machine, secrets stay out of repos, and only explicitly flagged notes (`publish_external: true`) get synced to my public garden.
- If you want to try this yourself, start with the [Hermes docs](https://hermes-agent.nousresearch.com/docs) — setup is one binary, one config file, and a bot token.
