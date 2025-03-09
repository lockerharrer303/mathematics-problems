import random

def get_random_math_problem():
    numbers = [1, 2, 3, 4, 5]
    operators = ["+", "-", "*", "/"]
    problem = ""
    for i in range(len(numbers)):
        problem += str(numbers[i]) + " " + operators[random.randint(0, len(operators) - 1)] + " "
    problem += str(numbers[random.randint(0, len(numbers) - 1)])
    return problem
