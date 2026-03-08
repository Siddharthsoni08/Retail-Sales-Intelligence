import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


# ==============================
# TOTAL REVENUE
# ==============================

total_revenue = df["Sales"].sum()
print("\nTotal Revenue:", total_revenue)


# ==============================
# SALES BY CATEGORY
# ==============================

category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)


# ==============================
# MONTHLY SALES TREND
# ==============================

df["Month"] = df["Order Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("images/monthly_sales_trend.png")


# ==============================
# TOP 10 PRODUCTS
# ==============================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))

top_products.plot(kind="bar")

plt.title("Top 10 Best Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=75)

plt.savefig("images/top_products_sales.png")

plt.show()