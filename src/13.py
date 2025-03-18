  import random

def get_random_mathematics_problem(difficulty):
    # Generate a random problem based on the difficulty level
    if difficulty == "easy":
        # Easy problems have a maximum of two numbers and are typically addition or subtraction problems
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operation = random.choice(["+", "-"])
        problem = f"{num1} {operation} {num2} = ?"
        answer = int(eval(problem))
    elif difficulty == "medium":
        # Medium problems have a maximum of three numbers and can include multiplication, division, or subtraction
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        num3 = random.randint(0, 10)
        operation = random.choice(["+", "-", "*", "/"])
        problem = f"{num1} {operation} {num2} {operation} {num3} = ?"
        answer = int(eval(problem))
    elif difficulty == "hard":
        # Hard problems have a maximum of four numbers and can include any operation
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        num3 = random.randint(0, 10)
        num4 = random.randint(0, 10)
        operation1 = random.choice(["+", "-", "*", "/"])
        operation2 = random.choice(["+", "-", "*", "/"])
        problem = f"{num1} {operation1} {num2} {operation2} {num3} {operation2} {num4} = ?"
        answer = int(eval(problem))
    else:
        # Default to easy problems if difficulty level is not specified or is invalid
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operation = random.choice(["+", "-"])
        problem = f"{num1} {operation} {num2} = ?"
        answer = int(eval(problem))
    return {"problem": problem, "answer": answer}