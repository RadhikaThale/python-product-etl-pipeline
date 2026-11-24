import os
import logging

from dotenv import load_dotenv
from sqlalchemy import create_engine, text, URL

load_dotenv()

def load_data(df):

    required = [
        "DB_HOST", "DB_PORT", "DB_NAME",
        "DB_USER", "DB_PASSWORD"
    ]

    missing = [key for key in required if not os.getenv(key)]

    if missing:
        raise ValueError(f"Missing database settings: {missing}")

    db_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME")
    )

    engine = create_engine(db_url)

    create_table = """
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        price NUMERIC(10,2) NOT NULL,
        category VARCHAR(100),
        rating_rate NUMERIC(3,2),
        rating_count INTEGER,
        price_category VARCHAR(50),
        extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    insert_query = text("""
        INSERT INTO products (
            product_id, title, price, category,
            rating_rate, rating_count, price_category
        )
        VALUES (
            :product_id, :title, :price, :category,
            :rating_rate, :rating_count, :price_category
        )
        ON CONFLICT (product_id)
        DO UPDATE SET
            title = EXCLUDED.title,
            price = EXCLUDED.price,
            category = EXCLUDED.category,
            rating_rate = EXCLUDED.rating_rate,
            rating_count = EXCLUDED.rating_count,
            price_category = EXCLUDED.price_category,
            extracted_at = CURRENT_TIMESTAMP;
    """)

    try:
        records = df.to_dict(orient="records")

        with engine.begin() as connection:
            connection.execute(text(create_table))
            connection.execute(insert_query, records)

        logging.info("Loaded %d records", len(records))
        print(f"Successfully loaded {len(records)} records")

    except Exception:
        logging.exception("Database loading failed")
        raise

    finally:
        engine.dispose()
