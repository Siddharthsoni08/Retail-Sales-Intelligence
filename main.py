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

# ==============================
# PROFIT BY CATEGORY
# ==============================

profit_category = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:")
print(profit_category)

plt.figure(figsize=(8,5))

profit_category.plot(kind="bar", color="green")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.savefig("images/profit_by_category.png")
plt.show()


# ==============================
# REGION WISE PROFIT
# ==============================

region_profit = df.groupby("Region")["Profit"].sum()

print("\nProfit by Region:")
print(region_profit)

plt.figure(figsize=(8,5))

region_profit.plot(kind="bar")

plt.title("Region Wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.savefig("images/region_profit.png")
plt.show()


# ==============================
# LOSS MAKING PRODUCTS
# ==============================

loss_products = df[df["Profit"] < 0]

top_loss_products = loss_products.groupby("Product Name")["Profit"].sum().sort_values().head(10)

print("\nTop Loss Making Products:")
print(top_loss_products)

plt.figure(figsize=(10,6))

top_loss_products.plot(kind="bar", color="red")

plt.title("Top 10 Loss Making Products")
plt.xlabel("Product")
plt.ylabel("Loss")

plt.xticks(rotation=75)

plt.savefig("images/loss_products.png")
plt.show()