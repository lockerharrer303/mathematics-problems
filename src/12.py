import random
import math

def get_random_math_problem():
    problem_type = random.choice(["addition", "subtraction", "multiplication", "division"])
    if problem_type == "addition":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return f"{a} + {b} = ?"
    elif problem_type == "subtraction":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return f"{a} - {b} = ?"
    elif problem_type == "multiplication":
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        return f"{a} x {b} = ?"
    else:
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        return f"{a} / {b} = ?"

# Test the function with a few examples
print(get_random_math_problem())
print(get_random_math_problem())
print(get_random_math_problem())