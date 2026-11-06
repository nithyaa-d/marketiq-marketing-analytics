
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "raw" / "marketing_campaigns.csv"


def load_campaign_data():
    """Load the generated marketing campaign dataset."""
    assert DATA_FILE.exists(), "Marketing dataset is missing."
    return pd.read_csv(DATA_FILE)


def test_dataset_has_expected_columns():
    df = load_campaign_data()

    expected_columns = {
        "date",
        "campaign_id",
        "channel",
        "region",
        "device",
        "impressions",
        "clicks",
        "leads",
        "conversions",
        "spend",
        "revenue",
    }

    assert expected_columns.issubset(df.columns)


def test_dataset_has_expected_record_count():
    df = load_campaign_data()

    assert len(df) == 5110


def test_dataset_has_no_missing_values():
    df = load_campaign_data()

    assert df.isnull().sum().sum() == 0


def test_dataset_has_no_duplicate_campaign_dates():
    df = load_campaign_data()

    assert not df.duplicated(
        subset=["date", "campaign_id"]
    ).any()


def test_marketing_metrics_are_non_negative():
    df = load_campaign_data()

    numeric_columns = [
        "impressions",
        "clicks",
        "leads",
        "conversions",
        "spend",
        "revenue",
    ]

    assert (df[numeric_columns] >= 0).all().all()


def test_campaigns_have_full_year_of_data():
    df = load_campaign_data()

    df["date"] = pd.to_datetime(df["date"])

    assert df["date"].min() == pd.Timestamp("2025-01-01")
    assert df["date"].max() == pd.Timestamp("2025-12-31")
    assert df["campaign_id"].nunique() == 14

    records_per_campaign = df.groupby("campaign_id").size()

    assert (records_per_campaign == 365).all()
