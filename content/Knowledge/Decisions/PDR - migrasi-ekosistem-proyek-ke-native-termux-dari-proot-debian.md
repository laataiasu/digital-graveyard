---
title: "PDR: Migrasi Ekosistem Proyek ke Native Termux dari PRoot Debian"
date: 2026-10-03
tags: [decision, pdr]
publish_external: true
status: "pending"
confidence: 9
review_date: "2026-11-03"
---

# Decision: Migrasi Ekosistem Proyek ke Native Termux dari PRoot Debian

**Choice**: Migrasi runtime dan workspace pengembangan langsung ke native Termux Android (bionic libc) meninggalkan PRoot Debian ARM64  
**Confidence Score**: 9 / 10  
**Scheduled Review**: 2026-11-03  
**Status**: pending

## Context & Problem
Meskipun PRoot Debian menyediakan lingkungan Debian yang lengkap di Android, ptrace syscall interception menimbulkan overhead CPU/memori, latensi I/O filesystem, dan konsumsi baterai berlebih. Native Termux berjalan langsung di atas kernel Linux Android dan bionic libc dengan performa native tanpa virtualization overhead.

## Expected Outcome
Performa eksekusi CLI (uv run, pytest), git operations, dan pipeline I/O jauh lebih kencang; konsumsi baterai & RAM Xiaomi 14T Pro lebih hemat; serta automasi background/daemon berjalan lebih stabil tanpa ptrace bottleneck.

## Retrospective Calibration


---
*Logged in iERP Decision Journal.*
