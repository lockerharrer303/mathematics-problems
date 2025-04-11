# Problem statement: Write a program that takes two integers as input from the user.
# The program should output their greatest common divisor (GCD) using Euclid's algorithm.

# Function to find GCD of two numbers using Euclid's algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Get input from user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Calculate GCD using Euclid's algorithm
gcd_result = gcd(num1, num2)

# Output the result
print(f"The greatest common divisor of {num1} and {num2} is {gcd_result}")
