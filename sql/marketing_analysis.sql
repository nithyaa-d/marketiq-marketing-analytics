
-- MarketIQ: Marketing Channel Performance Analysis

WITH channel_performance AS (
    SELECT
        channel,
        SUM(impressions) AS total_impressions,
        SUM(clicks) AS total_clicks,
        SUM(leads) AS total_leads,
        SUM(conversions) AS total_conversions,
        ROUND(SUM(spend), 2) AS total_spend,
        ROUND(SUM(revenue), 2) AS total_revenue

    FROM read_csv_auto('data/raw/marketing_campaigns.csv')

    GROUP BY channel
)

SELECT
    channel,
    total_impressions,
    total_clicks,
    total_leads,
    total_conversions,
    total_spend,
    total_revenue,

    ROUND(
        100.0 * total_clicks / NULLIF(total_impressions, 0), 2
    ) AS ctr_pct,

    ROUND(
        total_spend / NULLIF(total_clicks, 0), 2
    ) AS cost_per_click,

    ROUND(
        total_spend / NULLIF(total_leads, 0), 2
    ) AS cost_per_lead,

    ROUND(
        total_spend / NULLIF(total_conversions, 0), 2
    ) AS customer_acquisition_cost,

    ROUND(
        100.0 * total_conversions / NULLIF(total_clicks, 0), 2
    ) AS conversion_rate_pct,

    ROUND(
        total_revenue / NULLIF(total_spend, 0), 2
    ) AS roas,

    ROUND(
        100.0 * (total_revenue - total_spend)
        / NULLIF(total_spend, 0), 2
    ) AS revenue_based_roi_pct

FROM channel_performance

ORDER BY roas DESC;
