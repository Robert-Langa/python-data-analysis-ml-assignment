import pandas as pd

# Load CSV and strip extra spaces from column names
df = pd.read_csv("q8-standings-data.csv")
df.columns = df.columns.str.strip()  # remove any accidental spaces

# Rename columns to match variable names for convenience
df.rename(columns={
    "Runs Scored": "RunsScored",
    "Runs Allowed": "RunsAllowed"
}, inplace=True)

# Compute Scoring Ratio
df["ScoringRatio"] = df["RunsScored"] / df["RunsAllowed"]

# Predicted Winning Percentage (Pythagorean Theorem)
df["PredictedWinningPercentage"] = (df["ScoringRatio"] ** 2) / (1 + df["ScoringRatio"] ** 2)

# Actual Winning Percentage
df["ActualWinningPercentage"] = df["Wins"] / (df["Wins"] + df["Losses"])

# Absolute Error
df["AbsoluteError"] = abs(df["PredictedWinningPercentage"] - df["ActualWinningPercentage"])

# Mean Absolute Deviation
mad = df["AbsoluteError"].mean()

# Print first 5 rows
print(df.head())

# Print MAD
print(f"MAD: {mad:.4f}")

# Is MAD < 2%?
print("Yes" if mad < 0.02 else "No")
