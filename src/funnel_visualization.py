import pandas as pd
import plotly.graph_objects as go


def create_funnel_chart():

    df = pd.read_csv("data/processed/funnel_analysis.csv")

    row = df.iloc[0]

    stages = [
        "Impressions",
        "Clicks",
        "Leads",
        "Conversions",
    ]

    values = [
        row["total_impressions"],
        row["total_clicks"],
        row["total_leads"],
        row["total_conversions"],
    ]

    fig = go.Figure(
        go.Funnel(
            y=stages,
            x=values,
            textinfo="value+percent initial",
        )
    )

    fig.update_layout(
        title="Marketing Conversion Funnel",
        template="plotly_white",
        xaxis_title="Number of Events",
    )

    fig.write_html("reports/marketing_funnel.html")

    print("Funnel chart saved: reports/marketing_funnel.html")


if __name__ == "__main__":
    create_funnel_chart()