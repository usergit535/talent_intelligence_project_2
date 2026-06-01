# Talent Intelligence Scraper Pipeline

An automated, asynchronous cloud-deployed data extraction engine designed to discover high-growth corporate entities across 4 distinct job networks, analyze real-time hiring metrics, enrich corporate social intelligence vectors, and export deduplicated, validated documentation models.

---

## 🚀 Key Features

* **Dynamic Source Discovery:** Orchestrates multi-network sweeps to index live entity listings.
* **Playwright Core Integration:** Runs resilient, headless Chromium browser sessions mimicking human behaviors using random user-agent rotations.
* **Multi-Layer Enrichment Pipeline:**
  * **Stage 1 (Hiring Status):** Audits career portals to map real-time hiring posture.
  * **Stage 2 (Social Graph):** Extracts and maps company tracking profiles across major platforms.
* **Deduplication Engine:** Formats, sanitizes, and cleans overlapping corporate datasets seamlessly.
* **Dual Format Exports:** Automatically builds corporate document sheets (`.xlsx`) and data payloads (`.json`).
* **CI/CD Cloud Automation:** Powered by GitHub Actions to execute independently daily via headless virtual environments.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.10+
* **Automation Frame:** Playwright (Headless Chromium Core)
* **Data Layer:** Pandas, Openpyxl (Excel Sheet Compilers)
* **Networking:** Requests
* **Orchestration:** GitHub Actions Workflow Engine

---

## 📁 Repository Structure

```text
talent_intelligence_project_2/
├── .github/
│   └── workflows/
│       └── scraper.yml         # CI/CD Cloud Automation Workflow configuration
├── config/
│   ├── __init__.py
│   └── config.py               # Framework timeouts, agents, and configuration
├── scraper/
│   ├── __init__.py
│   ├── company_discovery.py    # Crawling module across 4 networks
│   ├── hiring_checker.py       # Career portal status tracking
│   ├── social_media_finder.py  # OSINT corporate profile discovery
│   ├── data_exporter.py        # Validation and multi-format exporter
│   └── logger.py               # Consolidated tracking system
├── output/                     # Generated cloud assets directory (Git Ignore Overridden)
│   ├── companies.xlsx          # Compiled target spreadsheet
│   └── companies.json          # Formatted JSON payload
├── main.py                     # Master execution pipeline loop
├── requirements.txt            # Operational library configurations
└── .gitignore                  # Development isolation mappings