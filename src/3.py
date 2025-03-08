import random

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def solve_problem():
    min_value = 1
    max_value = 10
    number = get_random_number(min_value, max_value)
    print("What is " + str(number) + " times " + str(number) + "?")
    answer = int(input())
    if answer == number ** 2:
        print("Correct! The answer is " + str(number ** 2))
    else:
        print("Incorrect. The correct answer is " + str(number ** 2))

solve_problem()
