import math

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

if __name__ == "__main__":
    length = 5.0
    width = 4.0
    area = calculate_area(length, width)
    print(f"The area of the rectangle with dimensions {length}x{width} is: {area}")
