# sales_etl — ETL Pipeline with Python & PostgreSQL

A professional ETL (Extract, Transform, Load) pipeline built with Python and PostgreSQL, following industry best practices for Data Engineering.

---

## About

This project extracts raw sales data from CSV files, applies data quality transformations using Pandas, and loads clean data into a PostgreSQL database. The pipeline is **idempotent** — it can run multiple times without duplicating data.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.14 | Core language |
| Pandas | Data transformation |
| psycopg2 | PostgreSQL driver |
| python-dotenv | Secure credentials management |
| PostgreSQL 15 | Target database |

---

## Project Structure

```
sales_etl/
├── data/
│   ├── raw/          # Input CSV files (never modify)
│   └── processed/    # Transformed data
├── src/
│   ├── extract.py    # Reads CSV, returns DataFrame
│   ├── transform.py  # Cleans and validates data
│   ├── load.py       # Inserts data into PostgreSQL
│   └── pipeline.py   # Orchestrates ETL + logging
├── sql/
│   └── schema.sql    # Database schema definition
├── logs/
│   └── pipeline.log  # Execution logs
├── .env              # Credentials (never commit!)
├── .gitignore
└── requirements.txt
```

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/rolandgarcia/sales_etl.git
cd sales_etl
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure credentials
Create a `.env` file in the project root:
```
DB_HOST=localhost
DB_NAME=sales_etl
DB_USER=your_user
DB_PASSWORD=your_password
```

### 5. Create the database
```bash
psql postgres
```
```sql
CREATE DATABASE sales_etl;
\c sales_etl
```

### 6. Run the schema
```sql
\i sql/schema.sql
```

### 7. Seed reference data
```sql
INSERT INTO customers (name, email) VALUES
('Garcia', 'garcia@email.com'),
('Maria', 'maria@email.com'),
('Joao', 'joao@email.com');

INSERT INTO products (name, price, stock) VALUES
('Produto A', 50.00, 100),
('Produto B', 75.00, 50),
('Produto C', 30.00, 200);
```

---

## How to Run

```bash
python src/pipeline.py
```

Expected output:
```
2026-03-23 03:22:58 - __main__ - INFO - Starting pipeline
2026-03-23 03:22:58 - __main__ - INFO - 9 rows extracted
2026-03-23 03:22:58 - __main__ - INFO - 4 rows transformed
2026-03-23 03:22:58 - __main__ - INFO - 4 rows loaded
```

---

## How the Pipeline Works

```
data/raw/orders.csv
        |
extract.py    -- reads CSV, returns DataFrame
        |
transform.py  -- removes duplicates, fixes types, handles nulls
        |
load.py       -- inserts clean data into PostgreSQL
        |
PostgreSQL (sales_etl database)
        |
logs/pipeline.log
```

### Data Quality — What Transform handles

| Problem | Example | Solution |
|---|---|---|
| Duplicates | order 1001 appears twice | drop_duplicates() |
| Wrong type | quantity = "N/A" | to_numeric(errors='coerce') |
| Null values | status = null | fillna('pendente') |
| Invalid values | date = "data_invalida" | to_datetime(errors='coerce') |

---

## Security

- Credentials stored in `.env` — never hardcoded
- `.env` protected by `.gitignore`
- All SQL queries use parameterized placeholders (`%s`) — protected against SQL Injection
- PostgreSQL connection managed with context manager (`with conn:`) — auto-closes on error

---

## Idempotency

The pipeline uses `ON CONFLICT (id_pedido) DO NOTHING` — running it multiple times always produces the same result in the database. No duplicates, no errors.

---

## Raw Data Format

The pipeline expects a CSV file at `data/raw/orders.csv` with the following columns:

```
id_pedido, customer_id, product_id, quantity, total, status, order_date
```

---

## Author

Roland Garcia
Data Engineer in training — Bootcamp Data Engineering, Week 2
