import numpy as np
import matplotlib.pyplot as plt


def y(x):
    y = []
    for xx in x:
        if -5 <= xx <= 5:
            y += [xx * xx]
        elif xx < -5:
            y += [2 * np.absolute(xx) - 1]
        else:
            y += [2 * xx]
    return np.array(y)


x = np.arange(-10, 10.01, 1)
y = y(x)
plt.plot(x, y)
plt.xlim(-10, 10)
plt.grid()
plt.show()
