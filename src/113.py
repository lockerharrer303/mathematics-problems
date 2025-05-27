def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Example usage
result1 = add(5, 3)
print("Result of addition is:", result1)

result2 = subtract(6, 4)
print("Result of subtraction is:", result2)

result3 = multiply(8, 7)
print("Result of multiplication is:", result3)

result4 = divide(9, 0)
if isinstance(result4, (float, int)):
    print("Result of division is: ", result4)
else:
    print("Error: Division by zero")
