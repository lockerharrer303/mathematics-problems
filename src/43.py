import math
import numpy as np

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def reverse_string(string):
    return string[::-1]

# Example usage:
print(sum_of_squares(3))  # Output: 5
print(is_prime(7))      # Output: True
print(fibonacci_sequence(6))  # Output: [0, 1, 1, 2, 3, 5]
print(reverse_string("hello"))  # Output: "olleh"
