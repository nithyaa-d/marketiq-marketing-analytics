import pandas as pd
import plotly.express as px


def create_regional_chart():

    df = pd.read_csv("data/processed/regional_analysis.csv")

    df = df.sort_values("roas", ascending=True)

    fig = px.bar(
        df,
        x="region",
        y="roas",
        text="roas",
        title="Marketing Performance by Region",
        labels={
            "region": "Region",
            "roas": "Return on Ad Spend (x)",
        },
        hover_data=[
            "total_revenue",
            "total_spend",
            "cac",
            "conversion_rate_pct",
        ],
    )

    fig.update_traces(
        texttemplate="%{text:.2f}x",
        textposition="outside",
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
    )

    fig.write_html("reports/regional_performance.html")

    print("Regional chart saved: reports/regional_performance.html")


if __name__ == "__main__":
    create_regional_chart()