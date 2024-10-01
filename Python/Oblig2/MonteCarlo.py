import random

def monte_carlo():
    number_of_hits = 0
    for i in range(1000000):
        circle_point_x = random.uniform(-1, 1)
        circle_point_y = random.uniform(-1, 1)
        if circle_point_x**2 + circle_point_y**2 <= 1:
            number_of_hits += 1
    return 4 * number_of_hits / 1000000

print (monte_carlo())

