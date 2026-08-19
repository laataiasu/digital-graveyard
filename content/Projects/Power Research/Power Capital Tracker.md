---
title: "Power Capital Tracker"
date: 2026-05-19
tags: [project]
publish_external: false
---

## 🧱 “Power Capital Tracker”

### 🔍 1. **Start With Institutions (VCs & Investment Firms)**

| Type                                   | Where to Find                                                                        |
| -------------------------------------- | ------------------------------------------------------------------------------------ |
| [[Venture Capital]]                    | AC Ventures, East Ventures, Alpha JWC, Intudo, Skystar                               |
| [[Private Equity]] / [[Family Office]] | Saratoga Investama, Northstar Group, TBS Energi, Triputra, Falcon House              |
| [[State Capital]]                      | INA (Indonesia Investment Authority), Telkomsel Ventures, BUMN incubators, Danantara |

➡️ For each, get:

- Partner names
    
- Founder bios
    
- Shareholding structure
    
- Investment portfolio
    

---

### 📚 Public Sources to Extract From ([[Data Sources]])

| Source                                        | Data You Want                                 |
| --------------------------------------------- | --------------------------------------------- |
| **Indonesia Stock Exchange filings (Emiten)** | Who owns investment holding companies         |
| **AHU.go.id / ProfilBisnis**                  | Legal entity structure, ownership             |
| **LinkedIn**                                  | Who’s who in VC / PE firms                    |
| **Crunchbase / Tracxn**                       | Startup–VC mappings                           |
| **Tempo, Katadata, DealStreetAsia**           | Political-business ties, public announcements |
| **Pitchbook (if accessible)**                 | Cross-check investment histories              |
| **KPU / LHKPN**                               | Check if investor is also a politician        |
| **DPR.go.id**                                 | Look for business affiliations of MPs         |

---

### 🧠 2. ENTITY ENRICHMENT: From Firm → People → Networks

Example: **Northstar Group**

- Co-founder: Patrick Walujo
    
- Board: Gojek, Tiket, Bank Jago
    
- Family ties: Connected to Sandiaga Uno (via Saratoga/Recapital)
    
- Political links: Recapital → PAN, PPP circles
    

---

### 🕸️ 3. MAP THE RELATIONS

For each entity:

```json
{
  "person": "Patrick Walujo",
  "role": "Co-founder, Northstar",
  "investments": ["Gojek", "OVO", "Bank Jago"],
  "family_ties": ["Sandiaga Uno"],
  "connections": ["Recapital", "Saratoga", "PAN"]
}
```

Then link with:

- **Political party (if any)**
    
- **State contracts / BUMN ties**
    
- **Regulatory influence**
    
- **Philanthropy / CSR (e.g., Tzu Chi, Yayasan)**
    

---

### 🧰 TOOLS TO SPEED YOU UP

|Task|Tool|
|---|---|
|Scraping LinkedIn, company pages|`Selenium`, `Playwright`, `SerpAPI`|
|Entity extraction from articles|`spaCy`, `Haystack`, `LangChain`|
|Data linking / deduplication|`FuzzyWuzzy`, `Levenshtein`, `Neo4j`|
|Visual mapping|`NetworkX`, `Neo4j`, `Gephi`|
|Database|SQLite for local, PostgreSQL for scale|

---

### 🧭 Suggest Starting From:

|Direction|Seed Entity|
|---|---|
|🇮🇩 Local VC|East Ventures → Willson Cuaca, Batara Eto|
|🎩 Elite Capital|Northstar, Recapital → Patrick Walujo, Sandiaga Uno|
|📱 Tech Dynasties|Gojek, Tokopedia, Akulaku → check investor profiles|
|🏛️ BUMN Incubators|Telkomsel Ventures, MDI Ventures, INA|
|💼 Politicians-Turned-Investors|Erick Thohir, Sandiaga, Luhut family businesses|

---

## 🔥 If You Had Just 1 Weekend

You could:

- Build a CSV like:
    

```csv
person,firm,role,investments,political_links,source
Patrick Walujo,Northstar,Founder,"Gojek, OVO",Sandiaga Uno,https://...
```

- Parse this into a graph (NetworkX or Neo4j)
    
- Visualize key clusters: VC capital ↔ tech ↔ politics
    

---

Would you like me to now:

1. Generate a **starter dataset** of 20 key Indonesian capital holders?
    
2. Write the script to build & visualize their relationship graph?
    
3. Help design an enrichment pipeline (e.g., auto-search articles for links)?
    

You name it -- I’ll code it.
