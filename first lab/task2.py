import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x ** 2 - x - 6)
plt.xlim(-3, 4)  # задаем ограничения на отображаемую область по иксам и видем наши корни x = -2, x = 3
plt.grid()
plt.show()
