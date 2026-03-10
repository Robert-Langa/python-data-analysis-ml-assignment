import numpy as np
import matplotlib.pyplot as plt

# Define normal distribution function
def normal_pdf(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * \
           np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Generate x values
x = np.linspace(-10, 10, 1000)

# Compute curves
y1 = normal_pdf(x, 0, 1)
y2 = normal_pdf(x, 2, 0.5)
y3 = normal_pdf(x, -2, 5)
y4 = normal_pdf(x, 0, 0.25)

# Plot all on same axes
plt.plot(x, y1, color='blue', linestyle='-', label='μ=0, σ=1')
plt.plot(x, y2, color='red', linestyle='--', label='μ=2, σ=0.5')
plt.plot(x, y3, color='gold', linestyle='-.', label='μ=-2, σ=5')
plt.plot(x, y4, color='purple', linestyle=':', label='μ=0, σ=0.25')

# Formatting
plt.title("Normal Distribution Curves")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)

plt.show()
