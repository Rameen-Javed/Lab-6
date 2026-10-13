import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a messy weather dataset
data = {
    "Date": [
        "2026-01-01", "2026-01-02", "2026-01-03",
        "2026-01-04", "2026-01-05", "2026-01-06",
        "2026-01-07", "2026-01-08", "2026-01-09",
        "2026-01-10", "2026-01-11", "2026-01-12",
        "2026-01-13", "2026-01-14", "2026-01-15",
        "2026-01-03"
    ],
    "City": [
        " Lahore", "LAHORE ", "Karachi", " islamabad",
        "KARACHI", "Lahore ", "Islamabad", "KARACHI ",
        "lahore", "Islamabad ", "Karachi", " LAHORE",
        "ISLAMABAD", "Karachi ", "lahore", "Karachi"
    ],
    "Temperature": [
        "25C", "27C", "30C", "22C", "32C",
        "26C", "21C", "31C", "28C", "23C",
        "33C", "29C", "20C", "34C", "27C", "30C"
    ],
    "Humidity": [
        60, 55, None, 70, 45, None, 75, 40,
        58, 68, None, 50, 80, 35, 57, None
    ],
    "Condition": [
        "sunny", " CLOUDY", "Rainy ", "SUNNY",
        " rainy", "Cloudy ", "SUNNY", "rainy",
        "Sunny ", "CLOUDY ", "sunny", "Cloudy",
        "sunny ", "Sunny", "CLOUDY", "Rainy"
    ]
}

df = pd.DataFrame(data)

# 2. Clean text columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# 3. Remove the temperature unit and convert to numbers
df["Temperature"] = (
    df["Temperature"]
    .str.replace("C", "", regex=False)
    .astype(float)
)

# 4. Convert dates from text to datetime
df["Date"] = pd.to_datetime(df["Date"])

# 5. Remove duplicate rows
df = df.drop_duplicates().copy()

print("Rows after dropping duplicates:", len(df))

# 6. Fill missing humidity with the median
humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)

print("Missing Humidity filled with median:", humidity_median)

# 7. One-hot encode Condition
df_encoded = pd.get_dummies(
    df, columns=["Condition"], dtype=int
)

print("\nEncoded Condition Columns:")
condition_columns = [
    col for col in df_encoded.columns
    if col.startswith("Condition_")
]
print(df_encoded[condition_columns].to_string(index=False))

# 8. Print the cleaned dataset
print("\nCleaned Weather Dataset:")
print(df.to_string(index=False))

# 9. Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])
print("\nCorrelation (Temperature, Humidity):",
      round(correlation, 2))

# 10. Count weather conditions
condition_counts = df["Condition"].value_counts()

print("\nCondition counts:")
print(condition_counts)

# 11. Create four plots in a 2 x 2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Plot 1: Temperature over time
axes[0, 0].plot(
    df["Date"], df["Temperature"], marker="o"
)
axes[0, 0].set_title("Temperature Over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)

# Plot 2: Temperature versus humidity
axes[0, 1].scatter(
    df["Temperature"], df["Humidity"]
)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity")

# Plot 3: Number of days per condition
axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Weather Condition Share")

# Plot 4: Temperature distribution
axes[1, 1].hist(
    df["Temperature"], bins=5, edgecolor="black"
)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

# 12. Add overall title and save dashboard
fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()

print("\nSaved weather_dashboard.png")
