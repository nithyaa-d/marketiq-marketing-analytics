# MarketIQ — Marketing Campaign & Performance Analytics

**An end-to-end marketing analytics project built with Python, SQL, DuckDB and Streamlit to evaluate campaign effectiveness, monitor marketing KPIs and support data-driven business decisions.**

## Overview

MarketIQ is an interactive marketing analytics solution that transforms campaign-level data into meaningful business insights.

The project analyses marketing performance across channels, campaigns, regions, devices and time periods. It combines data generation, exploratory data analysis, SQL-based KPI calculations, statistical testing and interactive visualisation in one analytical workflow.

**Dataset disclaimer:** MarketIQ uses synthetic data generated specifically for this portfolio project. All analytical findings, campaign comparisons and A/B testing results are simulated and do not represent actual company performance.

## Business Objectives

- Evaluate marketing channel and campaign effectiveness.
- Measure marketing efficiency using CTR, CPC, CPL, CAC and ROAS.
- Compare performance across regions, devices and months.
- Analyse conversion funnel drop-offs.
- Demonstrate statistical hypothesis testing through an A/B experiment.
- Translate analytical findings into actionable business recommendations.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| SQL & Data Processing | SQL, DuckDB |
| Statistics | SciPy, Hypothesis Testing |
| Visualisation | Plotly, Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Testing | Pytest, pytest-cov |
| Development | Jupyter Notebook, Git, GitHub |

## Project Architecture

```text
Raw Marketing Data
        |
        v
Data Generation & Preparation
        |
        v
Exploratory Data Analysis
        |
        v
SQL Analytics using DuckDB
        |
        v
Processed Analytical Datasets
        |
        +----------------------+
        |                      |
        v                      v
Interactive Reports      Statistical Testing
        |                      |
        +----------+-----------+
                   |
                   v
          Streamlit Dashboard
                   |
                   v
       Business Insights & Analysis
```

## Dataset

The primary marketing dataset contains **5,110 simulated records**, representing 14 campaigns over 365 days in 2025.

It includes:

| Column | Description |
|---|---|
| date | Campaign activity date |
| campaign_id | Unique campaign identifier |
| channel | Marketing acquisition channel |
| region | Geographic region |
| device | Device category |
| impressions | Number of impressions |
| clicks | Number of clicks |
| leads | Number of generated leads |
| conversions | Number of conversions |
| spend | Marketing expenditure |
| revenue | Revenue attributed to campaigns |

An additional simulated A/B testing dataset contains 20,000 observations split between control and treatment groups.

## Key Marketing KPIs

| KPI | Calculation |
|---|---|
| CTR | Clicks / Impressions × 100 |
| CPC | Spend / Clicks |
| CPL | Spend / Leads |
| CAC | Spend / Conversions |
| Conversion Rate | Conversions / Clicks × 100 |
| ROAS | Revenue / Spend |
| Revenue-based ROI | (Revenue − Spend) / Spend × 100 |

*Note: CAC uses conversions as a proxy for acquired customers. Revenue-based ROI excludes product and operating costs, so it should not be interpreted as profit ROI.*

## Analytical Modules

### 1. Channel Performance
- Compare marketing channels using CTR, conversion rate, CAC and ROAS.
- Evaluate relative channel efficiency.
- Identify channels that may warrant further investigation.

### 2. Monthly Performance
- Analyse monthly marketing trends.
- Compare ROAS and conversion rates over time.
- Examine changes in campaign efficiency.

### 3. Regional Analysis
- Compare marketing performance across geographic regions.
- Evaluate regional ROAS, CAC and conversion rates.

### 4. Device Analysis
- Compare campaign performance across mobile, desktop and tablet.
- Examine differences in conversion efficiency and returns.

### 5. Campaign Performance
- Rank individual campaigns by ROAS.
- Compare acquisition costs and conversion performance.
- Identify high- and low-performing simulated campaigns.

### 6. Marketing Funnel Analysis
- Examine aggregate impressions, clicks, leads and conversions.
- Calculate stage-to-stage conversion rates.
- Identify the largest proportional drop-off.

*The funnel uses aggregate counts rather than user-level journey tracking.*

### 7. A/B Testing
- Compare control and treatment conversion rates.
- Apply a two-proportion z-test.
- Calculate absolute and relative conversion lift.
- Estimate a 95% confidence interval.
- Evaluate statistical significance.

## Interactive Reports

Explore the individual Plotly visualisations:

| Report | Interactive Visualisation |
|---|---|
| Channel Performance | [View Channel ROAS](reports/channel_roas.html) |
| Monthly Trends | [View Monthly Performance](reports/monthly_roas.html) |
| Regional Analysis | [View Regional Performance](reports/regional_performance.html) |
| Device Analysis | [View Device Performance](reports/device_performance.html) |
| Campaign Analysis | [View Campaign Performance](reports/campaign_performance.html) |
| Marketing Funnel | [View Marketing Funnel](reports/marketing_funnel.html) |
| A/B Testing | [View A/B Test Comparison](reports/ab_test_comparison.html) |

## Simulated A/B Testing Results

The experiment compares two simulated groups, each containing 10,000 observations.

| Metric | Control | Treatment |
|---|---:|---:|
| Sample Size | 10,000 | 10,000 |
| Conversions | 773 | 930 |
| Conversion Rate | 7.73% | 9.30% |

**Statistical results:**

| Metric | Result |
|---|---:|
| Absolute Conversion Lift | +1.57 percentage points |
| Relative Conversion Lift | +20.31% |
| Z-statistic | 3.9776 |
| P-value | 0.000070 |
| 95% Confidence Interval | 0.80 to 2.34 percentage points |

The simulated treatment group shows a statistically significant conversion-rate difference at the 5% significance level.

This demonstrates the application of statistical hypothesis testing to marketing experiments. It does not establish the effectiveness of a real-world marketing intervention.

## Exploratory Data Analysis

The EDA workflow includes:

- Dataset structure and data type inspection.
- Missing-value and duplicate checks.
- Descriptive statistical analysis.
- Correlation analysis.
- IQR-based potential outlier identification.

Potential outliers are flagged for investigation rather than automatically removed.

## Project Structure

```text
marketiq-marketing-analytics/
│
├── app.py
├── generate_data.py
├── run_analysis.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   ├── marketing_campaigns.csv
│   │   └── ab_test_experiment.csv
│   │
│   └── processed/
│       ├── campaign_analysis.csv
│       ├── device_analysis.csv
│       ├── funnel_analysis.csv
│       ├── marketing_analysis.csv
│       ├── monthly_trends.csv
│       └── regional_analysis.csv
│
├── sql/
│   ├── marketing_analysis.sql
│   ├── monthly_trends.sql
│   ├── regional_analysis.sql
│   ├── device_analysis.sql
│   ├── funnel_analysis.sql
│   └── campaign_analysis.sql
│
├── src/
│   ├── eda.py
│   ├── channel_visualization.py
│   ├── monthly_visualization.py
│   ├── regional_visualization.py
│   ├── device_visualization.py
│   ├── campaign_visualization.py
│   ├── funnel_visualization.py
│   ├── generate_ab_test.py
│   ├── ab_test_analysis.py
│   └── ab_test_visualization.py
│
├── reports/
│   ├── channel_roas.html
│   ├── monthly_roas.html
│   ├── regional_performance.html
│   ├── device_performance.html
│   ├── campaign_performance.html
│   ├── marketing_funnel.html
│   ├── ab_test_comparison.html
│   ├── ab_test_group_results.csv
│   └── eda_summary.txt
│
├── tests/
│   └── test_data_validation.py
│
├── docs/
│   └── images/
│
└── notebooks/
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- Git

### 1. Clone the repository

```bash
git clone https://github.com/nithyaa-d/marketiq-marketing-analytics.git

cd marketiq-marketing-analytics
```

### 2. Create a virtual environment

**Windows:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the marketing dataset

```bash
python generate_data.py
```

### 5. Generate the A/B testing dataset

```bash
python src/generate_ab_test.py
```

### 6. Execute SQL analyses

```bash
python run_analysis.py
```

### 7. Run exploratory data analysis

```bash
python src/eda.py
```

### 8. Launch the Streamlit dashboard

```bash
streamlit run app.py
```

Open the local dashboard:

`http://localhost:8501`

### 9. Run automated tests

```bash
python -m pytest tests -v
```

## Testing

The project includes automated data validation tests covering:

- Expected dataset columns.
- Record count validation.
- Missing-value checks.
- Duplicate campaign-date detection.
- Non-negative marketing metrics.
- Campaign and date-range completeness.

**Current test result: 6 passed.**

## Skills Demonstrated

- Python programming and data manipulation.
- SQL analytics and KPI development.
- Data cleaning and exploratory data analysis.
- Marketing campaign and funnel analytics.
- Statistical hypothesis testing and A/B testing.
- Interactive dashboards and data visualisation.
- Data validation and automated testing.
- Business-oriented analytical thinking.

## Author

**Nithya Doresha**

Data Analyst | Analytics Engineer | Data Engineer

Based in Gothenburg, Sweden.

- [LinkedIn](https://www.linkedin.com/in/nithyad2608/)
- [GitHub](https://github.com/nithyaa-d)

Open to opportunities across Sweden and willing to relocate within Sweden.

---

*MarketIQ is an independent portfolio project created to demonstrate practical data analytics, SQL, Python, statistical testing and business-focused visualisation.*
