import math

def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

radius = 5.0
height = 10.0
volume = calculate_cylinder_volume(radius, height)
print(f"The volume of the cylinder with radius {radius} and height {height} is: {volume:.2f}")
