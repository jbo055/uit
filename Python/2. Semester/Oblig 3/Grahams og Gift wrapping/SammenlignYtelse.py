import random
import time

import sys
sys.path.append("Python/2. Semester/Oblig 3")
from Exercise16_12_grahams_liang import get_convex_hull as graham_scan
from Exercise16_11_gift_wrapping_liang import get_convex_hull as gift_wrapping


def generate_random_points(size):
    points = []
    for i in range(size):
        x = random.random() * 100
        y = random.random() * 100
        points.append([x, y])
    return points

def measure_time(algorithm, points):
    start_time = time.time()
    hull = algorithm(points)
    end_time = time.time()
    return end_time - start_time

sizes = [100, 1000, 10000, 100000]

for size in sizes:
    points = generate_random_points(size)
    print(f"\nSize: {size}")
    print(f"Graham's Scan: {measure_time(graham_scan, points)} seconds")
    print(f"Gift Wrapping: {measure_time(gift_wrapping, points)} seconds")
    
# Kommentar:
# Jeg har ikke testet for 100 000 points, siden det tar for lang tid. Jeg har testet for 100, 1000 og 10 000 points.
# Gift Wrapping er mye raskere enn Graham's Scan. 

# Etter jeg fikset feilen i Exercise16_12_grahams_liang.py, så er Graham's Scan raskere enn Gift Wrapping.

# Her er den fiksede koden:
# def sort_on_angles(S):
#     S[1:] = sorted(S[1:], key=lambda p: (math.atan2(p[1] - S[0][1], p[0] - S[0][0]), -distance(S[0][0], S[0][1], p[0], p[1])))