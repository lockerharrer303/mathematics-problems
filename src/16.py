import math
a = 3.141592653589793
b = 4.0
c = 5.0

delta = b**2 - 4*a*c
x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)

print(f"x1: {x1}, x2: {x2}")
