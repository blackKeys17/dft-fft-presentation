import numpy as np
import matplotlib.pyplot as plt

sample = np.linspace(0, 1, 20)
grid = np.ndarray((20, 20))

waves = []
for i in range(0, 20):
    y = sin1 = np.cos((sample * 2 * np.pi) * i)
    waves.append(y)

for i in range(20):
    for j in range(20):
        grid[i][j] = np.dot(waves[i], waves[j])

plt.imshow(grid, cmap="Greens")
plt.show()