import math

def calculate_volume(radius, height):
    """
    Calculate the volume of a cylinder using its radius and height.
    
    Parameters:
    - radius: float, the radius of the cylinder's base in meters.
    - height: float, the height of the cylinder in meters.
    
    Returns:
    - volume: float, the calculated volume of the cylinder in cubic meters.
    """
    # Calculate volume using the formula: V = πr^2h
    volume = math.pi * radius ** 2 * height
    
    return volume

# Example usage and verification
if __name__ == "__main__":
    # Define sample values for radius and height
    radius = 3.0
    height = 5.0
    
    # Calculate the volume
    volume = calculate_volume(radius, height)
    
    print(f"The volume of the cylinder with radius {radius} meters and height {height} meters is: {volume:.2f} cubic meters.")
