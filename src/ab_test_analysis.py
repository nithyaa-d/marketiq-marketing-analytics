from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm


def analyze_ab_test():

    df = pd.read_csv("data/raw/ab_test_experiment.csv")

    summary = df.groupby("variant")["converted"].agg(
        users="count",
        conversions="sum",
        conversion_rate="mean",
    )

    control = summary.loc["Control"]
    treatment = summary.loc["Treatment"]

    p1 = control["conversion_rate"]
    p2 = treatment["conversion_rate"]

    n1 = control["users"]
    n2 = treatment["users"]

    absolute_lift = p2 - p1
    relative_lift = (absolute_lift / p1) * 100

    pooled_rate = (
        control["conversions"] + treatment["conversions"]
    ) / (n1 + n2)

    standard_error = np.sqrt(
        pooled_rate * (1 - pooled_rate) * (1 / n1 + 1 / n2)
    )

    z_score = absolute_lift / standard_error
    p_value = 2 * norm.sf(abs(z_score))

    # 95% confidence interval for the difference
    ci_se = np.sqrt(
        (p1 * (1 - p1) / n1)
        + (p2 * (1 - p2) / n2)
    )

    ci_lower = absolute_lift - 1.96 * ci_se
    ci_upper = absolute_lift + 1.96 * ci_se

    print("\nAB TEST RESULTS")
    print("=" * 40)

    print(summary.round(4))

    print(f"\nAbsolute lift: {absolute_lift * 100:.2f} percentage points")
    print(f"Relative lift: {relative_lift:.2f}%")
    print(f"Z-score: {z_score:.4f}")
    print(f"P-value: {p_value:.6f}")

    print(
        f"95% confidence interval: "
        f"{ci_lower * 100:.2f}% to {ci_upper * 100:.2f}%"
    )

    if p_value < 0.05:
        print("\nResult: Statistically significant difference.")
    else:
        print("\nResult: No statistically significant difference.")

    Path("reports").mkdir(exist_ok=True)

    summary.to_csv("reports/ab_test_group_results.csv")

    print("\nResults saved to reports/ab_test_group_results.csv")


if __name__ == "__main__":
    analyze_ab_test()