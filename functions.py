import numpy as np


def sphere():
    x = np.random.uniform(-100, 100, 400)
    y = []
    for i in range(400):
        z = 0
        for j in range(30):
            z = z + (x[i] ** 2)
        y.append(z)
    return y


def rastrigin():
    x = np.random.uniform(-5.12, 5.12, 50)
    y = []
    for i in range(50):
        z = 0
        for j in range(30):
            z = z + (x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i]) + 10)
        y.append(z)
    return y


def alpine():
    x = np.random.uniform(-10, 10, 100)
    y = []
    for i in range(100):
        z = 0
        for j in range(30):
            z = z + np.abs((x[i] * np.sin(x[i]) + 0.1 * x[i]))
        y.append(z)
    return y

def schwefel():
    x = np.random.uniform(-100, 100, 400)
    y = []
    for i in range(400):
        z = 0
        for j in range(30):
            z = z + np.abs(x[i] * np.sin(np.sqrt(np.abs(x[i]))))
        y.append(z)
    return y

def bohachevsky():
    x = np.random.uniform(-10, 10, 100)
    y = []
    # ??????????
    for i in range(99):
        z = 0
        for j in range(30):
            z = z + (x[i] ** 2 + 2 * x[i+1] ** 2 - 0.3 * np.cos(3 * np.pi * x[i]))
        y.append(z)
    return y

def elliptic():
    x = np.random.uniform(-100, 100, 400)
    y = []
    for i in range(400):
        z = 0
        for j in range(30):
            z = z + ((10**6)**((i - 1)/(30-1))*x[i]**2)
        y.append(z)
    return y

