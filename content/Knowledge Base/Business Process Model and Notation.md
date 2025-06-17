---
date: 1970-01-01
---

Camunda **does not natively support "code-as-diagram" syntax like Mermaid**, where you write textual code and automatically render a diagram. Camunda BPMN diagrams are typically created using **drag-and-drop graphical tools**, such as:

* **Camunda Modeler** (official desktop app)
* **Camunda Web Modeler** (in Camunda Platform 8)

---

### ✅ What Camunda Does Support:

* **BPMN 2.0 XML**: You can write or edit BPMN diagrams as XML (machine-readable), which Camunda engines interpret and execute.
* **Modeler UI**: Create diagrams visually, then export to BPMN XML.
* **Camunda Platform 8**: Integrates with tools like Zeebe and offers better cloud-native workflow modeling.

---

### ❌ What Camunda Does Not Support:

* No native support for **text-based modeling like Mermaid.js**, PlantUML, or YAML/DSL to BPMN translation.
* You can't write something like:

  ```mermaid
  graph TD
    A(Start) --> B[Place Order]
    B --> C{Payment Success?}
    C -- Yes --> D[Send Confirmation]
    C -- No --> E[Display Error]
    D --> F(End)
    E --> F
  ```

---

### 🔁 Workarounds / Alternatives

If you're looking for **text-to-diagram workflows** and want to integrate with BPM tools:

* ✅ **Mermaid + Camunda (indirect)**:

  * Use Mermaid for **lightweight visualization**.
  * Translate manually or semi-automatically into BPMN XML for Camunda.

* ✅ **BPMN Sketch Miner**:

  * Generates BPMN diagrams from structured natural language.
  * Output can be converted into BPMN for Camunda.

* ✅ **Custom DSL → BPMN converters**:

  * Some teams create domain-specific languages or scripts that compile into BPMN XML for execution.

---

### Summary

| Feature                    | Mermaid           | Camunda |
| -------------------------- | ----------------- | ------- |
| Text-based diagramming     | ✅                 | ❌       |
| Executable workflow engine | ❌                 | ✅       |
| BPMN 2.0 standard          | ❌ (not supported) | ✅       |

---

Would you like help with a Mermaid-to-Camunda conversion or recommendations on combining both styles in your workflow?
