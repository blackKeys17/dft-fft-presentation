import numpy as np
import matplotlib.pyplot as plt

freq1 = 3
freq2 = 5
sample = np.linspace(0, 1, 20)
freqs = np.linspace(0, 19, 20)
sampled = np.sin((sample * 2 * np.pi) * freq1) + np.sin((sample * 2 * np.pi) * freq2)

transformed = np.fft.fft(sampled)
modulus = np.abs(transformed)
plt.bar(freqs, modulus)

plt.show()