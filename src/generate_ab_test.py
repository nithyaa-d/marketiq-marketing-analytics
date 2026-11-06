from pathlib import Path

import numpy as np
import pandas as pd


def generate_ab_test_data():

    rng = np.random.default_rng(42)

    sample_size = 10000

    variants = np.array(
        ["Control", "Treatment"] * sample_size
    )

    rng.shuffle(variants)

    conversion_probabilities = {
        "Control": 0.08,
        "Treatment": 0.09,
    }

    probabilities = [
        conversion_probabilities[variant]
        for variant in variants
    ]

    conversions = rng.binomial(1, probabilities)

    df = pd.DataFrame({
        "user_id": range(1, len(variants) + 1),
        "variant": variants,
        "converted": conversions,
    })

    output_path = Path("data/raw/ab_test_experiment.csv")
    df.to_csv(output_path, index=False)

    print(f"Generated {len(df)} experiment records.")
    print(df["variant"].value_counts())
    print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    generate_ab_test_data()