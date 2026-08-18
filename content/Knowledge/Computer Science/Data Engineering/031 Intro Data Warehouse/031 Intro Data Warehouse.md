---
title: "031 Intro Data Warehouse"
date: 2001-01-01
tags: []
publish_external: false
---

Operational Databases  
Pros: Excellent for operations, no redundancy, high integrity  
Cons: Too slow for analytics, Too hard to understand  
Data Warehouse: subject-oriented, integrated, nonvolatile, time-variant
## DWH pada konteks bisnis:
- Perhatikan setiap requirement
    - Scaling? Apakah single database cukup?
    - Kompleksitas?
    - Tabular data?
    - Apakah perlu performance yang cepat atau bisa fleksibel?
  
  
#### OLTP vs OLAP
| OLTP               | OLAP                             |
| ------------------ | -------------------------------- |
| Transactional  | Analytical                       |
| Performance    | Perlu banyak query/join          |
| No redundancy  | Sulit dipahami                   |
| High integrity | As long as can generate analysis |
  
  
## Fact or Dimension Table
- Fact Table biasanya bersifat **numeric & additive** seperti transaksi, order, dll
- Dimension table biasanya merupakan table penjelasan dari attribute pada fact table seperti, departemen, lokasi, karyawan, waktu, dll.
  
ETL → Dimensional model
Tujuan Data Modelling : Agar mudah dipahami dan fast query → **Star Schema**
Dari normalized/OLTP menuju OLAP
  
  
## Data Warehouse Architecture:
**Kimball**  
Standarisasi untuk setiap fungsi bisnis atau departmen  
**Data mart**
- Setiap departemen memiliki ETL dan dimensional model nya masing-masing
- Bisa menimbulkan inkonsistensi, beda departemen beda data
**Inmon's corporate information factory (CIF)**
- Semua data ditampung terlebih dahulu pada bentuk normal (pada ETL), kemudian tiap departmen load ke dimensional model masing-masing yang dibutuhkannya
**Hybrid (Kimbal + Inmon)**
  
### DWH Architecture
### Kimball's Bus Architecture
All sources -> DWH -> Enterprise DW bus architecture
### Independent Data Marts
The department has independent ETL
### Inmon's Corporate Information Factory (CIF)
All sources -> DWH (3NF) -> Datamart
### Hybrid Kimball Bus & Inmon CIF
All sources -> DWH (3NF) -> Enterprise DW bus architecture
  
### OLAP Cubes
Roll-Up: City to Country (Makin simpel)  
Drill-Down: Country to City (Makin banyak)  
Slice: Where City="WHAT"  
Dice: Where City="WHAT" and Month in ["WHAT", ...] and Branch in ["WHAT", ...]  
GROUP by CUBE(movie, branch, month): kombinasi aggregasi dari semuanya, misalnya total, total by movie branch month, total by movie branch, total by movie, etc.
  
**MOLAP**: Pre-aggregate OLAP Cubes ke **non-relational database**  
**ROLAP**: _On the fly_ menggunakan SQL biasa
  











































