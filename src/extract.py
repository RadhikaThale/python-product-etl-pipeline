import requests
import logging

API_URL = "https://fakestoreapi.com/products"

def extract_data():
    try:
        response = requests.get(API_URL, timeout=30)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            raise ValueError("Expected a list of products")

        logging.info("Extracted %d records", len(data))
        print(f"Extracted {len(data)} records")

        return data

    except requests.RequestException as error:
        logging.exception("API extraction failed")
        raise
