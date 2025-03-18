import numpy as np
import matplotlib.pyplot as plt

# Setting up the plot
sample = np.linspace(0, 1, 20)
freq1 = 3
freq2 = 5
sampled1 = np.sin((sample * 2 * np.pi) * freq1)
sampled2 = np.sin((sample * 2 * np.pi) * freq2)

plt.plot(sample, sampled1, c="red")
plt.plot(sample, sampled2, c="blue")
print(np.dot(sampled1, sampled1))
print(np.dot(sampled1, sampled2))

plt.show()