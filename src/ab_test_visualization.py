import pandas as pd
import plotly.express as px


def create_ab_test_chart():

    df = pd.read_csv("data/raw/ab_test_experiment.csv")

    summary = (
        df.groupby("variant")["converted"]
        .mean()
        .reset_index()
    )

    summary["conversion_rate_pct"] = (
        summary["converted"] * 100
    )

    fig = px.bar(
        summary,
        x="variant",
        y="conversion_rate_pct",
        text="conversion_rate_pct",
        title="A/B Test — Conversion Rate Comparison",
        labels={
            "variant": "Experiment Group",
            "conversion_rate_pct": "Conversion Rate (%)",
        },
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside",
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        yaxis_title="Conversion Rate (%)",
    )

    fig.write_html("reports/ab_test_comparison.html")

    print("A/B test chart saved: reports/ab_test_comparison.html")


if __name__ == "__main__":
    create_ab_test_chart()