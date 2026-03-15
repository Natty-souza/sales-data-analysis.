import pandas as pd

data = pd.read_csv("sales_data.csv")

print(data.head())

sales_by_region = data.groupby("region")["sales"].sum()

print(sales_by_region)