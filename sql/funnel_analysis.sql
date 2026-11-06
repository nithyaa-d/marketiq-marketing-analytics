-- MarketIQ: Marketing Funnel Analysis

SELECT
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(leads) AS total_leads,
    SUM(conversions) AS total_conversions,

    ROUND(
        100.0 * SUM(clicks) / NULLIF(SUM(impressions), 0), 2
    ) AS impression_to_click_pct,

    ROUND(
        100.0 * SUM(leads) / NULLIF(SUM(clicks), 0), 2
    ) AS click_to_lead_pct,

    ROUND(
        100.0 * SUM(conversions) / NULLIF(SUM(leads), 0), 2
    ) AS lead_to_conversion_pct,

    ROUND(
        100.0 * SUM(conversions) / NULLIF(SUM(impressions), 0), 4
    ) AS overall_conversion_pct

FROM read_csv_auto('data/raw/marketing_campaigns.csv');