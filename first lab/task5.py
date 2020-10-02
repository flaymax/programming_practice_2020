import numpy as np
import matplotlib.pyplot as plt

x = np.array((1, 2, 3, 4, 5, 6))
y = np.array((.99, 1.4, 1.97, 2.2, 2.05, 2.76))

p1, i = np.polyfit(x, y, deg=1, cov=True)
polynomial_1 = np.poly1d(p1)
y_p1 = polynomial_1(x)

p2, i = np.polyfit(x, y, deg=2, cov=True)
polynomial_2 = np.poly1d(p2)
y_p2 = polynomial_2(x)


plt.plot(x, y, '--o')
plt.plot(x, y_p1, 'r-')
plt.plot(x, y_p2)
plt.xlim(0, 8)
plt.show()
