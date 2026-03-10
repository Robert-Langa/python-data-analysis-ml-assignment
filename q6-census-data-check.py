import pandas as pd
import matplotlib.pyplot as plt

# Load census data
df = pd.read_csv("census.csv")

# Filter Canada, both sexes
df_filtered = df.query("`Geographic name` == 'Canada' and Sex == 'Both sexes'")
df_filtered = df_filtered.sort_values("Census Years")
df_filtered["Census Years"] = df_filtered["Census Years"].astype(int)

# Convert percentages to float
for col in ["0 to 14 years (% distribution)",
            "15 to 64 years (% distribution)",
            "65 years and over (% distribution)"]:
    df_filtered[col] = df_filtered[col].astype(float)

years = df_filtered["Census Years"]
percentages = df_filtered["65 years and over (% distribution)"]

# 1) Comma-separated percentages
print(",".join([f"{p:.2f}" for p in percentages]))

# 2) Year with max 65+
print(int(df_filtered.loc[percentages.idxmax(), "Census Years"]))

# 3) Always increasing?
print("Yes" if all(percentages.iloc[i] <= percentages.iloc[i + 1] for i in range(len(percentages)-1)) else "No")

# 4) Plot age groups
plt.figure(figsize=(10,6))
plt.plot(years, df_filtered["0 to 14 years (% distribution)"], marker='o', label="0-14 years")
plt.plot(years, df_filtered["15 to 64 years (% distribution)"], marker='s', label="15-64 years")
plt.plot(years, df_filtered["65 years and over (% distribution)"], marker='^', label="65+ years")
plt.xlabel("Census Year")
plt.ylabel("Percentage of Population")
plt.title("Canadian Population by Age Group (1921–2011)")
plt.xticks(years, rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
