import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a messy inventory dataset
data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Bread", "Water", "Cookies", "Yogurt", "Soda"
    ],
    "Category": [
        "beverages ", "SNACKS", " Dairy", "Snacks",
        "beverages", " BAKERY", "beverages ",
        "snacks ", "DAIRY", "Beverages"
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120",
        "Rs. 1,800", "Rs. 150", "Rs. 50",
        "Rs. 200", "Rs. 300", "Rs. 900"
    ],
    "Stock": [40, 120, 60, 100, 35, 80, 200, 70, 55, 45]
}

df = pd.DataFrame(data)

# 2. Clean category names
df["Category"] = df["Category"].str.strip().str.title()

# 3. Convert Price into numeric values
df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# 4. Encode categories with integer codes
df["Category_Code"] = (
    df["Category"].astype("category").cat.codes
)

# 5. Display the cleaned dataset
print("Cleaned Inventory Dataset:")
print(df.to_string(index=False))

# 6. Calculate average price for each category
avg_price = df.groupby("Category")["Price"].mean()

# 7. Calculate total stock for each category
stock_by_category = df.groupby("Category")["Stock"].sum()

print("\nAverage Price by Category:")
print(avg_price)

print("\nTotal Stock by Category:")
print(stock_by_category)

# 8. Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot: average price
axes[0].bar(avg_price.index, avg_price.values)
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=30)

# Pie chart: share of total stock
axes[1].pie(
    stock_by_category.values,
    labels=stock_by_category.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1].set_title("Category Share of Total Stock")

# 9. Adjust layout and save the figure
plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()

print("\nSaved inventory_plots.png")
