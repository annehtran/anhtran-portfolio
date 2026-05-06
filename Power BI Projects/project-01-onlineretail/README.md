# Project 1 - Online Retail Analysis
![DAX](https://img.shields.io/badge/DAX-0E5A8A?logo=microsoft&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

# Subjective
This is an exploratory analysis on a real online retail transaction data set of two years from [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii). Findings the **insights** through countries, customers, prices, products performances and sale drivers across all regions then generate report and provide **recommendations** 

## Business Question Answered
1. How did it perform in 2020 and 2021?
2. Identifying the key drivers for rising an droping in sales.
3. What are top products and niche products?
4. Exploratory data analysis to find interesting insights.
5. Recommendations

## Summary
- **Revenue declined 4.3% YoY**: £8.6M in FY2010 vs £8.2M in FY2011, driven by volume contraction despite a slight price improvement.
- **United Kingdom dominates**: 82.58% of all revenue (£8.2M) in FY2011, making international diversification a clear strategic priority.
- **Strong seasonal concentration**: October and November alone account for over 30% of annual revenue in both years, driven by Christmas gifting.
- **Critical return rate problem**: Two top-selling products (PAPER CRAFT LITTLE BIRDIE, MEDIUM CERAMIC TOP STORAGE JAR) each have ~50% return rates which is a major profitability risk.
- **Customer acquisition is healthy**: 4,210 unique customers in 2011 vs 4,212 in 2010, with 2,657 customers buying in both years resulting a 63% retention rate.


## Recommendation
- Build operational resilience around the November peak. The business depends on a single month for ~18% of annual revenue.
- Develop a deliberate international growth strategy. A 3-year target of 75% UK and 25% international as giving the growth signals in Australia, France and Germany which is achievable.
- Conduct a quality standards or identify the root defect of the two high-return products immediately.
- Invest in Australia as a priority international market. 

---

# Raw Data and Outputs
## Dataset
- This dataset has an excel file containing two sheets with 1,067,371 raw rows in total.
- Source: https://archive.ics.uci.edu/dataset/502/online+retail+ii
- License: Under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.
- Donated on 9/20/2019

## Tables
1. Fact_Sales: 802,949 rows | 10 columns
2. Fact_Returns: 19,493 rows | 9 columns
3. Dim_Product: 4,626 rows | 3 columns
4. Dim_Customer: 5,862 rows | 7 columns
5. Dim_Country: 40 rows | 4 columns
6. Dim_Date: 761 rows | 13 columns

## Key DAX Measures
1. Total Revenue (SUMX): calculates row by row and respects filter context
2. Revenue YoY%: uses CALCULATE filter context to the prior year
3. Revenue LY: cumulatives performance tracking
4. Return Rate: examines product quality
5. New Customers: uses All(Dim_Date) to look across entire date range to find each customer's fist-ever purchase date
6. Avg Order Value: efficiency metric when comparing to Total Orders

## Report Pages
1. Executive Overview
2. Product & Category
3. Region Performance
4. Drivers
5. Country Details
6. Definitions

## Final Reports
1. Raw Power BI file is located in pbix folder
2. Snapshot of reports are exported in pdf located at exports folder
