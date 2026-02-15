import pandas as pd 

df = pd.read_csv("/home/aryan/Documents/AI_ML/data-analyst-portfolio/pandas-analysis/superstore.csv",encoding="latin1")

print("Data Type of data")
print(df.dtypes)

print("Data of first 5 rows")
print(df.head())

print("Data of last 5 rows")
print(df.tail())

print("Information about data")
print(df.info())

print("Details of data")
print(df.describe())

print("Number of null rows in every column")
print(df.isnull().sum())

print("Data of Profit and Sales")
print(df[["Profit","Sales"]])

print("Data of sales above 250")
print(df[df["Sales"]>250])

print("Data reports where sales is above 4000 and profit is above 800")
print(df[(df["Sales"]>4000) & (df["Profit"]>800)])

print("Total sales report")
print(df["Sales"].sum())

print("Total unique order ID")
print(df["Order ID"].nunique())

print("Total unique Customer ID and Order Date")
print(df[["Customer ID","Order Date"]].nunique())

print("Report of sales by category")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=True))

print("Reports of Profit by sub-category")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False))

print("Reports of Sales by region")
print(df.groupby("Region")["Sales"].sum())

print("Converting string date into column date for easy and better analysis")
df["Order Date"] = pd.to_datetime(df["Order Date"])
print(df["Order Date"])
print(df["Order Date"].dt.year)
print(df["Order Date"].dt.month)
print(df["Order Date"].dt.day) 

print("Report of yearly growth")
df["year"]= df["Order Date"].dt.year
print(df.groupby("year")["Sales"].sum())

print("Reports of Monthly sales ")
df["Month"] = df["Order Date"].dt.to_period("M")
print(df.groupby("Month")["Sales"].sum()) 

print("List of top 10 customers")
print(df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10))

print("List of repeated Customer")
print(df.groupby("Customer ID")["Order ID"].nunique().sort_values(ascending=False))

print("list of top categories with highest profit")
print(df.groupby("Category")[["Profit","Sales"]].sum().sort_values(by=["Profit"],ascending=False))

