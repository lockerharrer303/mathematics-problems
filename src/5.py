import random

def get_random_math_problem():
    operands = [2, 5, 10, 17, 23, 42]
    operator = ["+", "-", "*", "/"]
    problem = f"{operands[random.randint(0, len(operands) - 1)]} {operator[random.randint(0, len(operator) - 1)]} {operands[random.randint(0, len(operands) - 1)]}"
    return problem