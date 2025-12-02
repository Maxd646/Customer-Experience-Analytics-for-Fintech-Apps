# Task 2 — Sentiment and Thematic Analysis

## Overview
Analyze the reviews collected in Task 1 to identify customer sentiments and recurring themes.

## Sentiment Analysis
- Use `distilbert-base-uncased-finetuned-sst-2-english` or simpler libraries like VADER/TextBlob.
- Compute sentiment scores (positive, negative, neutral).
- Aggregate by bank and rating.

## Thematic Analysis
- Extract keywords and n-grams (TF-IDF, spaCy).
- Cluster into 3–5 themes per bank:
  - Account Access Issues
  - Transaction Performance
  - User Interface & Experience
  - Customer Support
  - Feature Requests

## Pipeline
- Tokenization, stop-word removal, lemmatization
- Save results as CSV (`review_id, review_text, sentiment_label, sentiment_score, identified_theme(s)`)

## KPIs
- Sentiment scores for 90%+ reviews
- 3+ themes per bank
- Modular pipeline code

## Output
- Cleaned, analyzed CSV dataset ready for PostgreSQL storage in Task 3
