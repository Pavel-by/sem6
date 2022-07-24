import numpy as np


def f(x1, x2, x3 = 0):
    return x1**2 + 2*x2**2 + 4*x1


def f1(x1, x2, x3 = 0):
    return np.array([2*x1 + 4, 4*x2])


def f2(x1, x2, x3 = 0):
    return np.matrix([
        [2, 0],
        [0, 4]
    ])


size = 2
x0 = [1, 3]


