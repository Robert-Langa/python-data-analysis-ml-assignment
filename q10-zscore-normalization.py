import numpy as np

# Z-score normalization function
def zscore_normalize(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data - mean) / std

# Load CSV into numpy array (skip header if it exists)
data = np.loadtxt("q10-raw-data.csv", delimiter=",", skiprows=1)

# Normalize
normalized_data = zscore_normalize(data)

# Output rows 10-15, columns 3-5
subset = normalized_data[9:15, 2:5]
print(subset)

# Write entire 2nd column to CSV
second_column = normalized_data[:, 1]
np.savetxt("q10-normalized-column.csv", second_column, delimiter=",")
