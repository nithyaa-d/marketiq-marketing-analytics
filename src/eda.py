from pathlib import Path

import pandas as pd


def run_eda():

    df = pd.read_csv("data/raw/marketing_campaigns.csv")

    numeric_columns = [
        "impressions",
        "clicks",
        "leads",
        "conversions",
        "spend",
        "revenue",
    ]

    report = []

    report.append("MARKETIQ - EXPLORATORY DATA ANALYSIS")
    report.append("=" * 45)

    report.append("\n1. DATASET OVERVIEW")
    report.append(f"Rows: {df.shape[0]}")
    report.append(f"Columns: {df.shape[1]}")
    report.append(f"Date range: {df['date'].min()} to {df['date'].max()}")

    report.append("\n2. DATA TYPES")
    report.append(df.dtypes.to_string())

    report.append("\n3. MISSING VALUES")
    report.append(df.isnull().sum().to_string())

    report.append("\n4. DUPLICATE ROWS")
    report.append(str(df.duplicated().sum()))

    report.append("\n5. DESCRIPTIVE STATISTICS")
    report.append(df[numeric_columns].describe().round(2).to_string())

    report.append("\n6. CORRELATION MATRIX")
    report.append(
        df[numeric_columns].corr().round(2).to_string()
    )

    report.append("\n7. OUTLIER CHECK (IQR METHOD)")

    for column in numeric_columns:

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = df[
            (df[column] < lower_bound)
            | (df[column] > upper_bound)
        ]

        report.append(
            f"{column}: {len(outliers)} potential outliers"
        )

    output = "\n".join(report)

    Path("reports").mkdir(exist_ok=True)
    Path("reports/eda_summary.txt").write_text(
        output,
        encoding="utf-8",
    )

    print(output)
    print("\nEDA report saved to reports/eda_summary.txt")


if __name__ == "__main__":
    run_eda()