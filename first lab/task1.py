import numpy as np


def f(x):
    return np.log((1./(np.exp(np.sin(x)) + 1))/(5./4 + 1/(x ** 15))) / np.log(1 + x ** 2)


print(f(1), f(10),  f(1000))
