import numpy as np
import matplotlib.pyplot as plt

# Create 500 theta values from 0 to 2π
theta = np.linspace(0, 2 * np.pi, 500)

# Define r values
r1 = 3 - 2 * np.cos(theta)
r2 = 4 + 3 * np.sin(theta)

# Create side-by-side polar plots
fig, axes = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})

# Left plot
axes[0].plot(theta, r1, color='blue')
axes[0].set_title("r = 3 - 2cos(θ)")
axes[0].grid(True)

# Right plot
axes[1].plot(theta, r2, color='red')
axes[1].set_title("r = 4 + 3sin(θ)")
axes[1].grid(True)

plt.show()
