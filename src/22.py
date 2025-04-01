def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    pi = 3.14
    
    # Calculating the area using the formula: π * r^2
    area = pi * (radius ** 2)
    
    return area

# Example usage and test cases
print("Area of a circle with radius 5:")
print(calculate_area(5))
