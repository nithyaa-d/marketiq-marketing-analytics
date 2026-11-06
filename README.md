\# MarketIQ — Marketing Campaign \& Performance Analytics



\*\*An end-to-end marketing analytics project using Python, SQL, DuckDB and Streamlit to evaluate campaign performance, understand marketing efficiency, and support data-driven budget decisions.\*\*



\## Project Overview



MarketIQ is an interactive marketing analytics solution designed to transform campaign-level data into actionable business insights.



The project explores how marketing performance can be evaluated across channels, campaigns, regions, devices and time periods. It combines data preparation, exploratory analysis, SQL-based KPI calculations, statistical testing and interactive visualisation in a single analytics workflow.



\*\*Note:\*\* This project uses synthetic data generated for portfolio and demonstration purposes. All findings and A/B test results are simulated and do not represent actual company performance.



\## Business Objectives



\- Evaluate marketing channel and campaign effectiveness.

\- Monitor key performance indicators such as CTR, CPC, CPL, CAC and ROAS.

\- Compare performance across regions, devices and months.

\- Identify conversion funnel drop-offs.

\- Demonstrate statistical analysis through a simulated A/B test.

\- Present findings through an interactive dashboard.



\## Technology Stack



| Area | Technologies |

|---|---|

| Programming | Python, Pandas, NumPy |

| SQL Analytics | SQL, DuckDB |

| Statistics | SciPy, hypothesis testing |

| Visualisation | Plotly, Matplotlib, Seaborn |

| Dashboard | Streamlit |

| Testing | Pytest, pytest-cov |

| Development | Jupyter Notebook, Git |



\## Project Workflow



1\. \*\*Data Generation:\*\* Create a synthetic marketing dataset covering 14 campaigns across 2025.

2\. \*\*Data Exploration:\*\* Examine data types, missing values, duplicates, descriptive statistics, correlations and potential outliers.

3\. \*\*SQL Analytics:\*\* Use DuckDB to calculate marketing KPIs and analyse campaign, channel, regional, device and monthly performance.

4\. \*\*Statistical Analysis:\*\* Conduct a two-proportion z-test on a simulated A/B experiment.

5\. \*\*Visualisation:\*\* Build interactive Plotly reports.

6\. \*\*Dashboard:\*\* Bring the analyses together in a Streamlit application with interactive filters and KPI summaries.



\## Key Metrics



| KPI | Definition |

|---|---|

| CTR | Clicks / Impressions × 100 |

| CPC | Spend / Clicks |

| CPL | Spend / Leads |

| CAC | Spend / Conversions |

| Conversion Rate | Conversions / Clicks × 100 |

| ROAS | Revenue / Spend |

| Revenue-based ROI | (Revenue − Spend) / Spend × 100 |



\*CAC uses conversions as a proxy for acquired customers. Revenue-based ROI excludes product and operating costs and should not be interpreted as profit ROI.\*



\## Interactive Reports



The project includes the following interactive Plotly reports:



| Analysis | Report |

|---|---|

| Channel Performance | \[View Channel ROAS](reports/channel\_roas.html) |

| Monthly Trends | \[View Monthly ROAS](reports/monthly\_roas.html) |

| Regional Performance | \[View Regional Analysis](reports/regional\_performance.html) |

| Device Performance | \[View Device Analysis](reports/device\_performance.html) |

| Campaign Performance | \[View Campaign Analysis](reports/campaign\_performance.html) |

| Marketing Funnel | \[View Funnel Analysis](reports/marketing\_funnel.html) |

| A/B Testing | \[View A/B Test Comparison](reports/ab\_test\_comparison.html) |



\*\*Dashboard:\*\* Run the Streamlit application locally using the instructions below.



\## Simulated A/B Testing



A simulated experiment compares two groups of 10,000 observations each.



| Metric | Control | Treatment |

|---|---:|---:|

| Sample Size | 10,000 | 10,000 |

| Conversions | 773 | 930 |

| Conversion Rate | 7.73% | 9.30% |



\*\*Simulated experiment results:\*\*

\- Absolute conversion lift: 1.57 percentage points.

\- Relative conversion lift: 20.31%.

\- Z-statistic: 3.98.

\- P-value: 0.000070.

\- 95% confidence interval for the absolute difference: 0.80 to 2.34 percentage points.



The simulated result is statistically significant at the 5% level. It demonstrates how a two-proportion z-test can be used to evaluate conversion-rate differences. It is not evidence of an actual marketing intervention's effectiveness.



\## Example Analytical Questions



\- Which marketing channels generate the strongest return on advertising spend?

\- How do campaign costs and conversion rates vary?

\- Are there meaningful differences in performance across regions and devices?

\- How does marketing performance change over time?

\- Where does the largest proportional drop-off occur in the aggregate funnel?

\- Is the difference between simulated experiment groups statistically significant?



\## Project Structure



```text

marketiq-marketing-analytics/

│

├── app.py

├── generate\_data.py

├── run\_analysis.py

│

├── data/

│   ├── raw/

│   └── processed/

│

├── sql/

│   ├── marketing\_analysis.sql

│   ├── monthly\_trends.sql

│   ├── regional\_analysis.sql

│   ├── device\_analysis.sql

│   ├── funnel\_analysis.sql

│   └── campaign\_analysis.sql

│

├── src/

│   ├── eda.py

│   ├── channel\_visualization.py

│   ├── monthly\_visualization.py

│   ├── regional\_visualization.py

│   ├── device\_visualization.py

│   ├── campaign\_visualization.py

│   ├── funnel\_visualization.py

│   ├── generate\_ab\_test.py

│   └── ab\_test\_analysis.py

│

├── reports/

├── docs/

│   └── images/

├── notebooks/

└── tests/

```



\## Getting Started



\### 1. Clone the repository



```bash

git clone https://github.com/nithyaa-d/marketiq-marketing-analytics.git

cd marketiq-marketing-analytics

```



\### 2. Create and activate a virtual environment



\*\*Windows:\*\*



```cmd

python -m venv .venv

.venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Generate the synthetic dataset



```bash

python generate\_data.py

```



\### 5. Run SQL analyses



```bash

python run\_analysis.py

```



\### 6. Launch the dashboard



```bash

streamlit run app.py

```



The dashboard will be available at:



`http://localhost:8501`



\## Skills Demonstrated



\- Python-based data analysis and data preparation.

\- SQL querying and analytical KPI development.

\- Data exploration and statistical reasoning.

\- Marketing performance and funnel analytics.

\- A/B testing and hypothesis testing.

\- Interactive visualisation and dashboard development.

\- Translating analytical results into business questions and recommendations.



\## Author



\*\*Nithya Doresha\*\*



Data Analyst | Analytics Engineer | Data Engineer



\- \[LinkedIn](https://www.linkedin.com/in/nithyad2608/)

\- \[GitHub](https://github.com/nithyaa-d)



Open to opportunities across Sweden and relocation within Sweden.



\---



\*Built as a portfolio project to demonstrate practical data analytics, SQL, Python, statistical testing and business-focused visualisation.\*

