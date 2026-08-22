---
title: "044 Introduction to Data Lakes"
date: 2001-01-01
tags: [note]
publish_external: true
---

**Schema-On-Read**: analysis tanpa predefined schema
Spark memungkinkan Schema-On-Read dengan abstraksi RDD DataFrame atau SQL
Data lake merupakan evolusi data warehouse dimana:
- Format data yang bervariasi
- Perlu explorasi dan analytics lebih lanjut seperti ML, Graph Analytics, dan Recommender Systems
Awalnya data lake hanya dimplementasikan melalui hadoop ecosystem, yaitu dengan HDFS, Hive, Pig, Impala, dan Spark.
Data diletakkan as-is, baru kemudian di transform: **ELT **
Columnar Storage menggunakan **parquet** tanpa MPP databases yang mahal
**MLib** dan **Graphx** untuk advanced analytics

### Data Lake Issues
- Data garbage dump
- Hard data governance
- data lake should replace, offload or work in parallel with data warehouse or data marts?
  
  
![[Untitled.jpeg]]























