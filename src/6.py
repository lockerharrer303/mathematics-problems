import random
def get_random_math_problem(level):
    if level == 1:
        number1 = random.randint(0, 10)
        number2 = random.randint(0, 10)
        operation = random.choice(['+', '-', 'x'])
        answer = calculate_answer(number1, number2, operation)
        return f"{number1} {operation} {number2} = ?"
    elif level == 2:
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)
        operation = random.choice(['+', '-', 'x'])
        answer = calculate_answer(number1, number2, operation)
        return f"{number1} {operation} {number2} = ?"
    elif level == 3:
        number1 = random.randint(0, 1000)
        number2 = random.randint(0, 1000)
        operation = random.choice(['+', '-', 'x'])
        answer = calculate_answer(number1, number2, operation)
        return f"{number1} {operation} {number2} = ?"
    else:
        number1 = random.randint(0, 10000)
        number2 = random.randint(0, 10000)
        operation = random.choice(['+', '-', 'x'])
        answer = calculate_answer(number1, number2, operation)
        return f"{number1} {operation} {number2} = ?"
def calculate_answer(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    else:
        return number1 * number2