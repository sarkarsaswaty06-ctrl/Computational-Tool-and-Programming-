
import matplotlib.pyplot as plt

# Monthly sales data
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

sales = [
    45000, 52000, 48000, 61000, 58000, 65000,
    62000, 70000, 68000, 75000, 72000, 80000
]

# Find highest and lowest sales
max_sales = max(sales)
min_sales = min(sales)

highest_month = months[sales.index(max_sales)]
lowest_month = months[sales.index(min_sales)]

# Create two charts
plt.figure(figsize=(12, 5))

# Line chart
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Revenue - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True)
plt.xticks(rotation=45)

# Bar chart
plt.subplot(1, 2, 2)
plt.bar(months, sales)
plt.title("Monthly Sales Revenue - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Display results
print("Highest Sales:", highest_month, "₹", max_sales)
print("Lowest Sales:", lowest_month, "₹", min_sales)
