import math

def calculate_area(base, height):
    """
    Calculate the area of a rectangle.
    
    Args:
    base (float): The length of the base of the rectangle.
    height (float): The height of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return base * height

# Example usage
base = 5.0
height = 3.0
area = calculate_area(base, height)
print(f"The area is: {area:.2f}")
