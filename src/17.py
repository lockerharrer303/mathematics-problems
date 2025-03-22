import math

def calculate_area_rectangle(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

def calculate_area_triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle given its base and height.
    
    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

def calculate_perimeter_rectangle(length: float, width: float) -> float:
    """
    Calculate the perimeter of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The perimeter of the rectangle.
    """
    return 2 * (length + width)

def calculate_circumference_circle(radius: float) -> float:
    """
    Calculate the circumference of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The circumference of the circle.
    """
    return 2 * math.pi * radius

def main():
    # Example usage
    length = 4.0
    width = 3.5
    area_rectangle = calculate_area_rectangle(length, width)
    print(f"Area of rectangle: {area_rectangle:.2f}")
    
    triangle_base = 7.0
    triangle_height = 1.0
    area_triangle = calculate_area_triangle(triangle_base, triangle_height)
    print(f"Area of triangle: {area_triangle:.2f}")
    
    perimeter_rectangle = calculate_perimeter_rectangle(length, width)
    print(f"Perimeter of rectangle: {perimeter_rectangle:.2f}")
    
    circumference_circle = calculate_circumference_circle(radius=5.0)
    print(f"Circumference of circle with radius 5.0: {circumference_circle:.2f}")

if __name__ == "__main__":
    main()
