import math
import numpy as np

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage:
distance = calculate_distance(0, 0, 3, 4)
print(f"The distance between the points A(0, 0) and B(3, 4) is: {distance:.2f}")
