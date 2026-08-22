---
title: "Concurrency"
date: 2001-01-01
tags: [note]
publish_external: true
---

### ⚙️ What is **Concurrency**?

**Concurrency** is the ability of a system to handle multiple tasks at the same time. In distributed systems, it means **multiple operations or processes executing independently and potentially in parallel**--either on the same machine (multi-threaded) or across multiple machines (distributed).

---

### 🧠 Concurrency vs. Parallelism

| Concept         | Definition                                                             | Example                                    |
| --------------- | ---------------------------------------------------------------------- | ------------------------------------------ |
| **Concurrency** | Tasks make progress **independently** (may or may not run in parallel) | A web server handling many client requests |
| **Parallelism** | Tasks actually run **simultaneously** on multiple CPUs                 | Matrix multiplication using multiple cores |

> All parallel programs are concurrent, but not all concurrent programs are parallel.

---

### 🔁 Concurrency in Distributed Systems

In distributed systems (like Temporal, databases, cloud services), concurrency allows:

* **Handling multiple requests** from clients
* **Executing multiple workflows** in parallel
* **Scaling up** to use multiple CPUs/nodes
* **Non-blocking I/O** for better resource use

---

### 🚨 Challenges of Concurrency

1. **Race conditions**
   → Two operations interfere with each other (e.g., two users withdrawing from the same bank account)

2. **Deadlocks**
   → Two or more operations wait on each other indefinitely

3. **Consistency problems**
   → Especially when multiple operations modify shared data

4. **Non-determinism**
   → Harder to test and debug when the execution order changes

---

### 🔐 Tools & Strategies for Managing Concurrency

* **Locks/Mutexes**: Ensure only one process accesses shared data
* **Semaphores**: Control access to a limited number of resources
* **Transactions**: In databases, to ensure atomic and isolated updates
* **Message Queues**: Decouple producers and consumers
* **Workflow engines (e.g., Temporal)**: Manage concurrent execution with built-in control

---
