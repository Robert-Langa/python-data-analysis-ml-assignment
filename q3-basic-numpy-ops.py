import numpy as np

# Step 1: Create array
a = np.arange(1, 59, 3)

# Step 2: Scalar multiply by 11
a = a * 11

# Step 3: Reshape to 4x5
a = a.reshape(4, 5)

# Step 4: Update 3rd element of 2nd row to negative
a[1, 2] = -a[1, 2]

# Step 5: Update every odd element to 111
a[a % 2 == 1] = 111

# Step 6: Output column sums
print(np.sum(a, axis=0))

# Output row max values
print(np.max(a, axis=1))

# Step 7: Find index of minimum element
min_index = np.unravel_index(np.argmin(a), a.shape)

# Select bottom-right subarray
sub_array = a[min_index[0]:, min_index[1]:]

# Step 8: Blank line before sub-array
print()
print(sub_array)
