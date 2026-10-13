import pandas as pd
import matplotlib.pyplot as plt

# Messy inventory data (10 products)
data = {
    "Product":  ["Cola", "Chips", "Milk", "Biscuits", "Juice",
                 "Cheese", "Water", "Popcorn", "Yogurt", "Tea"],
    "Category": ["beverages ", "SNACKS", " Dairy", "Snacks", "beverages",
                 "DAIRY ", "Beverages", " snacks", "dairy", "BEVERAGES "],
    "Price":    ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 1,800",
                 "Rs. 950", "Rs. 60", "Rs. 150", "Rs. 220", "Rs. 1,100"],
    "Stock":    [40, 120, 60, 90, 35, 25, 200, 80, 70, 50],
}

df = pd.DataFrame(data)

# (a) Category clean karo
df["Category"] = df["Category"].str.strip().str.title()

# (b) Price ko number banao ("Rs. " aur commas hatao)
df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False)
df["Price"] = df["Price"].str.replace(",", "", regex=False).astype(float)

# (c) Label encoding
df["Category_Code"] = df["Category"].astype("category").cat.codes
print(df)

# (d) Bar plot + pie chart, ek figure mein
avg_price = df.groupby("Category")["Price"].mean()
stock_share = df.groupby("Category")["Stock"].sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(avg_price.index, avg_price.values, color=["#4C78A8", "#F58518", "#54A24B"])
axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")

axes[1].pie(stock_share.values, labels=stock_share.index,
            autopct="%1.1f%%", startangle=90)
axes[1].set_title("Share of Total Stock by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()
print("Saved inventory_plots.png")