import pandas as pd
import numpy as np

df = pd.read_csv("/home/aryan/Documents/AI_ML/data-analyst-portfolio/numpy-analysis/train.csv",encoding="latin1")
numeric_df = df.select_dtypes(include=[np.number])
data = numeric_df.values


print("All the columns with only numeric values")
print(numeric_df)

print("No. of rows and columns in dataset")
print(data.shape)

print("All the columns name with numeric values")
print(numeric_df.columns)

print("Index value of column SalePrice")
salesprice_index = numeric_df.columns.get_loc("SalePrice")
print(salesprice_index)

print("Mean of sales price")
print(np.mean(data[:, salesprice_index]))

print("max of sales price")
print(np.max(data[:,salesprice_index]))

print("Total sum of all sales price")
print(np.sum(data[:,salesprice_index]))

print("Houses which have price more than 300000")
expensive_houses = data[data[:, salesprice_index]>300000]
print(expensive_houses)
print(len(expensive_houses))

print("Houses which are built after year 2000")
year_index = numeric_df.columns.get_loc("YearBuilt")
modern_houses = data[data[:, year_index]>2000]
print(modern_houses)
print(len(modern_houses)) 

print("House which have more than 3 bedrooms") 
bedroom_index = numeric_df.columns.get_loc("BedroomAbvGr")
big_houses = data[data[:, bedroom_index]>3]
print(big_houses)
print(len(big_houses))

print("correlation matrix of sales")
corr_matrix = np.corrcoef(data.T)
sale_corr = corr_matrix[salesprice_index]
print(sale_corr)

print("Columns with correlation matrix")
feature_names = numeric_df.columns
for name, corr in zip(feature_names, sale_corr):
    print(name, corr)

y = numeric_df["SalePrice"].values
x = numeric_df.drop(columns=["SalePrice"]).values

print("price per square root")
grliv_index = numeric_df.columns.get_loc("GrLivArea")
price_per_sqrt = y/x[:, grliv_index]
price_per_sqrt = price_per_sqrt.reshape(-1,1)
x_new = np.hstack((x, price_per_sqrt))
print(price_per_sqrt)