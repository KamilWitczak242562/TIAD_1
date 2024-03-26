import math
import random
import numpy as np

g_cognitive_const = 1.8  # od 0 do 2 malec
g_social_const = 0.4  # nie wiem rosnac
g_inertia = 0.9  # od 0 do 1 malec


class Particle:
    def __init__(self, x, inertia, cognitive_const, social_const, function):
        self.x = x()
        self.y = function(self.x)
        self.adaptation = math.inf
        self.velocity = 0
        self.best_x = self.x
        self.best_y = self.y
        self.best_adaptation = math.inf
        self.inertia = inertia
        self.cognitive_constant = cognitive_const
        self.social_const = social_const
        self.function = function

    def update_adap(self):
        self.adaptation = self.function(self.x)
        if self.adaptation < self.best_adaptation:
            self.best_adaptation = self.adaptation
            self.best_x = self.x
            self.best_y = self.adaptation


class Swarm:
    def __init__(self, x, amount, function):
        self.particles = [
            Particle(x, g_inertia, g_cognitive_const, g_social_const,
                     function) for _ in range(amount)]

    def __iter__(self):
        return iter(self.particles)


def best_in_swarm(swarm):
    best_adap = math.inf
    best_particle = None
    for particle in swarm:
        particle.update_adap()
    for particle in swarm:
        if particle.adaptation < best_adap:
            best_adap = particle.adaptation
            best_particle = particle
    return best_particle


def calc_inertia(velocity):
    return g_inertia * velocity


def calc_cognitive_acceleration():
    return g_cognitive_const * random.uniform(0, 1)


def calc_social_acceleration():
    return g_social_const * random.uniform(0, 1)


def calc_distance(best_x, best_y, x, y):
    return np.sqrt((np.subtract(best_x, x)) ** 2 + (best_y - y) ** 2)


def calc_cognitive_component(best_x_particle, best_y_particle, x_particle, y_particle):
    acceleration = calc_cognitive_acceleration()
    distance = calc_distance(best_x_particle, best_y_particle, x_particle, y_particle)
    return acceleration * distance


def calc_social_component(best_x_swarm, best_y_swarm, x_particle, y_particle):
    acceleration = calc_social_acceleration()
    distance = calc_distance(best_x_swarm, best_y_swarm, x_particle, y_particle)
    return acceleration * distance


def update_particle(best_x_swarm, best_y_swarm, particle):
    inertia = calc_inertia(particle.velocity)
    cognitive_const = calc_cognitive_component(particle.best_x, particle.best_y, particle.x, particle.y)
    social_const = calc_social_component(best_x_swarm, best_y_swarm, particle.x, particle.y)
    particle.velocity = inertia + cognitive_const + social_const
    particle.x = np.add(particle.x, particle.velocity)
    particle.y = np.add(particle.y, particle.velocity)


max_iter_without_improvement = 6000
iter_since_last_improvement = 0


def run_pso_simulation(x, iterations, amount, function):
    swarm = Swarm(x, amount, function)
    previous_best_adaptation = math.inf
    iter = 0
    global g_cognitive_const
    global g_social_const
    global g_inertia
    global iter_since_last_improvement

    # change_cog = (g_cognitive_const - 0.4) / iterations
    # change_soc = (1.5 - g_social_const) / iterations
    # change_inertia = (g_inertia - 0.5) / iterations

    current_best_particle = best_in_swarm(swarm)

    for _ in range(iterations):
        iter += 1
        current_best_particle = best_in_swarm(swarm)

        if current_best_particle.adaptation < previous_best_adaptation:
            previous_best_adaptation = current_best_particle.adaptation
            iter_since_last_improvement = 0
        else:
            iter_since_last_improvement += 1

        if iter_since_last_improvement >= max_iter_without_improvement:
            print(f"Algorytm zatrzymany z powodu stagnacji. Najlepsza adaptacja: {previous_best_adaptation}")
            break

        for particle in swarm:
            update_particle(current_best_particle.x, current_best_particle.y, particle)

        g_cognitive_const = 1.8 - 1.5 * (iter / iterations)
        g_inertia = 0.9 - 0.5 * (iter / iterations)
        g_social_const = 0.4 + 1.5 * (iter / iterations)

    return current_best_particle
