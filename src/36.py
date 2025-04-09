def is_divisible_by_7(n):
    """
    Check if a number n is divisible by 7.
    
    Args:
    n (int): The number to check
    
    Returns:
    bool: True if n is divisible by 7, False otherwise
    """
    return n % 7 == 0

# Example usage and verification
number = int(input("Enter a number to check if it's divisible by 7: "))
result = is_divisible_by_7(number)
print(f"The number {number} is divisible by 7: {result}")
