def fibonacci(n):
    """
    Generate a list containing the Fibonacci sequence up to the nth number.
    
    Parameters:
    n (int): The length of the Fibonacci sequence to generate.
    
    Returns:
    list: A list of integers representing the Fibonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

# Example usage
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
