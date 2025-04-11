def find_common_factors(x, y):
    """
    Find common factors between two positive integers x and y.
    
    Args:
    - x: An integer
    - y: Another integer
    
    Returns:
    - A list of all common factors of x and y, sorted in ascending order.
    """
    # Get the smallest prime factor of both numbers
    min_factor = min(x, y)
    for i in range(min_factor + 1, x + y):
        if x % i == 0 and y % i == 0:
            return [i]
    return []

# Example usage
x = 18
y = 24
print(find_common_factors(x, y))
