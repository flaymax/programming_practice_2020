import matplotlib.pyplot as plt
import numpy as np

function = input()
x = np.arange(-10, 10.01, 0.01)
#plt.plot(x, eval(function))

with plt.xkcd():
    plt.plot(x, eval(function))

plt.grid()
plt.show()