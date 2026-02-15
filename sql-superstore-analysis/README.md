# Superstore Sales Analysis using SQL

## Overview
This project focuses on extracting and analyzing retail data using **Advanced SQL** queries. The goal was to transform raw transactional records into structured business reports to identify growth opportunities and customer behavior patterns.

## Database
- **System:** MySQL 
- **Table:** `superstore`
- **Total Records:** 9,994 entries

## SQL Skills Demonstrated
* **Complex Aggregations:** Utilizing `SUM()` to evaluate store performance.
* **Data Grouping:** Mastering `GROUP BY` and `HAVING` clauses to filter aggregated results.
* **Temporal Analysis:** Using `EXTRACT()`, `DATE_FORMAT()`for time-series reporting.
* **Window Functions:** Implementing `OVER BY` `SUM() AS PROFIT_TOTAL` for deep-dive analytics.

## Key Analysis
* **Sales by Category:** Comparative analysis of revenue across **Technology**, **Furniture**, and **Office Supplies**.
* **Monthly Revenue Trends:** Month-over-month (MoM) growth calculations to identify seasonal sales cycles.
* **Top Customers:** Ranking customers by total spend and order frequency using `DENSE_RANK()`.
* **Running Total Analysis:** Tracking cumulative revenue over the fiscal year to monitor target achievements.
* **Profitability Audit:** Identifying products with negative profit margins despite high sales volume.

## Key Insights
* **Category Lead:** **Technology** generates the highest profit margin per unit, while **Office Supplies** drives the highest transaction volume.
* **Growth Peaks:** Consistent revenue spikes identified in **November and December**, suggesting a heavy reliance on holiday promotions.
* **Customer Loyalty:** The top 10% of customers contribute to nearly 40% of the total annual revenue.

## Files
- `schema.sql`: Contains the DDL scripts for table creation and data constraints.
- `queries.sql`: A collection of all analytical scripts, from basic filtering to advanced window functions.

## Author
**Aryan** | Aspiring Data Analyst