---
title: "Claude Code with OpenRouter Custom Models"
date: 2026-08-26
tags: [tech]
publish_external: true
draft: false
---

Claude Code is not locked to Anthropic. The CLI happily talks to any endpoint that speaks the Anthropic Messages protocol, so you can route it through OpenRouter and run whatever model you want — including non-Claude models, or in my case a stealth model (`stealth/ox-alpha`) that I also use as my Hermes brain.

## How it works

Claude Code reads its config from `~/.claude/settings.json`. The whole trick is four environment variables under the `env` key:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://openrouter.ai/api",
    "ANTHROPIC_AUTH_TOKEN": "<your openrouter key>",
    "ANTHROPIC_API_KEY": "",
    "ANTHROPIC_MODEL": "stealth/ox-alpha",
    "ANTHROPIC_SMALL_FAST_MODEL": "stealth/ox-alpha",
    "CLAUDE_CODE_MAX_CONTEXT_TOKENS": "200000"
  }
}
```

What each line does:

- `ANTHROPIC_BASE_URL` — instead of `https://api.anthropic.com`, every request goes to OpenRouter. Note the URL is `openrouter.ai/api` (not `/api/v1`) because OpenRouter exposes an Anthropic-compatible skin at `/api/v1/messages`, and Claude Code appends `/v1/messages` itself.
- `ANTHROPIC_AUTH_TOKEN` — the OpenRouter API key, sent as a Bearer token. `ANTHROPIC_API_KEY` must stay empty so Claude Code doesn't try to use it or trigger OAuth login.
- `ANTHROPIC_MODEL` — the default model for everything interactive.
- `ANTHROPIC_SMALL_FAST_MODEL` — the background model Claude Code uses internally (session titles, autocompletion-ish tasks). I set it to the same model so *everything* routes to one place.
- `CLAUDE_CODE_MAX_CONTEXT_TOKENS` — optional but useful: since the model name is unknown to Claude Code, it can't look up the context window and will nag about auto-compact. This tells it to assume 200k tokens.

## Getting there

1. Install: `npm install -g @anthropic-ai/claude-code`. On Fedora with npm's script-blocking, allow the postinstall first: `npm config set allow-scripts=@anthropic-ai/claude-code --location=user` — otherwise the native binary never downloads and `claude` errors out.
2. Keep the API key out of the settings file if the file might get shared; mine is sourced from `~/.secrets` (`export or="sk-or-v1-..."`) and injected by a small script.
3. Verify: `claude -p "Reply with exactly: OK" --model stealth/ox-alpha` should print just `OK`.

## Caveats

- Claude Code prints `[claude-code:unrecognized_model]` warnings for custom models — harmless. It just doesn't know the model's context window, hence the `CLAUDE_CODE_MAX_CONTEXT_TOKENS` shim above.
- Switching models later is just editing `ANTHROPIC_MODEL` to any OpenRouter slug (`deepseek/deepseek-chat`, `google/gemini-3.6-flash`, etc.) — no proxy needed, OpenRouter translates on their side.
- You pay OpenRouter per-token for whatever model you pick, so this trades Anthropic billing for OpenRouter credits. Free-tier models exist too (`:free` suffix) with rate limits.
