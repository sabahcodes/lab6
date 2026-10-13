import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Messy weather log (15 din + 1 duplicate row)
data = {
    "Date": ["2026-10-01", "2026-10-02", "2026-10-03", "2026-10-04", "2026-10-05",
             "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09", "2026-10-10",
             "2026-10-11", "2026-10-12", "2026-10-13", "2026-10-14", "2026-10-15",
             "2026-10-05"],
    "City": [" lahore", "LAHORE", "Lahore ", "lahore", " Lahore",
             "LAHORE ", "Lahore", "lahore ", " lahore", "Lahore",
             "LAHORE", "lahore", " Lahore", "Lahore ", "lahore",
             " Lahore"],
    "Temperature": ["32C", "30C", "28C", "33C", "34C",
                    "27C", "31C", "35C", "29C", "33C",
                    "26C", "30C", "34C", "32C", "28C",
                    "34C"],
    "Humidity": [45, 50, np.nan, 40, np.nan,
                 65, 55, 38, 60, np.nan,
                 70, 52, 42, 48, 58,
                 np.nan],
    "Condition": ["sunny", " Rainy", "CLOUDY ", "Sunny", "sunny ",
                  "rainy", "Cloudy", "SUNNY", "cloudy", "Sunny",
                  "Rainy", " Cloudy", "sunny", "SUNNY", "cloudy ",
                  "sunny "],
}

df = pd.DataFrame(data)

# (a) Cleaning
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
df = df.drop_duplicates()
print("Rows after dropping duplicates:", len(df))

median_h = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_h)
print("Missing Humidity filled with median:", median_h)

# (b) One-hot encoding
df_encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)
print(df_encoded.filter(like="Condition_").head())

# (d) Correlation
corr = df["Temperature"].corr(df["Humidity"])
print("Correlation (Temperature, Humidity):", round(corr, 2))

# (e) Condition counts
counts = df["Condition"].value_counts()
print("Condition counts:")
print(counts)

# (c), (d), (e), (f) 2 x 2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].plot(df["Date"], df["Temperature"], marker="o", color="steelblue")
axes[0, 0].set_title("Temperature over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].scatter(df["Temperature"], df["Humidity"], color="darkorange", s=60)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity (%)")
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].pie(counts.values, labels=counts.index, autopct="%1.1f%%", startangle=90)
axes[1, 0].set_title("Days per Condition")

axes[1, 1].hist(df["Temperature"], bins=5, color="seagreen", edgecolor="white")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()
print("Saved weather_dashboard.png")