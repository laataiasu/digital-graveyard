---
date: 1970-01-01
---

**Idempotency** is a fundamental concept in [[Distributed Systems]], APIs, and fault-tolerant computing. Here's what it means and why it matters:

---

### 🔁 What is Idempotency?

An **operation is idempotent** if **performing it multiple times has the same effect as performing it once**.

#### Example:

```http
POST /charge-customer
```

Without idempotency: charging twice = double charge 💸
With idempotency: charging twice = charged once ✅

---

### 🔧 Why Idempotency is Important in Distributed Systems

In distributed systems (like Temporal, REST APIs, payment systems, etc.), **network failures, retries, and crashes** can cause the same message or request to be processed more than once. Without idempotency, this can result in:

* **Duplicate transactions**
* **Corrupt data**
* **Unexpected side effects**

---

### 🧠 Real-World Examples

| Operation               | Idempotent? | Notes                                          |
| ----------------------- | ----------- | ---------------------------------------------- |
| `GET /users/123`        | ✅           | Reading doesn’t change state                   |
| `DELETE /users/123`     | ✅           | Deleting twice has same effect                 |
| `POST /create-user`     | ❌/✅         | Only idempotent if client provides a unique ID |
| `POST /process-payment` | ❌           | Usually **not** unless designed carefully      |

---

### ✅ How to Ensure Idempotency

1. **Use unique request IDs**:

   * Clients send an `Idempotency-Key` with each request.
   * Server tracks and ignores duplicates.

2. **Store operation status in durable storage**:

   * Persist result the first time.
   * On retry, return the stored result.

3. **Avoid non-deterministic effects**:

   * E.g., sending emails, making payments—wrap with idempotent logic.

---
