---
date: 1970-01-01T00:00:00Z
---

Cloud Managed
- RDS, DynamoDB, S3
Self-Managed
- EC2 + Postgresql, EC2 + Cassandra, EC2 + Unix FS
Redshift/Teradata Aster/Oracle Exadata/Azure SQL: SQL, Columnar, Massively Parallel
Pada DBMS SQL, biasanya **setiap query** selalu dieksekusi pada **single CPU** dari 1 node  
Dengan Massively Parallel Processing (MPP), 1 query dapat dieksekusi ke **multiple CPU** atau node
### Redshift
SQL, Columnar, Massively Parallel  
Komponen:  
- Leader Node: Koordinasi Compute Nodes, external communication, optimisasi query
- Compute Nodes: Memiliki beberapa slices, cluster dengan n slices dapat memproses n partisi dari table secara simultan
### Optimizing ETL Design
Improving performance untuk query time
### Distribution Styles
- EVEN distribution
    - Round robin load-balancing (membagi row berurutan ke tiap CPU)
    - Drawback: Sulit untuk join karena bisa jadi dimension table dan fact table diproses pada CPU yang berbeda (Shuffling: pindah data antar node pada cluster)
- All distribution
    - Distributing `fact` dengan EVEN, tetapi `dimensions` di load ke semua CPU
    - Tidak ada shuffling
- AUTO distribution:
    - Tergantung redshift
    - Apabila tabel berukuran kecil menggunakan ALL, apabila sebaliknya menggunakan EVEN
- KEY distribution
    - Row dibagi berdasarkan KEY yang sama. Artinya, setiap CPU hanya berisi row dengan KEY yang sama.
    - Drawback: Skewed distribution
### Sorting Key
Diurutkan berdasarkan key dan kemudian round robin seperti EVEN distribution, sehingga memudahkan join
  








































































