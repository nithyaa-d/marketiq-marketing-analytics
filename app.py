
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="MarketIQ | Marketing Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# LIGHT THEME
# ==========================================================

st._config.set_option("theme.base", "light")

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Global application */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: #F5F7FB !important;
    color: #1E293B !important;
}

html, body, [class*="css"] {
    font-family: 'Inter', Arial, sans-serif;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #172554 !important;
    font-weight: 750 !important;
}

h1 {
    font-size: 2.5rem !important;
    letter-spacing: -1px;
}

h2 {
    font-size: 1.65rem !important;
}

h3 {
    font-size: 1.15rem !important;
}

/* Standard text */
p, li, label,
[data-testid="stMarkdownContainer"] p {
    color: #334155 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0;
}

[data-testid="stSidebar"] * {
    color: #334155;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #172554 !important;
}

/* Filter labels */
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p {
    color: #334155 !important;
    font-weight: 600 !important;
}

/* Input fields */
input, textarea {
    color: #1E293B !important;
    background-color: #FFFFFF !important;
    -webkit-text-fill-color: #1E293B !important;
}

/* Selectbox and multiselect */
[data-baseweb="select"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="select"] * {
    color: #1E293B !important;
}

[data-baseweb="select"] input {
    color: #1E293B !important;
    -webkit-text-fill-color: #1E293B !important;
}

/* Dropdown menus */
[data-baseweb="popover"],
[data-baseweb="menu"],
[data-baseweb="list"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="popover"] *,
[data-baseweb="menu"] * {
    color: #1E293B !important;
}

/* Date picker */
[data-baseweb="calendar"] {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
}

[data-baseweb="calendar"] * {
    color: #1E293B !important;
}

/* KPI cards */
.kpi-card {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 21px 22px;
    min-height: 130px;
    margin-bottom: 12px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
}

.kpi-card .kpi-label {
    color: #64748B !important;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 12px;
}

.kpi-card .kpi-value {
    color: #172554 !important;
    font-size: 27px;
    font-weight: 800;
    line-height: 1.3;
}

.kpi-card .kpi-subtitle {
    color: #64748B !important;
    font-size: 12px;
    margin-top: 8px;
}

/* KPI accent borders */
.kpi-blue {
    border-left: 5px solid #3B82F6;
}

.kpi-purple {
    border-left: 5px solid #8B5CF6;
}

.kpi-green {
    border-left: 5px solid #10B981;
}

.kpi-orange {
    border-left: 5px solid #F59E0B;
}

.kpi-pink {
    border-left: 5px solid #EC4899;
}

.kpi-teal {
    border-left: 5px solid #14B8A6;
}

/* Streamlit metric cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    padding: 18px 20px;
    border-radius: 14px;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: #64748B !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div {
    color: #172554 !important;
    font-size: 26px !important;
    font-weight: 800 !important;
}

/* Tables */
[data-testid="stDataFrame"] {
    background-color: #FFFFFF !important;
}

/* Captions */
[data-testid="stCaptionContainer"] p {
    color: #64748B !important;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 10px;
}

[data-testid="stAlert"] p {
    color: #334155 !important;
}

/* Buttons */
.stButton button {
    background-color: #2563EB !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px;
    font-weight: 600;
}

.stButton button p {
    color: #FFFFFF !important;
}

/* Dividers */
hr {
    border-color: #E2E8F0 !important;
}

/* Chart containers */
[data-testid="stPlotlyChart"] {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 5px;
}

/* Section descriptions */
.section-description {
    color: #64748B !important;
    font-size: 13px;
    margin-top: -10px;
    margin-bottom: 18px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# DATA LOADING
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent


@st.cache_data
def load_csv(relative_path):
    file_path = BASE_DIR / relative_path

    if not file_path.exists():
        return None

    return pd.read_csv(file_path)


campaigns = load_csv("data/raw/marketing_campaigns.csv")

if campaigns is None:
    st.error("Marketing dataset not found. Check data/raw/marketing_campaigns.csv.")
    st.stop()

campaigns["date"] = pd.to_datetime(
    campaigns["date"],
    errors="coerce"
)

campaigns = campaigns.dropna(subset=["date"])

ab_test_data = load_csv("reports/ab_test_group_results.csv")


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def safe_divide(numerator, denominator):
    return numerator / denominator if denominator else 0


def create_kpi_card(label, value, subtitle, color_class):
    st.markdown(
        f"""
        <div class="kpi-card {color_class}">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def style_chart(fig, height=380):
    fig.update_layout(
        template="plotly_white",
        height=height,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        margin=dict(l=20, r=20, t=60, b=25),
        title_font=dict(
            size=17,
            color="#172554",
        ),
        font=dict(
            family="Arial",
            color="#334155",
            size=12,
        ),
        legend_title_text="",
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            font_size=12,
            font_color="#1E293B",
        ),
        xaxis=dict(
            title_font=dict(color="#334155"),
            tickfont=dict(color="#334155"),
            gridcolor="#E2E8F0",
        ),
        yaxis=dict(
            title_font=dict(color="#334155"),
            tickfont=dict(color="#334155"),
            gridcolor="#E2E8F0",
        ),
    )
    return fig


# ==========================================================
# HEADER
# ==========================================================

st.title("📊 MarketIQ")

st.subheader("Marketing Campaign & Performance Analytics")

st.markdown(
    """
    <p style="font-size:15px; color:#64748B !important;">
    An interactive marketing analytics platform exploring campaign
    performance, marketing efficiency, conversion funnels and
    business insights.
    </p>
    """,
    unsafe_allow_html=True,
)

st.info(
    "📌 Dataset notice: This project uses synthetic data. "
    "All campaign results, experiment outcomes and business insights "
    "are simulated for demonstration purposes."
)

st.divider()


# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.title("🎛️ Dashboard Filters")
st.sidebar.caption("Explore campaign performance using the filters below.")

channels = sorted(campaigns["channel"].dropna().unique())
regions = sorted(campaigns["region"].dropna().unique())
devices = sorted(campaigns["device"].dropna().unique())

selected_channels = st.sidebar.multiselect(
    "Marketing Channel",
    channels,
    default=channels,
)

selected_regions = st.sidebar.multiselect(
    "Region",
    regions,
    default=regions,
)

selected_devices = st.sidebar.multiselect(
    "Device",
    devices,
    default=devices,
)

min_date = campaigns["date"].min().date()
max_date = campaigns["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
else:
    start_date, end_date = min_date, max_date

st.sidebar.divider()

if st.sidebar.button("Reset filters", use_container_width=True):
    st.rerun()


# ==========================================================
# APPLY FILTERS
# ==========================================================

filtered_df = campaigns[
    campaigns["channel"].isin(selected_channels)
    & campaigns["region"].isin(selected_regions)
    & campaigns["device"].isin(selected_devices)
    & (campaigns["date"].dt.date >= start_date)
    & (campaigns["date"].dt.date <= end_date)
].copy()

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()


# ==========================================================
# KPI CALCULATIONS
# ==========================================================

impressions = filtered_df["impressions"].sum()
clicks = filtered_df["clicks"].sum()
leads = filtered_df["leads"].sum()
conversions = filtered_df["conversions"].sum()
spend = filtered_df["spend"].sum()
revenue = filtered_df["revenue"].sum()

ctr = safe_divide(clicks, impressions) * 100
click_to_conversion = safe_divide(conversions, clicks) * 100
roas = safe_divide(revenue, spend)
cpc = safe_divide(spend, clicks)


# ==========================================================
# EXECUTIVE KPI OVERVIEW
# ==========================================================

st.header("Executive KPI Overview")

st.markdown(
    '<p class="section-description">Key marketing performance indicators for the selected period.</p>',
    unsafe_allow_html=True,
)

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    create_kpi_card(
        "Total Impressions",
        f"{impressions:,.0f}",
        "Campaign reach",
        "kpi-blue",
    )

with kpi2:
    create_kpi_card(
        "Total Clicks",
        f"{clicks:,.0f}",
        "Audience engagement",
        "kpi-purple",
    )

with kpi3:
    create_kpi_card(
        "Total Leads",
        f"{leads:,.0f}",
        "Leads generated",
        "kpi-green",
    )

kpi4, kpi5, kpi6 = st.columns(3)

with kpi4:
    create_kpi_card(
        "Total Conversions",
        f"{conversions:,.0f}",
        "Recorded conversions",
        "kpi-orange",
    )

with kpi5:
    create_kpi_card(
        "Marketing Spend",
        f"${spend:,.2f}",
        "Total campaign investment",
        "kpi-pink",
    )

with kpi6:
    create_kpi_card(
        "Revenue",
        f"${revenue:,.2f}",
        "Recorded campaign revenue",
        "kpi-teal",
    )


# ==========================================================
# MARKETING EFFICIENCY
# ==========================================================

st.divider()

st.header("Marketing Efficiency")

eff1, eff2, eff3, eff4 = st.columns(4)

eff1.metric("Click-Through Rate", f"{ctr:.2f}%")
eff2.metric("Click-to-Conversion", f"{click_to_conversion:.2f}%")
eff3.metric("Return on Ad Spend", f"{roas:.2f}x")
eff4.metric("Cost per Click", f"${cpc:.2f}")


# ==========================================================
# CHANNEL AGGREGATION
# ==========================================================

channel_summary = (
    filtered_df
    .groupby("channel", as_index=False)
    .agg(
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        leads=("leads", "sum"),
        conversions=("conversions", "sum"),
        spend=("spend", "sum"),
        revenue=("revenue", "sum"),
    )
)

channel_summary["ctr"] = (
    channel_summary["clicks"]
    / channel_summary["impressions"].replace(0, float("nan"))
    * 100
).fillna(0)

channel_summary["conversion_rate"] = (
    channel_summary["conversions"]
    / channel_summary["clicks"].replace(0, float("nan"))
    * 100
).fillna(0)

channel_summary["roas"] = (
    channel_summary["revenue"]
    / channel_summary["spend"].replace(0, float("nan"))
).fillna(0)

channel_summary["cac"] = (
    channel_summary["spend"]
    / channel_summary["conversions"].replace(0, float("nan"))
).fillna(0)


# ==========================================================
# CHANNEL PERFORMANCE
# ==========================================================

st.divider()

st.header("Channel Performance Analysis")

st.markdown(
    '<p class="section-description">Compare channels by return, conversion efficiency and investment.</p>',
    unsafe_allow_html=True,
)

chart1, chart2 = st.columns(2)

with chart1:
    roas_data = channel_summary.sort_values("roas")

    fig_roas = px.bar(
        roas_data,
        x="roas",
        y="channel",
        orientation="h",
        color="channel",
        text=roas_data["roas"].map(lambda x: f"{x:.2f}x"),
        title="Return on Ad Spend by Channel",
        labels={"roas": "ROAS", "channel": "Marketing Channel"},
    )

    fig_roas.update_traces(textposition="outside", cliponaxis=False)
    fig_roas.update_layout(showlegend=False)
    st.plotly_chart(style_chart(fig_roas), use_container_width=True)

with chart2:
    conversion_data = channel_summary.sort_values("conversion_rate")

    fig_conversion = px.bar(
        conversion_data,
        x="conversion_rate",
        y="channel",
        orientation="h",
        color="channel",
        text=conversion_data["conversion_rate"].map(lambda x: f"{x:.2f}%"),
        title="Click-to-Conversion Rate by Channel",
        labels={
            "conversion_rate": "Conversion Rate (%)",
            "channel": "Marketing Channel",
        },
    )

    fig_conversion.update_traces(textposition="outside", cliponaxis=False)
    fig_conversion.update_layout(showlegend=False)
    st.plotly_chart(style_chart(fig_conversion), use_container_width=True)

fig_spend = px.bar(
    channel_summary,
    x="channel",
    y=["spend", "revenue"],
    barmode="group",
    title="Marketing Spend vs Revenue by Channel",
    labels={
        "value": "Amount",
        "channel": "Marketing Channel",
        "variable": "Metric",
    },
    color_discrete_map={
        "spend": "#F59E0B",
        "revenue": "#2563EB",
    },
)

st.plotly_chart(style_chart(fig_spend), use_container_width=True)


# ==========================================================
# MONTHLY PERFORMANCE
# ==========================================================

st.divider()

st.header("Monthly Performance Trends")

monthly_summary = (
    filtered_df
    .assign(month=filtered_df["date"].dt.to_period("M").astype(str))
    .groupby("month", as_index=False)
    .agg(
        clicks=("clicks", "sum"),
        conversions=("conversions", "sum"),
        spend=("spend", "sum"),
        revenue=("revenue", "sum"),
    )
)

monthly_summary["roas"] = (
    monthly_summary["revenue"]
    / monthly_summary["spend"].replace(0, float("nan"))
).fillna(0)

monthly_summary["conversion_rate"] = (
    monthly_summary["conversions"]
    / monthly_summary["clicks"].replace(0, float("nan"))
    * 100
).fillna(0)

monthly_col1, monthly_col2 = st.columns(2)

with monthly_col1:
    fig_monthly_roas = px.line(
        monthly_summary,
        x="month",
        y="roas",
        markers=True,
        title="Monthly Return on Ad Spend",
        labels={"month": "Month", "roas": "ROAS"},
    )

    fig_monthly_roas.update_traces(
        line=dict(width=3, color="#2563EB"),
        marker=dict(size=8),
    )

    st.plotly_chart(style_chart(fig_monthly_roas), use_container_width=True)

with monthly_col2:
    fig_monthly_conversion = px.line(
        monthly_summary,
        x="month",
        y="conversion_rate",
        markers=True,
        title="Monthly Click-to-Conversion Rate",
        labels={
            "month": "Month",
            "conversion_rate": "Conversion Rate (%)",
        },
    )

    fig_monthly_conversion.update_traces(
        line=dict(width=3, color="#10B981"),
        marker=dict(size=8),
    )

    st.plotly_chart(
        style_chart(fig_monthly_conversion),
        use_container_width=True,
    )


# ==========================================================
# REGIONAL PERFORMANCE
# ==========================================================

st.divider()

st.header("Regional Performance")

region_summary = (
    filtered_df
    .groupby("region", as_index=False)
    .agg(
        clicks=("clicks", "sum"),
        conversions=("conversions", "sum"),
        spend=("spend", "sum"),
        revenue=("revenue", "sum"),
    )
)

region_summary["roas"] = (
    region_summary["revenue"]
    / region_summary["spend"].replace(0, float("nan"))
).fillna(0)

region_summary["conversion_rate"] = (
    region_summary["conversions"]
    / region_summary["clicks"].replace(0, float("nan"))
    * 100
).fillna(0)

region_col1, region_col2 = st.columns(2)

with region_col1:
    fig_region = px.bar(
        region_summary,
        x="region",
        y="roas",
        color="region",
        title="ROAS by Region",
        labels={"region": "Region", "roas": "ROAS"},
    )

    fig_region.update_layout(showlegend=False)
    st.plotly_chart(style_chart(fig_region), use_container_width=True)

with region_col2:
    fig_region_conversion = px.bar(
        region_summary,
        x="region",
        y="conversion_rate",
        color="region",
        title="Conversion Rate by Region",
        labels={
            "region": "Region",
            "conversion_rate": "Conversion Rate (%)",
        },
    )

    fig_region_conversion.update_layout(showlegend=False)
    st.plotly_chart(
        style_chart(fig_region_conversion),
        use_container_width=True,
    )


# ==========================================================
# DEVICE PERFORMANCE
# ==========================================================

st.divider()

st.header("Device Performance")

device_summary = (
    filtered_df
    .groupby("device", as_index=False)
    .agg(
        clicks=("clicks", "sum"),
        conversions=("conversions", "sum"),
        spend=("spend", "sum"),
        revenue=("revenue", "sum"),
    )
)

device_summary["roas"] = (
    device_summary["revenue"]
    / device_summary["spend"].replace(0, float("nan"))
).fillna(0)

device_summary["conversion_rate"] = (
    device_summary["conversions"]
    / device_summary["clicks"].replace(0, float("nan"))
    * 100
).fillna(0)

device_col1, device_col2 = st.columns(2)

with device_col1:
    fig_device_roas = px.bar(
        device_summary,
        x="device",
        y="roas",
        color="device",
        title="ROAS by Device",
        labels={"device": "Device", "roas": "ROAS"},
    )

    fig_device_roas.update_layout(showlegend=False)
    st.plotly_chart(style_chart(fig_device_roas), use_container_width=True)

with device_col2:
    fig_device_conversion = px.bar(
        device_summary,
        x="device",
        y="conversion_rate",
        color="device",
        title="Conversion Rate by Device",
        labels={
            "device": "Device",
            "conversion_rate": "Conversion Rate (%)",
        },
    )

    fig_device_conversion.update_layout(showlegend=False)
    st.plotly_chart(
        style_chart(fig_device_conversion),
        use_container_width=True,
    )


# ==========================================================
# MARKETING FUNNEL
# ==========================================================

st.divider()

st.header("Marketing Funnel Analysis")

funnel_df = pd.DataFrame({
    "stage": ["Impressions", "Clicks", "Leads", "Conversions"],
    "volume": [impressions, clicks, leads, conversions],
})

fig_funnel = go.Figure(
    go.Funnel(
        y=funnel_df["stage"],
        x=funnel_df["volume"],
        textinfo="value+percent initial",
        marker=dict(
            color=["#93C5FD", "#60A5FA", "#3B82F6", "#1D4ED8"]
        ),
        connector=dict(line=dict(color="#CBD5E1")),
    )
)

fig_funnel.update_layout(title="Marketing Conversion Funnel")

st.plotly_chart(
    style_chart(fig_funnel, height=420),
    use_container_width=True,
)

st.caption(
    "This funnel uses aggregate stage totals, not user-level journey tracking."
)


# ==========================================================
# CAMPAIGN PERFORMANCE
# ==========================================================

st.divider()

st.header("Campaign Performance")

campaign_summary = (
    filtered_df
    .groupby("campaign_id", as_index=False)
    .agg(
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        leads=("leads", "sum"),
        conversions=("conversions", "sum"),
        spend=("spend", "sum"),
        revenue=("revenue", "sum"),
    )
)

campaign_summary["roas"] = (
    campaign_summary["revenue"]
    / campaign_summary["spend"].replace(0, float("nan"))
).fillna(0)

campaign_summary["cac"] = (
    campaign_summary["spend"]
    / campaign_summary["conversions"].replace(0, float("nan"))
).fillna(0)

campaign_summary = campaign_summary.sort_values(
    "roas",
    ascending=False,
)

fig_campaign = px.bar(
    campaign_summary,
    x="campaign_id",
    y="roas",
    color="roas",
    color_continuous_scale="Blues",
    title="Campaign ROAS Comparison",
    labels={"campaign_id": "Campaign", "roas": "ROAS"},
    hover_data={
        "spend": ":,.2f",
        "revenue": ":,.2f",
        "conversions": ":,",
        "cac": ":.2f",
    },
)

st.plotly_chart(style_chart(fig_campaign), use_container_width=True)

st.subheader("Campaign Performance Details")

display_campaigns = campaign_summary.copy()
display_campaigns["roas"] = display_campaigns["roas"].round(2)
display_campaigns["cac"] = display_campaigns["cac"].round(2)

st.dataframe(
    display_campaigns,
    use_container_width=True,
    hide_index=True,
)


# ==========================================================
# A/B TESTING
# ==========================================================

st.divider()

st.header("A/B Testing – Experiment Analysis")

st.markdown(
    "A simulated experiment comparing conversion performance "
    "between a control group and a treatment group."
)

if ab_test_data is not None and not ab_test_data.empty:

    st.dataframe(
        ab_test_data,
        use_container_width=True,
        hide_index=True,
    )

    group_col = next(
        (
            col for col in ab_test_data.columns
            if col.lower() in ["group", "variant", "experiment_group"]
        ),
        None,
    )

    rate_col = next(
        (
            col for col in ab_test_data.columns
            if col.lower() in [
                "conversion_rate",
                "conversion_rate_pct",
                "rate",
            ]
        ),
        None,
    )

    if group_col and rate_col:

        ab_chart = px.bar(
            ab_test_data,
            x=group_col,
            y=rate_col,
            color=group_col,
            title="A/B Test Conversion Rate Comparison",
        )

        st.plotly_chart(
            style_chart(ab_chart),
            use_container_width=True,
        )

else:
    st.info(
        "A/B test results file was not found. "
        "Run the A/B test analysis script to generate it."
    )

st.caption(
    "The experiment is simulated. Statistical significance in generated "
    "data does not establish real-world campaign impact."
)


# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.divider()

st.header("Business Insights & Recommendations")

if not channel_summary.empty:

    best_channel = channel_summary.loc[
        channel_summary["roas"].idxmax()
    ]

    lowest_channel = channel_summary.loc[
        channel_summary["roas"].idxmin()
    ]

    best_conversion_channel = channel_summary.loc[
        channel_summary["conversion_rate"].idxmax()
    ]

    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:

        st.markdown("### 🏆 Strongest ROAS")

        st.success(
            f"**{best_channel['channel']}** has the highest "
            f"simulated ROAS at **{best_channel['roas']:.2f}x**."
        )

        st.markdown("### 🎯 Strongest Conversion Rate")

        st.info(
            f"**{best_conversion_channel['channel']}** has the "
            f"highest click-to-conversion rate at "
            f"**{best_conversion_channel['conversion_rate']:.2f}%**."
        )

    with insight_col2:

        st.markdown("### 🔍 Channel to Investigate")

        st.warning(
            f"**{lowest_channel['channel']}** has the lowest "
            f"simulated ROAS at **{lowest_channel['roas']:.2f}x**. "
            "Review targeting, creative and costs before making "
            "budget changes."
        )

        st.markdown("### 💡 Recommended Next Step")

        st.info(
            "Validate channel performance using real campaign data, "
            "customer acquisition costs and profit margins before "
            "reallocating marketing budgets."
        )


# ==========================================================
# PROJECT FOOTER
# ==========================================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        padding:25px 0;
        color:#64748B !important;
    ">
        <strong style="color:#172554 !important;">MarketIQ</strong>
        <br>
        Marketing Campaign & Performance Analytics
        <br>
        Built with Python · SQL · DuckDB · Pandas · Plotly · Streamlit
        <br><br>
        <span style="font-size:12px; color:#64748B !important;">
        Portfolio project | Synthetic dataset | Simulated findings
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
