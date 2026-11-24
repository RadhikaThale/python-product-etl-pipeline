# Product ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that extracts product data from a REST API, transforms and validates it using Pandas, and loads the processed data into a PostgreSQL database.

## Project Overview

This project demonstrates a complete data engineering workflow using Python, REST APIs, Pandas and PostgreSQL.

## Architecture

```text
Fake Store API
      |
      v
   Extract
      |
      v
  Transform
   (Pandas)
      |
      v
   Validate
      |
      v
    Load
      |
      v
  PostgreSQL
```

## Technologies Used

- Python
- Pandas
- REST API
- JSON
- PostgreSQL
- SQLAlchemy
- Psycopg2
- Pytest
- Git and GitHub

## Features

- Extracts product data from Fake Store API.
- Processes JSON responses.
- Removes duplicate product records.
- Handles missing and invalid values.
- Categorizes products based on price.
- Performs data quality validation.
- Loads product data into PostgreSQL.
- Uses automated tests with Pytest.

## Project Structure

```text
Product-ETL-Pipeline/
|
|-- src/
|   |-- extract.py
|   |-- transform.py
|   |-- load.py
|   |-- pipeline.py
|
|-- tests/
|   |-- test_transform.py
|
|-- data/
|-- logs/
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/RadhikaThale/python-product-etl-pipeline.git
cd python-product-etl-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a database named:

```sql
CREATE DATABASE product_etl_db;
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=product_etl_db
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
```

Do not upload your `.env` file to GitHub.

### 6. Run the ETL pipeline

```bash
python src/pipeline.py
```

## Database Verification

Execute these SQL queries in PostgreSQL:

```sql
SELECT * FROM products;

SELECT COUNT(*) FROM products;

SELECT category, COUNT(*)
FROM products
GROUP BY category;

SELECT AVG(price) FROM products;
```

## Run Automated Tests

```bash
python -m pytest -v
```

## ETL Pipeline Results

The initial successful execution processed 20 product records.

- Extraction: Successful
- Transformation: Successful
- Data validation: Passed
- PostgreSQL loading: Successful

## Future Enhancements

- Incremental data extraction.
- API pagination.
- Automated pipeline scheduling.
- Improved logging and monitoring.
- Data visualization dashboard.
- Docker-based deployment.

## Author

**Radhika Thale**

Computer Engineering Student | Aspiring Data Engineer

GitHub: https://github.com/RadhikaThale
