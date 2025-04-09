def is_even(n):
    """
    Checks if a given integer n is even.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is even, False otherwise.
    """
    return n % 2 == 0

# Example usage:
even_number = is_even(4)  # Even
odd_number = is_even(5)   # Odd
