import numpy as np
import pandas as pd

# Product sales data
sales = np.array([
    [100, 120, 150],
    [80, 100, 130],
    [150, 160, 180],
    [70, 90, 110],
    [120, 140, 160]
])


# 1. Total sales for every product
total_sales = np.sum(sales, axis=1)

print("Total sales of each product:")
print(total_sales)


# 2. Average monthly sales for every product
average_sales = np.mean(sales, axis=1)

print("\nAverage monthly sales:")
print(average_sales)


# 3. Best-selling product
best_product = np.argmax(total_sales)

print("\nBest-selling product:")
print("Product", best_product + 1)
print("Total sales:", total_sales[best_product])


# 4. Worst-selling product
worst_product = np.argmin(total_sales)

print("\nWorst-selling product:")
print("Product", worst_product + 1)
print("Total sales:", total_sales[worst_product])


# 5. Highest sales in each month
highest = np.max(sales, axis=0)

print("\nHighest sales in each month:")
print(highest)


# 6. Lowest sales in each month
lowest = np.min(sales, axis=0)

print("\nLowest sales in each month:")
print(lowest)


# 7. Products whose average sales are greater than 120
above_120 = np.where(average_sales > 120)

print("\nProducts with average sales greater than 120:")
print(above_120[0] + 1)


# 8. Total sales for each month
monthly_total = np.sum(sales, axis=0)

print("\nTotal sales for each month:")
print(monthly_total)


# 9. Standard deviation of monthly sales
std = np.std(sales, axis=0)

print("\nStandard deviation of monthly sales:")
print(std)


# 10. High / Low product classification
product_status = np.where(
    average_sales > 120,
    "High",
    "Low"
)

print("\nProduct classification:")
print(product_status)


# 11. Create Pandas DataFrame
df = pd.DataFrame({
    "Product": ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"],
    "Total Sales": total_sales,
    "Average Sales": average_sales
})

print("\nProduct DataFrame:")
print(df)


# 12. Sort DataFrame according to Total Sales
df = df.sort_values("Total Sales", ascending=False)

print("\nDataFrame sorted by Total Sales:")
print(df)