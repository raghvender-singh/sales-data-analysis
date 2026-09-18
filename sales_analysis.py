import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load Dataset
df = pd.read_csv("sales.csv", encoding="latin1")

# Data inspection
print(df.head())
df.info()
print(df.describe())

# Data Cleaning & Feature Creation
df["Date"] = pd.to_datetime(df["Date"])
df["revenue"] = df["Quantity"] * df["Unit_Price"]
df["Month"] = df["Date"].dt.month

# Analysis

# Total Revenue
total_revenue = (df["revenue"].sum())
print("total_revenue:",total_revenue)

# Category Revenue
category_revenue = df.groupby("Category")["revenue"].sum().sort_values(ascending=False)
print(category_revenue)

# City Revenue
city_revenue = df.groupby("City")["revenue"].sum().sort_values(ascending=False)
print(city_revenue)

# Product Revenue
product_revenue = df.groupby("Product")["revenue"].sum().sort_values(ascending=False)
print(product_revenue)

# City Summary
city_summary = df.groupby("City").agg(total_revenue = ("revenue","sum"), total_orders = ("Order_ID","count"))
city_summary["AOV"] = city_summary["total_revenue"]/city_summary["total_orders"]
print(city_summary)

# City Quantity

city_quantity = df.groupby("City")["Quantity"].sum().sort_values(ascending=False)
print(city_quantity)

# Average Unit Price by Product

product_avg_price = df.groupby("Product")["Unit_Price"].mean().sort_values(ascending=False)
print(product_avg_price)

# Average Unit Price by Category

category_avg_price = df.groupby("Category")["Unit_Price"].mean().sort_values(ascending=False)
print(category_avg_price)

# Monthly Revenue

monthly_revenue = df.groupby("Month")["revenue"].sum()
print(monthly_revenue)

# Visualizations

# Category Revenue
plt.figure(figsize=(8,5))
sns.barplot(x=category_revenue.index,y=category_revenue.values)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue(rupees)")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# City Revenue
plt.figure(figsize=(8,5))
sns.barplot(x= city_revenue.index,y= city_revenue.values)
plt.title("Revenue by city")
plt.xlabel("City")
plt.ylabel("Revenue(rupees)")
plt.show()

# Product Revenue
plt.figure(figsize=(10,5))
sns.barplot(x= product_revenue.index,y= product_revenue.values)
plt.title("Revenue by product")
plt.xlabel("Product")
plt.ylabel("Revenue(rupees)")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# AOV by City
plt.figure(figsize=(8,5))
sns.barplot(x= city_summary.index,y= city_summary["AOV"])
plt.title("Average Order Value by City")
plt.xlabel("City")
plt.ylabel("Average Order Value(rupees)")
plt.tight_layout()
plt.show()

# Quantity Sold by Product
product_quantity = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x = product_quantity.index, y= product_quantity.values)
plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation= 45)
plt.tight_layout()
plt.show()

# Business Insights

# - The total revenue generated during the analysis period was ₹2,58,300.
# - Electronics generated the highest revenue of ₹2,11,000.
# - Delhi generated the highest city-wise revenue of ₹1,35,200.
# - Lucknow generated the highest AOV of ₹34,833.
# - Laptop generated the highest product revenue of ₹1,65,000.
# - Pen had the highest quantity sold, with 20 units.
# - Kanpur had the highest total quantity sold, despite generating lower revenue.


