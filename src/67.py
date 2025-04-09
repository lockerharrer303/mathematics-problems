def sum_of_squares(n):
    """
    Calculate the sum of squares of first n natural numbers.
    
    Parameters:
    n (int): Natural number representing the count of natural numbers to be squared and summed.
    
    Returns:
    int: Sum of squares of first n natural numbers.
    """
    return (n * (n + 1) * (2 * n + 1)) // 6

sum_of_squares(5)
