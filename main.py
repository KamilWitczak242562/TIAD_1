import numpy as np

import functions as f
from pso import run_pso_simulation


if __name__ == '__main__':
    a = run_pso_simulation(f.x_sphere(), 1000000, 100, f.sphere)
    print(a.best_y)
    y = f.sphere(f.x_sphere())
    print(y)


