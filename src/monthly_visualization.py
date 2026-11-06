from pathlib import Path

import pandas as pd
import plotly.express as px


def create_monthly_roas_chart():

    df = pd.read_csv("data/processed/monthly_trends.csv")

    df["month"] = pd.to_datetime(df["month"])

    fig = px.line(
        df,
        x="month",
        y="roas",
        markers=True,
        title="Monthly Marketing ROAS Trend",
        labels={
            "month": "Month",
            "roas": "Return on Ad Spend (x)",
        },
        hover_data=[
            "total_revenue",
            "total_spend",
            "total_conversions",
        ],
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=9),
    )

    fig.update_layout(
        template="plotly_white",
        yaxis_title="ROAS (x)",
        xaxis_title="",
        hovermode="x unified",
    )

    fig.write_html("reports/monthly_roas.html")

    print("Monthly chart saved successfully!")


if __name__ == "__main__":
    create_monthly_roas_chart()