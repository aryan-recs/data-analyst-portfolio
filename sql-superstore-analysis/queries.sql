CREATE DATABASE IF NOT EXISTS superstore_db;
USE superstore_db;
CREATE TABLE IF NOT EXISTS superstore(
    row_id INT,
    order_id VARCHAR(50),
    order_date VARCHAR(50),
    ship_date VARCHAR(50),
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code INT,
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(100),
    sales VARCHAR(50),
    quantity INT,
    discount FLOAT,
    profit VARCHAR(50)
);
-- INSERTING DATA INTO ALL SCHEMAS

LOAD DATA LOCAL INFILE '/home/aryan/Documents/AI_ML/data-analyst-portfolio/sql-superstore-analysis/superstore.csv'
INTO TABLE superstore
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- CONVERTING DATE FORMAT OF SUPERSTORE DATABASE INTO SQL FORMAT
UPDATE superstore
SET order_date = STR_TO_DATE(order_date, '%m/%d/%Y'),
ship_date = STR_TO_DATE(ship_date, '%m/%d/%Y');

-- CHANGING order_date, ship_date CONSTRAINTS FROM VARCHAR TO DATE
ALTER TABLE superstore
MODIFY order_date DATE,
MODIFY ship_date DATE;

-- TO VIEW DATA
SELECT * FROM superstore LIMIT 10;

-- TOTAL SALES DATA
SELECT SUM(sales) AS total_sales FROM superstore;

-- TOTAL PROFIT 
SELECT SUM(PROFIT) AS total_profit FROM superstore;

-- UNIQUE CATEGORIES
SELECT DISTINCT category FROM superstore;

-- DATA OF SALES ON BASIS OF CATEGORY
SELECT category, SUM(sales) AS total_sales
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- DATA OF TOP 5 SALES ON BASIS OF SUB_CATEGORIES
SELECT sub_category, SUM(sales) AS sales
FROM superstore
GROUP BY sub_category
ORDER BY sales DESC;

-- DATA OF SALES ON BASIS OF REGION WISE
SELECT region, SUM(sales) AS total_sales
FROM superstore
GROUP BY region
ORDER BY total_sales DESC;

-- DATA OF SALES ON THE MONTLY BASIS
SELECT order_date, SUM(sales) AS revenue
FROM superstore
GROUP BY order_date
ORDER BY order_date DESC;

-- DATA OF PRODUCT ON THE BASIS OF LOSS
SELECT sub_category, SUM(profit) AS total_profit
FROM superstore
GROUP BY sub_category
HAVING total_profit<0
ORDER BY total_profit ASC ;

-- DATA OF TOP CUSTOMER ON BASIS OF SALES
SELECT customer_name, SUM(sales) AS total_spent
FROM superstore
GROUP BY customer_name
ORDER BY total_spent DESC;

-- DATA OF GROWTH YEAR BY YEAR
SELECT
YEAR (order_date) AS year,
SUM(sales) AS revenue
FROM superstore
GROUP BY year
ORDER BY year ASC;

-- DATA OF PROFIT MARGIN BY CATEGORY
SELECT
category,
SUM(profit) / SUM(sales) *100 AS profit_margin
FROM superstore
GROUP BY category
ORDER BY profit_margin ASC;

-- DATA OF TOTAL RUNNING SALES
SELECT
order_date,
SUM(profit) OVER (ORDER BY order_date) AS running_sales
FROM superstore
ORDER BY running_sales DESC;