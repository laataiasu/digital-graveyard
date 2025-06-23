---
date: 2001-01-01
---

## Overview

A **distributed system** is a collection of independent computers (nodes or machines) that appears to its users as a single coherent system. These machines communicate and coordinate their actions by passing messages over a network. Distributed systems are used to improve performance, scalability, fault tolerance, and availability.

### Key Characteristics

1. **[[Concurrency]]**: Multiple nodes operate concurrently.
2. **Lack of a global clock**: There’s no single clock across all machines; events must be ordered logically.
3. **Independent failures**: Parts of the system can fail independently.

---

### Examples of Distributed Systems

* **Web services (e.g., Google, Amazon)**
* **Distributed databases (e.g., Cassandra, MongoDB)**
* **Cloud computing platforms (e.g., AWS, Azure)**
* **Blockchain networks**
* **Microservices architectures**

---

### Core Challenges

1. **Latency and Network Failures**
2. **Data Consistency**
3. **Fault Tolerance and Recovery**
4. **Security**
5. **Synchronization**

---

### Types of Distributed Systems

* **Client-Server Systems**
* **Peer-to-Peer Systems**
* **Clustered Systems**
* **Grid Computing**
* **Cloud Computing**

---

### Important Concepts

* **CAP Theorem**: You can only choose two of **Consistency**, **Availability**, and **Partition Tolerance**.
* **Consensus Algorithms**: Paxos, Raft – for reaching agreement in the presence of failures.
* **Replication and Sharding**: Techniques for scaling and fault tolerance.
* **Middleware**: Software that provides communication, security, and coordination between nodes.

[[Idempotency]]
[[Asynchrony]]
[[Determinism]]

## [[Determinism]] vs [[Idempotency]]

### 🔍 **Quick Definitions**

| Concept         | Definition                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Determinism** | An operation always produces the **same result** and takes the **same path** when given the same inputs and state. |
| **Idempotency** | An operation can be **repeated multiple times** without changing the result beyond the first execution.            |

---

### 📦 Example to Illustrate the Difference

#### Imagine an API:

```http
POST /charge-user
```

* If calling it twice charges the user **twice**, it's **not idempotent**.
* If calling it twice charges the user **once**, it's **idempotent**.

Now imagine a **workflow function** that calls this API, and every time it's replayed, it **calls the API with a different timestamp** — that’s **non-deterministic**.

---

### 🔁 Key Differences

| Feature          | **Determinism**                                        | **Idempotency**                                            |
| ---------------- | ------------------------------------------------------ | ---------------------------------------------------------- |
| Focus            | Same input = same behavior                             | Repeated input = same **effect**                           |
| Applies To       | Workflow logic / functions                             | External operations / side effects (e.g., APIs, DB writes) |
| Purpose          | Reliable replay, fault recovery                        | Safe retries, avoiding duplicate side effects              |
| Violated When    | You use random, time, or concurrency in workflow logic | Repeating an API call causes unintended state change       |
| Temporal Concern | Required for workflows                                 | Required for activities & external systems                 |

---

### 🕸 In **Temporal** Terms:

| Workflow Logic (Determinism)              | Activity Side-Effects (Idempotency)            |
| ----------------------------------------- | ---------------------------------------------- |
| Must be **deterministic** to allow replay | Should be **idempotent** to allow safe retries |
| E.g., avoid `random()`, `datetime.now()`  | E.g., avoid charging credit card twice         |

---

### 💡 Analogy

> **Determinism** is like playing a recorded video: if the file is the same, it always plays the same way.
> **Idempotency** is like pressing the elevator button: pressing it once or five times has the same effect.

---

### ✅ Summary Table

| Aspect            | Determinism           | Idempotency                    |
| ----------------- | --------------------- | ------------------------------ |
| Concerned With    | Replaying logic       | Repeating operations           |
| Should Be Used In | Workflow code         | Activities, APIs, side effects |
| Ensures           | Reproducible behavior | Safe retries                   |
| Temporal Enforces | Strictly              | Up to you to implement         |

---

Would you like an example workflow + activity to see both concepts in action?

