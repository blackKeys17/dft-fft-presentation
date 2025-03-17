import numpy as np
import matplotlib.pyplot as plt

# Setting up the plot
x = np.linspace(0, 1, 1000)

# How many samples?
n = 20
fig, ax = plt.subplots(n+1, 1)

# For gradient
grad = np.linspace(0, 1, n+1)

# Plotting pure sine waves for each frequency
for i in range(0, n+1):
    y = sin1 = np.sin((x * 2 * np.pi) * i)
    ax[i].plot(x, y, c=(grad[i], 0, 0))
    ax[i].set_axis_off()

plt.show()