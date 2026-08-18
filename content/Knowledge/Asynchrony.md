---
title: "Asynchrony"
date: 2001-01-01
tags: []
publish_external: false
---

### ⚙️ What is **Asynchrony**?

**Asynchrony** refers to **executing operations without waiting for them to complete** before moving on to the next task. It allows a program or system to remain responsive and efficient, especially during **slow or blocking operations** like I/O, network requests, or long computations.

---

### 🧠 Asynchrony vs. Concurrency

| Concept                                                                                                     | Description                                                                  |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **[[Concurrency]]**                                                                                             | Multiple tasks progress independently (can be async or sync)                 |
| **Asynchrony**                                                                                              | Tasks don't block the thread while waiting--often event/callback/future-based |
| ✅ They are related but not the same. A system can be asynchronous without being concurrent, and vice versa. |                                                                              |

---

### 🔁 Why Asynchrony Matters in Distributed Systems

In distributed systems (like APIs, microservices, Temporal, etc.), **waiting on network, disk, or external services** is slow. Asynchrony helps by:

* **Improving responsiveness** (don’t block while waiting)
* **Better resource utilization** (use threads/cycles efficiently)
* **Enabling scaling** without needing more threads/processes

---

### 🧱 Common Asynchronous Patterns

* **Futures/Promises** (e.g., `Future`, `CompletableFuture` in Java)
* **async/await** (e.g., Python, JavaScript, C#)
* **Callbacks** (e.g., Node.js, event-driven systems)
* **Message queues & pub/sub** (e.g., Kafka, RabbitMQ)

---

### ✅ Benefits of Asynchrony

* **Non-blocking execution**
* **Better performance under load**
* **Naturally scalable**
* **Improved user experience (UX)** in front-end apps
