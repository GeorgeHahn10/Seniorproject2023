import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)

ax.plot(y, color='blue', label='Sine wave')
ax.plot(z, color='black', label='Cosine wave')

plt.xlim([25, 50])
plt.show()