import numpy as np


def sphere(x):
    y = 0
    for i in x:
        y = y + (i ** 2)
    return y

def x_sphere():
    return np.random.uniform(-100, 100, 5)

def rastrigin():
    x = [np.random.uniform(-5.12, 5.12, 29) for _ in range(40)]
    y = []
    for i in x:
        z = 0
        for j in i:
            z = z + (j ** 2 - 10 * np.cos(2 * np.pi * j) + 10)
        y.append(z)
    return y, x


def alpine():
    x = [np.random.uniform(-10, 10, 29) for _ in range(40)]
    y = []
    for i in x:
        z = 0
        for j in i:
            z = z + np.abs((j * np.sin(j) + 0.1 * j))
        y.append(z)
    return y, x

def schwefel():
    x = [np.random.uniform(-100, 100, 29) for _ in range(40)]
    y = []
    for i in x:
        z = 0
        for j in i:
            z = z + np.abs(j * np.sin(np.sqrt(np.abs(j))))
        y.append(z)
    return y, x

def bohachevsky():
    x = [np.random.uniform(-10, 10, 29) for _ in range(40)]
    y = []
    for i in x:
        z = 0
        for index, j in enumerate(i):
            next_j = i[(index + 1) % len(i)]
            z = z + (j ** 2 + 2 * next_j ** 2 - 0.3 * np.cos(3 * np.pi * j))
        y.append(z)
    return y, x

def elliptic():
    x = [np.random.uniform(-100, 100, 29) for _ in range(40)]
    y = []
    for i in x:
        z = 0
        for index, j in enumerate(i):
            z = z + ((10**6)**((index - 1)/(30-1))*j**2)
        y.append(z)
    return y, x

