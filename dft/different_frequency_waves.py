import numpy as np
import matplotlib.pyplot as plt

# Setting up the plot
x = np.linspace(0, 1, 1000)

# How many samples?
n = 20
fig, ax = plt.subplots(n, 1)

# For gradient
grad = np.linspace(0, 1, n)

# Plotting pure sine waves for each frequency
for i in range(1, n+1):
    y = sin1 = np.sin((x * 2 * np.pi) * i)
    ax[i-1].plot(x, y, c=(grad[i-1], 0, 0))
    ax[i-1].set_axis_off()

plt.show()