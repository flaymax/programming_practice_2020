import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 20)
x = np.arange(-2, 2, 0.001)
y = 0

for i in n:
    y += pow(0.5, i) * np.cos(pow(3, i) * np.pi * x)

plt.plot(x, y)
plt.title(r'Weierstraß')
plt.axis('equal')
plt.xlabel(r'$x$')
plt.ylabel(r'$W(x)$')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid()
plt.show()