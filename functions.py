import numpy as np


size = 30


def sphere(x):
    return np.sum(np.square(x))


def x_sphere():
    return np.random.uniform(-100, 100, size)


def rastrigin(x):
    y = 0
    for j in x:
        y = y + (j ** 2 - 10 * np.cos(2 * np.pi * j) + 10)
    return y


def x_rastrigin():
    return np.random.uniform(-5.12, 5.12, size)


def alpine(x):
    y = 0
    for j in x:
        y = y + np.abs((j * np.sin(j) + 0.1 * j))
    return y


def x_alpine():
    return np.random.uniform(-10, 10, size)


def schwefel(x):
    y = 0
    for j in x:
        y = y + np.abs(j * np.sin(np.sqrt(np.abs(j))))
    return y


def x_schwefel():
    return np.random.uniform(-100, 100, 29)


def bohachevsky(x):
    y = 0
    for index, j in enumerate(x):
        next_j = j[(index + 1) % len(j)]
        y = y + (j ** 2 + 2 * next_j ** 2 - 0.3 * np.cos(3 * np.pi * j))
    return y


def x_bohachevsky():
    return np.random.uniform(-10, 10, size)


def elliptic(x):
    y = 0
    for index, j in enumerate(x):
        y = y + ((10**6)**((index - 1)/(30-1))*j**2)
    return y


def x_elliptic():
    return np.random.uniform(-100, 100, size)
