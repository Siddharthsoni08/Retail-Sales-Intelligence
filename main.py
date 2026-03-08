import pandas as pd

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

print(df.head())

# Dataset size 
print("Dataset Shape:", df.shape)

#column Names
print("\nColumns:")

#dataset info
print("\nDataset Info:")
print(df.info())

#convert date columns 
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nDate conversion done")

print(df.dtypes)

# total revenue
total_revenue = df["Sales"].sum()
print("\nTotal Revenue:", total_revenue)

# sales by category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# extract month from order date
df["Month"] = df["Order Date"].dt.month

# monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("images/monthly_sales_trend.png")
plt.show()