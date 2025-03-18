import numpy as np
import matplotlib.pyplot as plt

sample = np.linspace(0, 1, 20)
freq1 = 2

sine = np.sin((sample * 2 * np.pi) * freq1)
cosine = np.cos((sample * 2 * np.pi) * freq1)

plt.plot(sample, sine, c="black")
plt.plot(sample, cosine, c="red")
plt.scatter(sample, sine, c="black", s=160)
plt.scatter(sample, cosine, c="red", s=160)

print(np.dot(sine, cosine))
plt.show()