---
title: "Power Research"
date: 2026-05-19
tags: []
publish_external: false
---

Indonesia (and many Global South countries) lacks an equivalent to [LittleSis](https://littlesis.org/)--a public accountability platform that maps the power structures of elites: who knows who, who funds whom, which family is behind what conglomerate, and how influence flows across business, politics, military, media, etc.

To approach this, let's break it down into 3 layers:

---

### ⚙️ SYSTEM DESIGN: "Power Research Indonesia"

---

#### 1. **Purpose & Vision**

> *A public infrastructure to map, track, and analyze the power networks of Indonesia: elites, institutions, influence flows.*

* **Why?**

  * Make elite networks legible to the public.
  * Help journalists, activists, academics, and citizens investigate concentration of power.
  * Enable civic tech, investigative journalism, and public accountability.

---

#### 2. **Core Principle: 80/20 Power Mapping**

> *“Focus on the top 20% of actors that shape 80% of national outcomes.”*

##### Initial Scope:

* Top 200 families/business groups
* Top 300 public officials (executive, legislative, judicial)
* Top 100 institutions (state-owned, regulatory, corporate, religious, media)

> *Use \[Pareto principle] to avoid overwhelming data collection.*

---

#### 3. **System Architecture (Modular)**

| Module                    | Purpose                         | Tools                              |
| ------------------------- | ------------------------------- | ---------------------------------- |
| **Entity Graph DB**       | Store people/orgs + connections | Neo4j / Typesense / PostgreSQL     |
| **Data Pipeline**         | Scrape & update data            | Python + Airflow                   |
| **UI Explorer**           | Web frontend for public access  | Next.js + Tailwind + React-Graph   |
| **Annotation Layer**      | Crowdsourced fact-checks, tags  | Hypothesis / custom                |
| **Audit & Provenance**    | Source traceability             | Markdown + source hash             |
| **Search & Intelligence** | Relationship + NLP summary      | Langchain + GPT backend (optional) |

---

#### 4. **Data Sources**

* Public company disclosures (IDX, OJK)
* KPU, DPR, MA profiles
* Media investigations (Tempo, Tirto, Project Multatuli)
* LHKPN (Wealth declarations)
* Court decisions (PN, MA, MK)
* NGOs (ICW, TII, WALHI)

---

#### 5. **Governance & Sustainability**

* **Stewarded by**: University lab / NGO / civic tech collective (e.g. SAFEnet, KawalKPK)
* **Open data license**: CC-BY-SA / Open Database License
* **Crowdsourcing**: Allow verified user contributions (Wikipedia-style)
* **Funding**: Philanthropy + research grants + donations (a la OpenSecrets / ProPublica)

---

#### 6. **Milestone Strategy**

| Phase                         | Description                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| **P0: Prototype**             | Manually map 50 elite profiles (family tree, political links, business ownerships) |
| **P1: MVP**                   | Graph DB + web UI + crowdsource platform                                           |
| **P2: API layer**             | Enable integration with journalists’ tools, civic dashboards                       |
| **P3: AI-assisted Discovery** | Use NLP to extract relationship info from news, PDFs, court docs                   |

---

#### 7. **Long-Term Goals**

* Track **dynastic politics** and **economic oligarchy**.
* Power literacy curriculum for schools/universities.
* Watchdog for anti-monopoly, corruption, state capture.
* Digital **"genealogy of power"** in Southeast Asia.

---

### 🔧 Example Entity View

* **Name**: Luhut Binsar Pandjaitan
* **Roles**: Coordinating Minister, Ex-Military, Business Owner
* **Connections**:

  * Ganda Group (family ties)
  * Toba Bara Sejahtera (ownership)
  * Erick Thohir (business + political alliance)
  * Jokowi (political network)
* **Mentions**: Tempo (2023 mining corruption), etc.

---

### 🌏 Why Indonesia Needs This

* Oligarchic capitalism is opaque by design.
* Digital colonialism (Facebook/TikTok) is easier to map than local elite networks.
* Citizen power = *understanding where power hides*.

---

Would you be interested in:

* building this kind of platform?
* starting with a smaller version (e.g., top 50 richest + top 100 public officials)?
* joining forces with civic tech folks, UI researchers, or NGOs?

Let me know, and I can help you sketch the **MVP product plan** or find open data sources to start.

---

Yes, **if you were the government**, things would be vastly easier. You’d have privileged access to:

* **first-party data** from:

  * Dukcapil (population registry)
  * Ditjen Pajak (tax declarations)
  * LHKPN (asset declarations)
  * KPU (election candidates)
  * AHU & OSS (company ownership & beneficial owners)
  * Police, Courts, Ministry of Law (legal histories)
  * BSSN or Kominfo (digital footprints)

But since you are not (yet) in government, you’re on the **outside** -- working with **fragmented, opaque, often outdated or low-trust secondary data**.

---

## 🛠️ Strategy When You’re Not in Power (Yet)

Instead of giving up, here’s a systems-thinking design you can follow:

---

### 🧩 1. **Treat the Government Itself as the System to Hack**

Build a “shadow” version of **One Data Indonesia**, not by replicating it 1:1, but by focusing on **power-relevant surfaces** (relationships, assets, ownership, appointments, etc.).

This means:

* Less about full population data
* More about elite actors, dynasties, networks of control

---

### 🪶 2. **Crowdsource + Infer Missing Data**

Use **triangulation**:

* No LHKPN? → Use media reports + SIPP + past positions.
* No family tree? → Use obituary data + Wikipedia + Kompas + genealogy forums.
* No shareholder breakdown? → Infer from indirect holdings via corporate registry scraping.

> **80/20 rule:** Get 80% of the picture from 20% of the effort using public, weakly-structured data.

---

### 🕸️ 3. **Design with a Soft Infrastructure Mindset**

Don’t try to fight the whole state bureaucracy. Build *soft power infrastructure*:

* **Civil society-first**: Empower journalists, researchers, students, activists.
* **Mirror power**: Force accountability by surfacing patterns.
* **Push policy change**: Once critical mass of visibility is reached, government may respond (see how KPK was pressured into digitizing LHKPN).

---

### 🔍 4. **Prototype: Small Unit of Analysis**

Don’t go national. Go **deep on one city**, **one ministry**, **one dynastic family**, or **top 100 public officials**.

Then:

* Publish it well.
* Open the database/API.
* Create “power profiles” like political Top 40 charts.

---

### 🔒 5. **Option: Infiltrate Instead of Compete**

If you really want the **first-party data**, then consider:

| Strategy                           | Role                                                  |
| ---------------------------------- | ----------------------------------------------------- |
| **Become insider**                 | Join Bappenas, KPK, Kemenkeu, or BPS                  |
| **Build think tank**               | Partner with UI, LPEM-FEUI, or CSIS for elite mapping |
| **Public-private data initiative** | Convince Gov to open parts of AHU, LHKPN, OSS         |
| **Academic cover**                 | Launch a research center on “Power and Policy Graphs” |

---

## 🌱 Long-Term System Design (5–10 Years)

| Time Horizon | System Element                                                     | Goal                                    |
| ------------ | ------------------------------------------------------------------ | --------------------------------------- |
| Now–1 yr     | Prototype elite graph                                              | Build minimum viable graph of power     |
| Year 1–3     | Publish shadow “One Power” data                                    | Enable journalists & watchdogs          |
| Year 3–5     | Pressure for open beneficial ownership & elite declaration systems | Policy shift                            |
| Year 5–10    | Merge into real One Data system / civic intelligence unit          | Influence institutional data governance |

---

## 🧠 Bonus: Mental Models

* **“Who benefits?”** → Cui bono (map benefit networks)
* **“Follow the money”** → Use procurement + corporate registry + political donation data
* **“Power = Relationships + Control over Resources”** → Always link people, institutions, wealth

---

Would you like help starting a **micro version** of this?
Maybe we can:

* Build an elite graph of the **2024 top presidential campaign donors**
* Map **5 most powerful dynasties** in Indonesia with sources
* Design a “Power Tracker” UI (like LittleSis or InfluenceMap)

Let’s make this real, even if we don’t have the government badge yet.


[[Power Capital Tracker]]
