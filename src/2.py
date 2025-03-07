import math

def get_random_mathematical_expression(max_operators):
    operators = ["+", "-", "*", "/"]
    numbers = [1, 2, 3, 4, 5]
    expression = ""
    for i in range(max_operators):
        operator = random.choice(operators)
        number = random.choice(numbers)
        expression += f" {operator} {number}"
    return expression