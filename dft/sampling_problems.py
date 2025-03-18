import numpy as np
import matplotlib.pyplot as plt

# Setting up the plot
x = np.linspace(0, 1, 1000)
y4 = sin1 = np.sin((x * 2 * np.pi) * 4)
y16 = sin1 = np.sin((x * 2 * np.pi) * 16)

samples = np.linspace(0, 1, 20)
y4_samples = np.sin((samples * 2 * np.pi) * 4)
y16_samples = np.sin((samples * 2 * np.pi) * 16)

fig, ax = plt.subplots(2, 1)

ax[0].plot(x, y4, c="black")
ax[0].scatter(samples, y4_samples, c="red", s=160)

ax[1].plot(x, y16, c="black")
ax[1].scatter(samples, y16_samples, c="red", s=160)

plt.show()