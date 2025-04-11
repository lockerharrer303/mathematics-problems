def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    - radius (float): The radius of the circle.
    
    Returns:
    - float: The area of the circle.
    """
    return 3.14159 * radius ** 2

# Example usage
radius = 7
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
