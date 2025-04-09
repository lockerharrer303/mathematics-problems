import math

def calculate_surface_area(shape):
    """
    Calculate the surface area of a given shape.
    
    Parameters:
    shape (str): The type of shape ("circle", "rectangle", "triangle").
    
    Returns:
    float: The calculated surface area.
    """
    if shape == "circle":
        radius = input("Enter the radius of the circle:")
        return 2 * math.pi * float(radius)
    elif shape == "rectangle":
        length = input("Enter the length of the rectangle:")
        width = input("Enter the width of the rectangle:")
        return 2 * (length + width)
    elif shape == "triangle":
        base = input("Enter the base of the triangle:")
        height = input("Enter the height of the triangle:")
        return 0.5 * base * math.tan(math.radians(height))
    else:
        print(f"Unsupported shape: {shape}.")
        return None

# Example usage
print(calculate_surface_area("circle"))
print(calculate_surface_area("rectangle"))
print(calculate_surface_area("triangle"))
