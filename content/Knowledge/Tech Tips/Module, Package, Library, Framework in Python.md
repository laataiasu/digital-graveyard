---
title: Module, Package, Library, Framework in Python
date: 2025-07-26T23:18:47+07:00
tags:
  - knowledge
  - tips
publish_external: true
---

# 📦 Module, Package, Library, Framework in Python
---

## 🔹 1. Module

A **module** is a single Python file (`.py`) that contains code—functions, classes, variables, etc.

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"
````

You can import this module:

```python
import my_module
print(my_module.greet("Alice"))
```

---

## 🔹 2. Package

A **package** is a collection of modules grouped together in a directory with an `__init__.py` file (can be empty).

```
my_package/
│
├── __init__.py
├── module1.py
└── module2.py
```

You can import like this:

```python
from my_package import module1
```

> **Note:** In modern Python (3.3+), `__init__.py` is optional, but still commonly used.

---

## 🔹 3. Library

A **library** is a broader term—it refers to a **collection of packages and modules** that offer related functionality.

Examples:

* `NumPy` – numerical operations
* `Pandas` – data analysis
* `Requests` – HTTP requests

So a **library** may consist of many **packages**, each with its own **modules**.

---

## 🔹 4. Framework

A **framework** is a more structured collection of libraries designed to help build applications, especially web or GUI ones.

Examples:

* `Django` – web framework
* `Flask` – micro web framework
* `PyTorch` – deep learning framework

> Frameworks are opinionated—they define how you should structure your app.

---

## 🔹 5. Standard Library

This is the **built-in set of modules** that comes with Python. You don’t need to install them.

Examples:

* `os` – interacting with the operating system
* `math` – mathematical functions
* `datetime` – working with dates and times

---

## 🔹 6. Virtual Environment

An **isolated environment** where Python packages are installed. Prevents conflicts between different projects.

```bash
python -m venv myenv
source myenv/bin/activate  # or myenv\Scripts\activate on Windows
```

---

## 🧾 Summary Table

| Term                 | Description                                | Example                |
| -------------------- | ------------------------------------------ | ---------------------- |
| **Module**           | A single `.py` file                        | `math.py`              |
| **Package**          | A folder of modules (with `__init__.py`)   | `mypackage/`           |
| **Library**          | Collection of packages/modules             | `NumPy`, `Pandas`      |
| **Framework**        | Structured toolkit for app development     | `Django`, `Flask`      |
| **Standard Library** | Built-in modules with Python               | `os`, `random`, `json` |
| **Virtual Env**      | Isolated environment for managing packages | `venv`, `virtualenv`   |

---
