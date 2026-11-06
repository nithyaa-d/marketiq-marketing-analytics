-- MarketIQ: Regional Marketing Performance

SELECT
    region,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(spend), 2) AS total_spend,
    ROUND(SUM(revenue), 2) AS total_revenue,

    ROUND(
        100.0 * SUM(clicks) / NULLIF(SUM(impressions), 0), 2
    ) AS ctr_pct,

    ROUND(
        100.0 * SUM(conversions) / NULLIF(SUM(clicks), 0), 2
    ) AS conversion_rate_pct,

    ROUND(
        SUM(spend) / NULLIF(SUM(conversions), 0), 2
    ) AS cac,

    ROUND(
        SUM(revenue) / NULLIF(SUM(spend), 0), 2
    ) AS roas

FROM read_csv_auto('data/raw/marketing_campaigns.csv')

GROUP BY region

ORDER BY roas DESC;