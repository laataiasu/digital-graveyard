---
date: 1970-01-01
---

# Temporal

## Overview

**Temporal** is considered a [[Distributed Systems]] because it is architected to coordinate **long-running, fault-tolerant workflows** across multiple machines in a reliable and scalable way. Here's a breakdown of **why Temporal qualifies as a distributed system**:

---

### ✅ 1. **Multiple Components Running Across Nodes**

Temporal is composed of several components:

* **Frontend service** (handles gRPC requests)
* **History service** (maintains workflow state)
* **Matching service** (schedules tasks to workers)
* **Worker service** (executes application logic)
  These services are typically deployed across different machines or containers, forming a distributed system.

---

### ✅ 2. **Workflow Execution is Distributed**

Workflows in Temporal:

* Are stateful, long-lived (minutes to months)
* Execute across different **worker processes**, which can be on different machines
* Survive worker crashes and resume elsewhere

This requires **distributed coordination**.

---

### ✅ 3. **Resilient and Fault-Tolerant**

Temporal ensures:

* **Durability** through persistent storage (e.g., Cassandra, MySQL, Postgres)
* **Failover** and **retry** mechanisms for tasks
* **Deterministic replay** of workflow history to recover state

These features require a distributed architecture to achieve high availability and fault isolation.

---

### ✅ 4. **Horizontal Scalability**

You can scale each component of Temporal independently:

* Add more workers to handle more tasks
* Add more frontend or history nodes to handle more workflows

Scalability across machines = distributed system.

---

### ✅ 5. **Communication via Network Calls**

Temporal services and workers communicate via gRPC over the network—another hallmark of a distributed system.

---

### In Summary:

> **Temporal is a distributed system** because it consists of multiple services running on different nodes, coordinating over a network to execute and manage workflows reliably, with fault-tolerance, persistence, and scalability.

---


## Idempotency In Temporal

Temporal **ensures [[Idempotency]] automatically** by:

* Replaying deterministic workflow code
* Not re-executing side effects (e.g., activities) unless marked as retryable
* Letting you manage external side effects with **activity retries and versioning**

This is one reason why Temporal workflows are **reliable and fault-tolerant**.

## Concurrency in **Temporal**

Temporal provides **safe [[Concurrency]]**:

* Multiple workflows can run in parallel
* Workflows themselves are **single-threaded and deterministic**
* Activities (external tasks) can run in parallel or be throttled
* Signals and queries can be sent concurrently to workflows

This lets you build systems that **scale**, **recover from failure**, and **remain consistent**.

## [[Asynchrony]] in **Temporal**

Temporal is **inherently asynchronous**:

* **Workflows** can call activities **asynchronously**, allowing parallel execution.
* **Timers**, **signals**, and **child workflows** are non-blocking.
* Even though workflows look synchronous (sequential code), Temporal **asynchronously manages state, retries, and execution under the hood**.

#### Example (pseudo-code):

```python
# Sequential but non-blocking: runs in parallel
a = await workflow.execute_activity(send_email)
b = await workflow.execute_activity(log_to_audit)
```

Even though this looks linear, Temporal can run the activities **in parallel** behind the scenes.

---

## [[Determinism]] in **Temporal**

Temporal **replays workflow code** from event history to restore state after restarts or crashes. To make this possible:

* **Workflow code must be deterministic**
* **Non-deterministic behavior (e.g., `Date.now()`, random numbers, external calls)** must be isolated inside **Activities**, not inside workflows

#### ✅ Good (Deterministic) Workflow Example:

```python
# This is safe: uses fixed inputs
result = await workflow.execute_activity(add, 3, 5)
```

#### ❌ Bad (Non-deterministic) Workflow Example:

```python
# BAD: result changes on every replay!
now = datetime.now() 
```

Instead, you should:

```python
# GOOD: use Temporal APIs for time
now = workflow.now()
```

---

### 🧠 How Temporal Enforces Determinism

* It **records a history** of all events (activity calls, timers, signals, etc.)
* When recovering, it **re-executes** the workflow code **from the beginning**, using that history to ensure behavior matches exactly
* Any divergence = **non-determinism error**

---

### 💡 Key Sources of Non-Determinism to Avoid

* Current time (`datetime.now()`)
* Randomness (`random()`)
* External API calls
* Multithreading and shared state
* Switch/case on dynamic values

---

### 🔐 How to Stay Deterministic

* Use Temporal’s built-in APIs (`workflow.now()`, `workflow.uuid4()`)
* Keep side-effects in **Activities**, not in the workflow code
* Don’t use global mutable state inside workflows
* Avoid concurrency inside workflows (Temporal executes them single-threaded)

---

### Summary

| Feature           | Deterministic Workflow | Non-Deterministic Workflow |
| ----------------- | ---------------------- | -------------------------- |
| ✅ Reliable replay | ✅                      | ❌                          |
| ✅ Safe retrying   | ✅                      | ❌                          |
| ✅ Debuggable      | ✅                      | ❌                          |

---


## **Workflow** in Temporal?

A **workflow** in Temporal is a **deterministic, stateful function** that orchestrates the execution of **activities** (units of external work), **timers**, **child workflows**, and **signals/queries** over **time**—possibly running for **minutes to months** while handling **failures, retries, and restarts** automatically.

---

### 🧠 Core Properties of Temporal Workflows

| Property                  | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| **Deterministic**         | Must always produce the same result when replayed       |
| **Durable**               | State is persisted to survive crashes/restarts          |
| **Fault-tolerant**        | Automatically restarts after worker failure             |
| **Event-driven**          | Can respond to signals, timers, and external events     |
| **Orchestration-focused** | Coordinates multiple async tasks (activities/workflows) |

---

### 📦 What Workflows Can Do

* Call and coordinate **activities** (e.g., send email, process payment)
* Sleep/timer logic without blocking resources
* Wait for **external signals**
* Spawn **child workflows**
* Handle retries, versioning, cancellations
* Maintain **business state** over time

---

### 🧱 Workflow Structure (High-Level)

```python
# Python SDK Example (simplified)
@workflow.defn
class MyWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        result = await workflow.execute_activity(send_email, name)
        await workflow.sleep(3600)  # wait 1 hour
        return f"Workflow completed for {name}"
```

Or in **Java**:

```java
@WorkflowInterface
public interface MyWorkflow {
    @WorkflowMethod
    String run(String name);
}
```

---

### 🚀 Workflow Lifecycle

1. **Started** by a client or parent workflow
2. **Executes** workflow code
3. Calls **activities** asynchronously
4. May sleep, wait for signals, etc.
5. **Completes**, **fails**, or is **cancelled**
6. Execution history is recorded and can be **replayed** at any time

---

### ⚠️ Workflow Best Practices

✅ DO:

* Use Temporal APIs: `workflow.now()`, `workflow.sleep()`
* Keep workflows deterministic
* Keep workflows orchestration-only (business logic in **activities**)

❌ AVOID:

* Non-deterministic calls (`random()`, `datetime.now()`, external API calls)
* Blocking I/O (use async)
* Long-running operations inside the workflow (use **activities** instead)

---

### 💡 Workflow vs Activity

| Feature   | Workflow                       | Activity                        |
| --------- | ------------------------------ | ------------------------------- |
| State     | Durable, replayed              | Stateless, not replayed         |
| Execution | Single-threaded, deterministic | Can be parallel, arbitrary code |
| Retry     | Orchestrated by Temporal       | Controlled via retry policy     |
| Use Case  | Orchestration                  | Actual work (I/O, DB, APIs)     |

---

## Process Orchestrator, Spring Batch Application, and Microservices Architecture 



### 🧩 1. **Process Orchestrator**

#### 💡 What It Is:

A **Process Orchestrator** is a centralized system that **manages, coordinates, and controls** the execution of multiple services, tasks, or processes in a defined sequence.

#### 🔧 Examples:

* **Temporal**
* **Camunda**
* **Apache Airflow**
* **AWS Step Functions**

#### ✅ Strengths:

* **Visual and logical orchestration** of tasks
* Handles **retries**, **timeouts**, **failures**, and **dependencies**
* Long-running workflows supported
* Easy to **monitor and audit process flows**

#### 🧠 Ideal For:

* Complex **business workflows**
* Coordinating across **multiple services**
* **Stateful**, long-lived flows (e.g., order fulfillment, onboarding)

---

### 🧪 2. **Spring Batch Application**

#### 💡 What It Is:

A **Spring Batch Application** is a Java-based framework for building **batch processing jobs** — often used for data transformation, ETL, or large-volume processing.

#### 🔧 Key Features:

* Job steps with readers, processors, writers
* Retry, skip, and restart mechanisms
* Handles large data volumes
* Runs in-memory or can be persisted

#### ✅ Strengths:

* Optimized for **throughput-heavy** jobs
* Mature ecosystem, integrates with Spring Boot
* Declarative and configurable

#### 🧠 Ideal For:

* **ETL jobs**, database migrations
* **File processing**, report generation
* Scheduled data processing (e.g., every night at 2 AM)

---

### 🧱 3. **Microservices Architecture**

#### 💡 What It Is:

An architectural style where an application is broken down into **small, independent services** that communicate over a network (usually via HTTP or messaging).

#### 🔧 Characteristics:

* Each service owns its **own database and logic**
* Services are **deployed independently**
* Communication via REST, gRPC, messaging (Kafka, RabbitMQ)

#### ✅ Strengths:

* **Scalability** (scale each service independently)
* **Resilience** (failures isolated to services)
* **Flexibility** in tech stack per service

#### 🧠 Ideal For:

* Large-scale applications with **distributed teams**
* Need for **high agility**, frequent deployments
* Applications with **bounded contexts**

---

### 🔍 Head-to-Head Comparison

| Feature                   | Process Orchestrator       | Spring Batch Application            | Microservices Architecture            |
| ------------------------- | -------------------------- | ----------------------------------- | ------------------------------------- |
| Primary Use Case          | Long-running workflows     | High-throughput data processing     | Distributed, independent services     |
| Handles State             | ✅ Yes                      | ⚠️ Partially (with job persistence) | ❌ Each service must manage its own    |
| Parallelism / Concurrency | ✅ Built-in                 | ✅ Step-level parallelism            | ✅ Per service                         |
| Error Handling / Retries  | ✅ Built-in                 | ✅ Configurable                      | ❌ Must be implemented in each service |
| Best for Orchestration    | ✅ Yes                      | ❌ No                                | ⚠️ Requires manual implementation     |
| Long-Running Tasks        | ✅ Yes                      | ❌ No (typically short-lived jobs)   | ❌ Requires careful design             |
| Workflow Visualization    | ✅ Yes (with tools like UI) | ❌ No                                | ❌ No built-in                         |

---

### 🔧 How They Can Work Together

* Use **Spring Batch** inside a **microservice** to perform batch jobs
* Use a **Process Orchestrator** to coordinate multiple microservices or Spring Batch jobs
* Combine **Temporal** with microservices to make fault-tolerant, distributed workflows

---

#### ✅ Recommendation by Use Case

| Use Case                           | Best Choice                               |
| ---------------------------------- | ----------------------------------------- |
| Order processing across services   | **Process Orchestrator (e.g., Temporal)** |
| Nightly ETL job                    | **Spring Batch**                          |
| Building an e-commerce platform    | **Microservices Architecture**            |
| Customer onboarding with approvals | **Process Orchestrator**                  |
| Migrating millions of records      | **Spring Batch**                          |

