# Superstore Sales Analysis using Pandas

## Overview
This project involves a comprehensive **Exploratory Data Analysis (EDA)** on a retail sales dataset. By using **Pandas**, I transformed raw transaction data into actionable business insights regarding profitability and regional growth.

## Dataset
- **Source:** Kaggle Superstore Dataset
- **Rows:** ~9,994 records
- **Columns:** 21 features (including Order Date, Region, Category, Sales, and Profit)
- **Description:** Historical data of a fictional retail store, capturing order-level details across multiple product lines and customer segments.

## Tools Used
- **Python:** Primary programming language.
- **Pandas:** Used for data manipulation, cleaning, and aggregation.

## Analysis Performed
* **Data Cleaning:** Handled missing values, corrected data types (e.g., converting Order Date to datetime objects), and removed duplicate entries.
* **Sales Trends:** Analyzed monthly and yearly sales growth to identify seasonal peaks.
* **Category Analysis:** Evaluated performance across main categories (**Furniture**, **Office Supplies**, **Technology**).
* **Regional Performance:** Segmented sales and profit by geography (East, West, Central, South).
* **Customer Segmentation:** Breakdown of revenue by Consumer, Corporate, and Home Office segments.

## Key Insights
* **Top Performing Categories:** **Technology** leads in total revenue, while **Office Supplies** shows the highest order frequency.
* **High Revenue Regions:** The **West** and **East** regions contribute over 60% of total sales.
* **Profitability Warning:** Identified specific sub-categories (like **Tables**) that generate high sales but frequent net losses due to heavy discounting.
* **Shipping Efficiency:** **Standard Class** is the most preferred shipping mode, accounting for the bulk of transactions.