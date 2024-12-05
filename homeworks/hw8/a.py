import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data.csv'  # Replace with the correct file path
df = pd.read_csv(file_path)

# Part 1: Data Import and Initial Cleaning
# Fill missing values in 'Sales' column with the average sales value
avg_sales = df['Sales'].mean()
df['Sales'].fillna(avg_sales, inplace=True)

# Add a new column 'Revenue' (Revenue = Sales * Price)
df['Revenue'] = df['Sales'] * df['Price']

# Part 2: Data Analysis with Grouping and Aggregation
# Group by 'Product' to calculate total Sales and Revenue
product_group = df.groupby('Product').agg({'Sales': 'sum', 'Revenue': 'sum'})

# Group by 'Region' to calculate total Revenue
region_group = df.groupby('Region').agg({'Revenue': 'sum'})

# Identify the product with the highest average revenue
product_avg_revenue = df.groupby('Product')['Revenue'].mean()
highest_avg_revenue_product = product_avg_revenue.idxmax()

# Part 3: Data Visualization with Matplotlib
# Bar chart for total revenue by Product
plt.figure(figsize=(8, 6))
product_group['Revenue'].plot(kind='bar', color='skyblue', title="Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Pie chart for revenue share by Region
plt.figure(figsize=(8, 6))
region_group['Revenue'].plot(kind='pie', autopct='%1.1f%%', startangle=90, title="Revenue Share by Region")
plt.ylabel("")  # Hides y-label for a cleaner pie chart
plt.show()

# Expected Results Discussion
print("Products total revenue:\n", product_group)
print("\nRegions total revenue:\n", region_group)
print(f"\nProduct with the highest average revenue: {highest_avg_revenue_product}")
