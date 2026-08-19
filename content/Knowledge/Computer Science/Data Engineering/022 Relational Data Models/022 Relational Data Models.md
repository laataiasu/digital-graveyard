---
title: "022 Relational Data Models"
date: 2001-01-01
tags: [note]
publish_external: false
---

### OLAP VS OLTP
OLAP → analytical
OLTP → transactional
  
### Normalization
Digunakan untuk transactional secara efisien → Mengurangi redundancy dan meningkatkan integrity
- 1NF → semua cell unique dan single values
- 2NF → semua kolom perlu dependen dengan primary key
- 3NF → Tidak ada transitif dependensi
### Denormalization
Digunakan untuk read heavy workloads → Meningkatkan performance untuk read
  
Fact tables: measurements, metrics, or facts dari proses bisnis
Dimension Tables: people, products, place, time untuk untuk menjelaskan fact tables
### Fact and Dimension Tables
- Star Schemas
    - benefit: denormalized, simple query, fast aggregations
    - drawbacks: data integrity, decrease flexibility, simplified
- Snowflake Schemas
    
  
























