def calculate_squares(num):
    """
    Calculate squares up to the given number.
    """
    result = []
    for i in range(1, num + 1):
        result.append(i * i)
    return result

num = 5
squares = calculate_squares(num)
print(squares)
