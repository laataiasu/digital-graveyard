---
title: "PDR: Migrasi Ekosistem Proyek ke Android PRoot"
date: 2026-09-21
tags: [decision, pdr]
publish_external: true
status: "pending"
confidence: 9
review_date: "2026-10-21"
---

# Decision: Migrasi Ekosistem Proyek ke Android PRoot

**Choice**: Jalankan pipeline dan pengembangan beberapa proyek di Android PRoot Debian ARM64 dibanding laptop  
**Confidence Score**: 9 / 10  
**Scheduled Review**: 2026-10-21  
**Status**: pending

## Context & Problem
Penggunaan utama biasanya di laptop, namun konektivitas WiFi laptop seringkali tidak stabil/unreliable. Android (Xiaomi 14T Pro) memiliki konektivitas seluler langsung yang andal dan independen.

## Expected Outcome
Automasi cron, pipeline ETL harian (IDX, Portfolio, iERP), dan sesi coding berjalan stabil tanpa interupsi drop koneksi jaringan.

## Retrospective Calibration


---
*Logged in iERP Decision Journal.*
