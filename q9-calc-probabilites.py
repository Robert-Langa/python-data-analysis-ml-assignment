import pandas as pd

# Create dataframe manually
data = {
    "Male": [30, 20],
    "Female": [10, 40]
}

index = ["Overweight", "Target"]

df = pd.DataFrame(data, index=index)

# Total population
total = df.values.sum()

# Compute probabilities
prob_overweight = df.loc["Overweight"].sum() / total
prob_male = df["Male"].sum() / total
prob_overweight_male = df.loc["Overweight", "Male"] / total
prob_target_or_female = (
    df.loc["Target"].sum() + df["Female"].sum() - df.loc["Target", "Female"]
) / total

# Sparse output for assignment
print(f"Overweight: {prob_overweight:.2f}")
print(f"Male: {prob_male:.2f}")
print(f"Overweight Male: {prob_overweight_male:.2f}")
print(f"Target or Female: {prob_target_or_female:.2f}")

