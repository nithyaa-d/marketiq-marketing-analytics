
from pathlib import Path

import numpy as np
import pandas as pd


def generate_marketing_data():
    """Generate reproducible synthetic marketing campaign data."""

    np.random.seed(42)

    channels = {
        "Google Ads": {
            "ctr": 0.045,
            "cpc": 1.80,
            "conversion_rate": 0.085,
            "aov": 120,
        },
        "Facebook Ads": {
            "ctr": 0.032,
            "cpc": 1.20,
            "conversion_rate": 0.065,
            "aov": 95,
        },
        "Instagram Ads": {
            "ctr": 0.038,
            "cpc": 1.40,
            "conversion_rate": 0.055,
            "aov": 90,
        },
        "Email Marketing": {
            "ctr": 0.085,
            "cpc": 0.15,
            "conversion_rate": 0.12,
            "aov": 110,
        },
        "LinkedIn Ads": {
            "ctr": 0.025,
            "cpc": 3.20,
            "conversion_rate": 0.075,
            "aov": 180,
        },
    }

    campaigns = [
        f"CMP_{i:03d}" for i in range(1, 15)
    ]

    regions = ["North", "South", "East", "West"]
    devices = ["Mobile", "Desktop", "Tablet"]

    dates = pd.date_range(
        start="2025-01-01",
        end="2025-12-31",
        freq="D",
    )

    rows = []

    for campaign_id in campaigns:

        channel = np.random.choice(list(channels.keys()))
        metrics = channels[channel]

        for date in dates:

            impressions = int(
                np.random.randint(500, 5000)
            )

            seasonality = (
                1.25 if date.month in [11, 12]
                else 1.0
            )

            clicks = int(
                impressions
                * metrics["ctr"]
                * np.random.uniform(0.75, 1.25)
            )

            clicks = min(clicks, impressions)

            leads = int(
                clicks
                * np.random.uniform(0.20, 0.45)
            )

            conversions = int(
                clicks
                * metrics["conversion_rate"]
                * seasonality
                * np.random.uniform(0.65, 1.35)
            )

            conversions = min(conversions, clicks)

            spend = round(
                clicks
                * metrics["cpc"]
                * np.random.uniform(0.85, 1.15),
                2,
            )

            average_order_value = (
                metrics["aov"]
                * np.random.uniform(0.75, 1.25)
            )

            revenue = round(
                conversions * average_order_value,
                2,
            )

            rows.append({
                "date": date,
                "campaign_id": campaign_id,
                "channel": channel,
                "region": np.random.choice(regions),
                "device": np.random.choice(devices),
                "impressions": impressions,
                "clicks": clicks,
                "leads": leads,
                "conversions": conversions,
                "spend": spend,
                "revenue": revenue,
            })

    df = pd.DataFrame(rows)

    output_path = Path("data/raw/marketing_campaigns.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print("Marketing dataset generated successfully!")
    print(f"Records: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Saved to: {output_path}")
    print("\nDataset preview:")
    print(df.head())

    print("\nDataset dimensions:")
    print(df.shape)


if __name__ == "__main__":
    generate_marketing_data()
