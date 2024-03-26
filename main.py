import numpy as np

import functions as f
from pso import run_pso_simulation


if __name__ == '__main__':
    best = run_pso_simulation(f.x_sphere, 100000, 10000, f.sphere)
    print(best.y)



