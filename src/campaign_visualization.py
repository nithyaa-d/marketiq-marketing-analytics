import pandas as pd
import plotly.express as px


def create_campaign_chart():

    df = pd.read_csv("data/processed/campaign_analysis.csv")
    df = df.sort_values("roas", ascending=True)

    fig = px.bar(
        df,
        x="roas",
        y="campaign_id",
        orientation="h",
        text="roas",
        color="channel",
        title="Campaign Performance — ROAS Comparison",
        labels={
            "roas": "Return on Ad Spend (x)",
            "campaign_id": "Campaign",
            "channel": "Marketing Channel",
        },
        hover_data=[
            "total_revenue",
            "total_spend",
            "total_conversions",
            "cac",
        ],
    )

    fig.update_traces(
        texttemplate="%{text:.2f}x",
        textposition="outside",
    )

    fig.update_layout(
        template="plotly_white",
        height=650,
        yaxis_title="",
        xaxis_title="ROAS (x)",
    )

    fig.write_html("reports/campaign_performance.html")

    print("Campaign chart saved: reports/campaign_performance.html")


if __name__ == "__main__":
    create_campaign_chart()