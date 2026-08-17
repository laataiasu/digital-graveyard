---
title: "Determinism"
date: 2001-01-01
tags: []
---

### ⚙️ What is **Determinism**?

**Determinism** means that a system or function, given the **same input and starting state**, will always produce the **same output and follow the same execution path**--**no randomness, no surprises**.

---

### 🔁 Why Determinism Matters in Distributed Systems

In distributed systems--especially in **workflow engines like Temporal**--**determinism is essential** for:

* **Replayability**: To recover workflow state after failure by replaying past events
* **Consistency**: Ensuring the same steps are followed every time
* **Debuggability**: Easier to trace, test, and reproduce bugs
* **Fault tolerance**: The system can safely retry or resume after crashes

---
