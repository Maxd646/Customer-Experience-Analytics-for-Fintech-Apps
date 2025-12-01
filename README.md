# Fintech App – Customer Experience Analytics

A data-driven project designed to analyze real customer feedback for a fintech mobile application using web scraping, text cleaning, and foundational NLP preprocessing.  
This repository follows a modular, production-grade architecture to support scalable analytics in later tasks.

---

## Task 1 – Data Collection & Preprocessing (COMPLETE)

**Objective:**  
Collect user reviews from the Google Play Store, store them in a structured format, and prepare a clean text dataset for downstream NLP tasks such as sentiment analysis, topic extraction, and trend visualization.

---

## Project Structure (Task 1)

```
Fintech-App-Customer-Experience-Analytics/
│
├── configs/
├── docs/
│
├── data/
│   ├── raw/               # Raw scraped reviews
│   ├── interim/           # Temporary/working files
│   ├── processed/         # Cleaned dataset (Task 1 output)
│   └── postgres_exports/
│
├── notebooks/             # Jupyter exploration (future tasks)
│
├── scripts/               # Executable Python scripts
│   ├── scrape_reviews.py  # Scraper (Task 1)
│   └── clean_reviews.py   # Cleaner (Task 1)
│
├── src/
│   └── fintech_app_reviews/
│       ├── scraper/       # Scraping logic
│       ├── preprocessing/ # Text cleaning functions
│       ├── nlp/           # NLP models (Task 2+)
│       ├── db/            # DB integration
│       ├── viz/           # Charts & insights
│       └── utils/         # Helper utilities
│
├── tests/
│   ├── unit/
│   │   ├── test_cleaning.py
│   │   └── test_scraper.py
│   └── integration/
│       └── test_pipeline.py
│
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── init_project.sh
├── .gitignore
└── README.md
```

---

## 🧹 Pipeline Overview

### Scraping

- Reviews collected from a Google Play Store app page.
- `BeautifulSoup` used for lightweight HTML parsing.
- 5 batches/pages scraped.
- Output stored in:  
  `data/raw/reviews_raw.csv`

### Cleaning

- Text normalization steps performed:
  - Lowercasing
  - Removing special characters
  - Removing repeated spaces
  - Stripping whitespace
- Preparing clean text for NLP.
- Output stored in:  
  `data/processed/reviews_clean.csv`

---

## 🛠 How to Run

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run scraper:**

```bash
python scripts/scrape_reviews.py
```

**Run cleaner:**

```bash
python scripts/clean_reviews.py
```

---

## Example Output Preview

**Raw Review:**

```
"Great app!!! Very useful, but sometimes slow…"
```

**Cleaned Text:**

```
great app very useful but sometimes slow
```
