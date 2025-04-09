import math

def calculate_area(shape):
    if shape == "circle":
        radius = float(input("Enter the radius: "))
        area = math.pi * (radius ** 2)
        print(f"The area of the circle is {area:.2f}")
    elif shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"The area of the rectangle is {area:.2f}")
    else:
        print("Invalid shape.")

calculate_area("circle")
