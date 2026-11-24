import logging
from pathlib import Path

from extract import extract_data
from transform import transform_data, validate_data
from load import load_data

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():

    try:
        print("\nStarting Product ETL Pipeline\n")

        print("STEP 1: Extracting data...")
        raw_data = extract_data()

        print("\nSTEP 2: Transforming data...")
        transformed_data = transform_data(raw_data)

        print("\nSTEP 3: Validating data...")
        validate_data(transformed_data)

        print("\nSTEP 4: Loading data...")
        load_data(transformed_data)

        print("\nETL PIPELINE COMPLETED SUCCESSFULLY!")

    except Exception as error:
        logging.exception("ETL pipeline failed")
        print(f"\nPipeline failed: {error}")
        raise

if __name__ == "__main__":
    run_pipeline()
