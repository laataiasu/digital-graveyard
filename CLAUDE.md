# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a **Quartz v4 Static Site Generator** deployment called "Digital Graveyard" — a personal knowledge base/digital garden built from Markdown content (Obsidian-compatible) that transforms into a static HTML website with search, graph visualization, and interactive features.

Based on `@jackyzha0/quartz` v4.5.1.

## Development Commands

```bash
# Local development with hot-reload
npx quartz build --serve

# Production build
npx quartz build

# Type checking + Prettier validation
npm run check

# Auto-format all files
npm run format

# Run tests
npm test
```

## Architecture

Quartz uses a **plugin-based pipeline architecture**:

```
Markdown Files → Transformers → Filters → Emitters → Static HTML
```

### Core Processing Stages

- **`quartz/processors/parse.ts`** — Converts markdown to AST using unified/remark/rehype
- **`quartz/processors/filter.ts`** — Filters content based on plugin criteria
- **`quartz/processors/emit.ts`** — Generates final static files

### Plugin System

Plugins are organized into three types in `quartz/plugins/`:

- **`transformers/`** — Transform content (syntax highlighting, TOC, frontmatter processing, etc.)
- **`filters/`** — Filter content (remove drafts, exclude certain paths)
- **`emitters/`** — Generate output (HTML, assets, RSS, sitemap)

### Entry Points

- **CLI**: `quartz/bootstrap-cli.mjs` — Main CLI using yargs
- **Build**: `quartz/build.ts` — Orchestrates the build pipeline with worker-based parallel processing

## Configuration

- **`quartz.config.ts`** — Main site configuration: title, theme, plugins, analytics, ignore patterns
- **`quartz.layout.ts`** — Component/layout configuration (pages, backlinks, search, graph view)

Key config details:
- SPA rendering enabled
- Wiki-link popovers enabled
- Analytics via Plausible
- Deployment target: GitHub Pages at `laataiasu.github.io/digital-graveyard`
- Ignore patterns: `private`, `templates`, `.obsidian`, `Untags`, `_draft`

## Code Quality

- **TypeScript**: Strict mode enabled, no unused locals/parameters
- **Formatting**: Prettier with 100 character line width, 2-space tabs, semi-colons off
- **Testing**: `tsx` test framework, tests in `quartz/util/*.test.ts`
- **CI**: Multi-OS matrix testing (Windows, macOS, Ubuntu) in `.github/workflows/ci.yaml`

## Tech Stack

- **Language**: TypeScript 5.8.3 (Node.js 22+)
- **Framework**: Preact with JSX (`react-jsx` transform)
- **Build**: esbuild with SCSS (lightningcss)
- **Markdown**: unified + remark + rehype ecosystem
- **Syntax Highlighting**: shiki + rehype-pretty-code
- **Search**: flexsearch (fast full-text search)
- **Visualization**: d3.js (graph view), pixi.js (WebGL visualizations)
- **Math**: KaTeX
- **Worker pool**: Multi-threaded parsing with configurable concurrency

## Content Structure

Source content lives in `/content/` with Obsidian-style markdown:
- Uses frontmatter for metadata (`---` YAML blocks)
- Supports `[[WikiLinks]]` for internal linking
- Organized by topic: `Knowledge/`, `Personal/`, `Projects/`, `Read/`, `Write/`, `Tags/`
- Static assets in `content/assets/`

## Deployment

- **Target**: GitHub Pages
- **Working branch**: `v4`
- **Output directory**: `public/`
- **Auto-deploy**: `.github/workflows/deploy.yml` triggers on push to `v4`

## When Working on This Codebase

- The Quartz core code in `/quartz/` is the framework - **do not modify** unless you understand the plugin architecture
- Most customization happens via plugins in `quartz/plugins/` or config files
- Add new content by editing Markdown in `/content/`
- For new features, prefer creating plugins rather than modifying core processors
- Always run `npm run check` before committing - CI blocks if TypeScript or Prettier fails