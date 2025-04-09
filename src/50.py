def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        return sequence

# Example usage
print(fibonacci(10))
