---
date: 2001-01-01
---

### Kapan butuh NoSQL?
- Perlu High availability
- Memiliki data dengan ukuran besar
- Perlu linear scalability
- Low latency
- Perlu fast reads and write
Pada **distributed database**, agar memiliki **high availability** diperlukan data yang tersebar atau diperlukan banyak copy dari data
**Eventual Consistency**: Consistency model pada **distributed** computing untuk mencapai **high availability (AP)**. Apabila tidak ada update pada suatu item, maka akses ke item tersebut akan mengembalikan update item terakhir kali.
  
### CAP (Consistency, Availability, Partition Tolerance) Theorem
Trilema
Consistency: Setiap read mengembalikan item terbaru yang benar atau error
Availability: Setiap request diterima dan response dikirim (meskipun data yang dikirim tidak update)
Partition tolerance: Sistem tetap berjalan meskipun ada node yang mati atau gangguan lainnya seperti gangguan network etc.

[![[cap-theorem.jpg]]](https://facingissuesonitcom.files.wordpress.com/2020/02/cap-theorem.jpg?w=1000)
  
## Apache Cassandra
- Perlu **Denormalization** untuk mencapai fast reads, karena tidak ada **JOINS**
- Optimized untuk fast reads
### Primary Key
- Unique
- Hashing pada nilai PK ini mengakibatkan penempatan ke node tertentu pada sistem
- Data distibuted melalui partition key ini
- Simple atau Composite
### Clustering Columns
- Sort data DESC order
  

























