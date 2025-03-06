def get_random_mathematical_expression():
    numbers = [1, 2, 3, 4, 5]
    operators = ["+", "-", "*", "/"]
    result = ""
    for i in range(4):
        result += str(numbers[randint(0, len(numbers) - 1)]) + " " + operators[randint(0, len(operators) - 1)] + " "
    return result
