import pandas as pd

def transform_data(raw_data):

    df = pd.json_normalize(raw_data)

    df = df[
        ["id", "title", "price", "category",
         "rating.rate", "rating.count"]
    ].copy()

    df.columns = [
        "product_id", "title", "price", "category",
        "rating_rate", "rating_count"
    ]

    df = df.drop_duplicates(subset=["product_id"])

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["rating_rate"] = pd.to_numeric(
        df["rating_rate"], errors="coerce"
    )
    df["rating_count"] = pd.to_numeric(
        df["rating_count"], errors="coerce"
    )

    df = df.dropna(
        subset=["product_id", "title", "price", "category"]
    )

    df = df[df["title"].astype(str).str.strip() != ""]
    df = df[df["price"] >= 0]

    df["rating_rate"] = df["rating_rate"].fillna(0)
    df["rating_count"] = df["rating_count"].fillna(0)

    df["price_category"] = df["price"].apply(
        lambda x: "Budget" if x < 50
        else "Mid-Range" if x < 150
        else "Premium"
    )

    return df


def validate_data(df):

    if df.empty:
        raise ValueError("No valid records found")

    if df["product_id"].duplicated().any():
        raise ValueError("Duplicate product IDs found")

    if df["title"].isna().any():
        raise ValueError("Missing product titles")

    if df["price"].isna().any():
        raise ValueError("Missing prices")

    if (df["price"] < 0).any():
        raise ValueError("Negative prices found")

    if df["category"].isna().any():
        raise ValueError("Missing categories")

    print("All data quality checks passed!")

    return True
