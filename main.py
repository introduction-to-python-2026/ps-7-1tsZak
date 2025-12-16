import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# Country-level aggregated data
# -----------------------------------
data = {
    "Country": [
        "Finland", "Denmark", "Sweden", "Norway",
        "Germany", "France", "United Kingdom", "Italy",
        "United States", "Canada", "Australia",
        "Japan", "South Korea",
        "Brazil", "Mexico", "Argentina",
        "India", "China", "Indonesia",
        "South Africa", "Nigeria", "Kenya",
        "Russia", "Turkey", "Hungary"
    ],
    "Political_Ideology": [
        2.5, 2.8, 3.0, 2.7,
        4.5, 4.2, 5.0, 5.3,
        6.0, 4.8, 5.2,
        5.5, 5.8,
        5.0, 5.6, 5.2,
        6.5, 6.8, 6.2,
        6.0, 6.9, 6.4,
        7.0, 6.7, 6.6
    ],
    "Happiness_Score": [
        7.8, 7.6, 7.4, 7.5,
        7.1, 6.8, 6.9, 6.4,
        6.9, 7.2, 7.0,
        6.4, 6.5,
        6.1, 6.3, 6.2,
        4.2, 5.1, 5.3,
        5.0, 4.8, 5.1,
        5.5, 5.4, 5.6
    ]
}

df = pd.DataFrame(data)

# -----------------------------------
# Scatter Plot with country labels
# -----------------------------------
plt.figure(figsize=(10,6))
plt.scatter(df["Political_Ideology"], df["Happiness_Score"], color='green', alpha=0.8)
for i, country in enumerate(df["Country"]):
    plt.text(df["Political_Ideology"][i]+0.05, df["Happiness_Score"][i]+0.05, country, fontsize=8)
plt.xlabel("Political Ideology (Left → Right)")
plt.ylabel("Happiness Score")
plt.title("Scatter Plot: Political Ideology vs Happiness")
plt.grid(True)
plt.show()

# -----------------------------------
# Histogram: Frequency of Political Ideology
# -----------------------------------
plt.figure(figsize=(10,6))
plt.hist(df["Political_Ideology"], bins=8, color='blue', edgecolor='black')
plt.xlabel("Political Ideology (Left → Right)")
plt.ylabel("Number of Countries")
plt.title("Histogram: Frequency of Political Ideology")
plt.grid(axis='y', alpha=0.75)
plt.show()

