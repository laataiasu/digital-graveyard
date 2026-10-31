---
title: "PDR: Migrasi Ekosistem Proyek ke Native Termux dari PRoot Debian"
date: 2026-10-03
tags: [case-study, review]
publish_external: true
status: "reviewed"
confidence: 9
review_date: "2026-11-03"
---

# Decision: Migrasi Ekosistem Proyek ke Native Termux dari PRoot Debian

**Choice**: Migrasi runtime dan workspace pengembangan langsung ke native Termux Android (bionic libc) meninggalkan PRoot Debian ARM64  
**Confidence Score**: 9 / 10  
**Scheduled Review**: 2026-11-03  
**Status**: reviewed

## Context & Problem
Meskipun PRoot Debian menyediakan lingkungan Debian yang lengkap di Android, ptrace syscall interception menimbulkan overhead CPU/memori, latensi I/O filesystem, dan konsumsi baterai berlebih. Native Termux berjalan langsung di atas kernel Linux Android dan bionic libc dengan performa native tanpa virtualization overhead.

## Expected Outcome
Performa eksekusi CLI (uv run, pytest), git operations, dan pipeline I/O jauh lebih kencang; konsumsi baterai & RAM Xiaomi 14T Pro lebih hemat; serta automasi background/daemon berjalan lebih stabil tanpa ptrace bottleneck.

## Retrospective Calibration
Migrasi ke Native Termux terbukti sukses 100%. Overhead ptrace PRoot tereliminasi total; performa eksekusi I/O git dan Python jauh lebih responsif dengan konsumsi baterai dan RAM yang optimal di Xiaomi 14T Pro. Automasi background daemon berjalan stabil dengan arsitektur standalone.

---
*Logged in iERP Decision Journal.*
