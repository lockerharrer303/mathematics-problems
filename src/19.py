def cube_of_sum(n):
    """
    Calculate the sum of cubes of first n natural numbers.
    
    Parameters:
        n (int): Natural number to calculate the sum of cubes
    
    Returns:
        int: Sum of cubes of first n natural numbers
    """
    # Formula for sum of cubes of first n natural numbers
    return (n * (n + 1) // 2) ** 2

# Example usage
n = 5
result = cube_of_sum(n)
print(f"The sum of cubes of the first {n} natural numbers is: {result}")
