from pathlib import Path

import pandas as pd
import plotly.express as px


def create_channel_roas_chart():

    file_path = Path("data/processed/marketing_analysis.csv")
    df = pd.read_csv(file_path)

    df = df.sort_values("roas", ascending=True)

    fig = px.bar(
        df,
        x="roas",
        y="channel",
        orientation="h",
        text="roas",
        title="Marketing Channel Performance — ROAS",
        labels={
            "roas": "Return on Ad Spend (x)",
            "channel": "Marketing Channel",
        },
        hover_data=[
            "total_spend",
            "total_revenue",
            "customer_acquisition_cost",
            "conversion_rate_pct",
        ],
    )

    fig.update_traces(
        texttemplate="%{text:.2f}x",
        textposition="outside",
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="ROAS (x)",
        yaxis_title="",
        showlegend=False,
    )

    fig.write_html("reports/channel_roas.html")

    fig.show()

    print("Chart saved to reports/channel_roas.html")


if __name__ == "__main__":
    create_channel_roas_chart()