import math

def calculate_area_rectangle(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The area of the rectangle.
    """
    return length * width

def calculate_volume_cuboid(length, width, height):
    """
    Calculate the volume of a cuboid.
    
    Args:
        length (float): The length of the cuboid.
        width (float): The width of the cuboid.
        height (float): The height of the cuboid.
        
    Returns:
        float: The volume of the cuboid.
    """
    return length * width * height

def main():
    # Example usage
    length = 5.0
    width = 3.0
    height = 4.0
    area_rectangle = calculate_area_rectangle(length, width)
    volume_cuboid = calculate_volume_cuboid(length, width, height)
    
    print(f"The area of the rectangle is: {area_rectangle:.2f}")
    print(f"The volume of the cuboid with dimensions {length}x{width}x{height} is: {volume_cuboid:.2f}")

if __name__ == "__main__":
    main()
