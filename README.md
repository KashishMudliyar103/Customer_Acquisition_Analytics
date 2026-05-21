# Customer Acquisition & Marketing Analytics Dashboard

An end-to-end data analytics project that simulates a real-world business problem faced by a retail bank — identifying which marketing channels are worth the spend, which customers are the most valuable, and where churn risk is highest.

Built entirely from scratch using **Python → SQL → Power BI**.

---

## Problem Statement

A retail bank spends budget across 5 marketing channels (Google Ads, Facebook, Email, Referral, Branch) with no clear visibility into:
- Which channels convert leads into customers most efficiently?
- Which customer segments generate the highest lifetime value?
- Where is churn concentrated, and which high-value segments are at risk?

This project answers all three questions through a multi-page interactive dashboard backed by a full data pipeline.

---

## Key Findings

| Insight | Detail |
|---|---|
| **Best converting channel** | Facebook — 51.5% conversion rate |
| **Most cost-efficient channel** | Google Ads — $39.58 cost per acquisition (lowest) |
| **Worst channel** | Email — most leads (3,361) but only 35.4% conversion |
| **Highest LTV segment** | Platinum card + $60K–$80K income → estimated LTV of **$314,958** |
| **Highest churn risk** | Gold card + $80K–$120K income → **23.8% churn rate** |
| **Overall churn rate** | 16.1% (1,627 of 10,127 customers attrited) |
| **Best acquisition month** | December — 1,193 customers acquired |

---

## Project Architecture

```
Raw CSV (Kaggle)
      │
      ▼
sql_pipeline.ipynb       ← SQLite queries → KPI tables (conversion rate, ROI, CLV, attrition)
      │
      ▼
segmentation.py          ← RFM scoring + K-Means clustering (scikit-learn)
      │
      ▼
analytics_output.xlsx    ← 5 KPI sheets exported for Power BI
segmentation_output.xlsx ← RFM segments + cluster labels
      │
      ▼
Power BI Dashboard       ← 2-page interactive dashboard
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python (pandas, numpy) | Data wrangling and pipeline |
| SQLite (via Python) | KPI queries — conversion rate, ROI, CLV, attrition |
| scikit-learn | K-Means clustering (k=4), StandardScaler |
| matplotlib / seaborn | Segment distribution chart |
| Power BI Desktop | Interactive multi-page dashboard |
| openpyxl | Excel export for Power BI import |

---

## File Structure

```
Customer Acquisition and marketing analytics dashboard/
│
├── Data/
│   ├── BankChurners.csv            ← Raw dataset (10,127 rows) from Kaggle
│   ├── analytics_output.xlsx       ← SQL pipeline output (5 sheets)
│   ├── segmentation_output.xlsx    ← RFM + K-Means output
│   ├── credit_card.db              ← SQLite database
│   └── segment_distribution.png   ← RFM segment bar chart
│
├── sql_pipeline.ipynb              ← SQL KPI pipeline (Jupyter Notebook)
├── segmentation.py                 ← RFM scoring + K-Means clustering
├── Final Dashboard.pbix            ← Power BI dashboard file
├── requirements.txt                ← Python dependencies
└── README.md

```

---

## Dashboard Pages

### Page 1 — Executive Summary
KPI cards (total customers, avg CLV, conversion rate, CPA, churn %), customer breakdown by card category, attrition donut chart, and churn rate by income segment.

### Page 2 — Marketing & Acquisition Analysis
- Horizontal bar: conversion rate by channel
- Combo chart: spend vs customers acquired by channel
- Dual-axis line: monthly new customers vs spend
- Scatter plot: cost per acquisition vs conversion rate (one dot per channel)

---

## Setup & Usage

### 1. Clone the repo
```bash
git clone https://github.com/KashishMudliyar103/customer-acquisition-analytics.git
cd customer-acquisition-analytics
```

### 2. Create virtual environment and install dependencies
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### 3. Run the SQL pipeline
Open `sql_pipeline.ipynb` in VS Code or Jupyter and run all cells.
This generates `analytics_output.xlsx` and `credit_card.db`.

### 4. Run the segmentation
```bash
python segmentation.py
```
This generates `segmentation_output.xlsx` and `segment_distribution.png`.

### 5. Open the dashboard
Open `Final Dashboard.pbix` in Power BI Desktop.
If prompted to refresh data, point the data source to your local `Data/` folder.

---

## Dataset

**BankChurners** by Sakshi Goyal — available on [Kaggle](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)

- 10,127 customers
- 23 features including age, income category, card type, transaction count, credit limit, and attrition flag
- A synthetic `marketing_campaigns` table (50 rows) was generated using NumPy to simulate multi-channel acquisition data

# Business Report
BA_Report_Kashish_Mudliyar.docx   ← Business analysis report with findings & recommendations

---

## Author

**Kashish Mudliyar**
[GitHub](https://github.com/KashishMudliyar103)
