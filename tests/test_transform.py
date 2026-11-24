import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from transform import transform_data, validate_data


def sample_data():
    return [
        {
            "id": 1,
            "title": "Laptop",
            "price": 100,
            "category": "electronics",
            "rating": {"rate": 4.5, "count": 10}
        },
        {
            "id": 2,
            "title": "Phone",
            "price": 30,
            "category": "electronics",
            "rating": {"rate": 4.0, "count": 5}
        }
    ]


def test_transform_data():
    df = transform_data(sample_data())

    assert len(df) == 2
    assert df.iloc[0]["price_category"] == "Mid-Range"
    assert df.iloc[1]["price_category"] == "Budget"


def test_duplicate_removal():
    raw = sample_data()
    raw.append(raw[0].copy())

    df = transform_data(raw)

    assert len(df) == 2


def test_validation():
    df = transform_data(sample_data())

    assert validate_data(df) is True
