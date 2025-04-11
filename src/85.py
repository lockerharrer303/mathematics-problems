import math

# Example of how to calculate the area of a triangle using Heron's formula
def calculate_triangle_area(base, height):
    s = (base + height) / 2  # semi-perimeter
    area = math.sqrt(s * (s - base) * (s - height))
    return area

# Example usage:
triangle_base = 3.0
triangle_height = 4.0
area_of_triangle = calculate_triangle_area(triangle_base, triangle_height)
print(f"The area of the triangle with sides {triangle_base} and {triangle_height} is: {area_of_triangle}")
