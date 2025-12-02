# Task 3 — Store Cleaned Data in PostgreSQL

## Overview
Persistently store the cleaned and processed review data in PostgreSQL.

## Database Setup
- Install PostgreSQL.
- Create a database named `bank_reviews`.

## Schema
### Banks Table
- `bank_id` (PRIMARY KEY)
- `bank_name`
- `app_name`

### Reviews Table
- `review_id` (PRIMARY KEY)
- `bank_id` (FOREIGN KEY)
- `review_text`
- `rating`
- `review_date`
- `sentiment_label`
- `sentiment_score`
- `source`

## Data Insertion
- Use Python (`psycopg2` or `SQLAlchemy`) to insert data.
- Verify data integrity with SQL queries.

## KPIs
- Tables populated with >1,000 reviews
- Working database connection
- SQL dump/schema file committed

## Output
- PostgreSQL database containing cleaned and structured review data
