import numpy as np
import matplotlib.pyplot as plt

# To plot the curve
x = np.linspace(0, 1, 1000)

# Sum of 2 sine waves
freq1 = 3
freq2 = 5
sin1 = np.sin((x * 2 * np.pi) * freq1)
sin2 = np.sin((x * 2 * np.pi) * freq2)

sample = np.linspace(0, 1, 20)
sampled = np.sin((sample * 2 * np.pi) * freq1) + np.sin((sample * 2 * np.pi) * freq2)

plt.plot(x, sin1 + sin2)
plt.scatter(sample, sampled)
plt.show()
