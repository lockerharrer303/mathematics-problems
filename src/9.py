import random

def get_random_math_problem(numbers=range(10), operations=['+', '-', '*', '/']):
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    operation = random.choice(operations)
    answer = eval(f"{num1} {operation} {num2}")
    return f"What is {num1} {operation} {num2}?"

# Example usage:
print(get_random_math_problem())