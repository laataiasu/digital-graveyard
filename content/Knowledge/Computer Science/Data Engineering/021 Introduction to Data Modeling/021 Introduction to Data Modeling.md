---
title: "021 Introduction to Data Modeling"
date: 2001-01-01
tags: [note]
publish_external: false
---

### Apa itu Data Modelling?
- Organizing elemen dari setiap data dan bagaimana relasi antara setiap data nya
- Untuk mendukung sistem informasi
### Tahapan
- Mengetahui kebutuhan bisnis dan user applications
- Conceptual Data Modelling
- Logical Data Modelling
- Physical Data Modelling
  
### 1. RDBMS
- Database/Schema : Kumpulan dari Table
- Tables/Relation : Kumpulan row dan column
    
    ### ACID Transactions
    
    Atomicity : semua transaksi diproses atau tidak ada yang diproses
    
    Consistency : Perlu ada constraint dan rules saat menuliskan ke database
    
    Isolation : transaction diproses secara independen dan aman, tidak peduli dengan urutannya
    
    Durability : transaksi yang sudah terjadi harus selalu disimpan meskipun sistemnya rusak
    
    ### Jangan menggunakan RDBMS Jika:
    
    - Large amounts of data
    - Perlu berbagai tipe format data
    - Perlu throughput banyak atau fast read
    - Schema yang fleksibel
    - High availability
    - Perlu horizontal scalability : menambah server
    
    Contoh RDBMS : PostgreSQL, Oracle, MySQL, dll
    
  
### 2. NoSQL
- Apache Cassandra (Partition Row Store)
- MongoDB (Document Store)
- DynamoDB (Key-Value Store)
- Apache HBase (Wide Column Store)
- Neo4j (Graph Database)
### Apache Cassandra
- Keyspace (mirip schema), Table, Row
- Partition
  














## ACID


















