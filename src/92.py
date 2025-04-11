import math
from fractions import Fraction

def calculate_factorial(n):
    """
    Calculate the factorial of a given number.
    
    Parameters:
    n (int): The non-negative integer to calculate the factorial for.
    
    Returns:
    int: The factorial of the given number.
    """
    return math.factorial(n)

def find_prime_factors(n):
    """
    Find and return all prime factors of a given number 'n'.
    Prime factors are numbers that divide a given number exactly, without leaving any remainder.
    
    Parameters:
    n (int): The non-negative integer to find the prime factors for.
    
    Returns:
    list: A list containing all the prime factors of 'n'.
    """
    i = 2
    primes = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if n == 1:
                break
            primes.append(i)
    if n > 1:
        primes.append(n)
    return sorted(primes)

def calculate_gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two non-negative integers.
    
    Parameters:
    a (int): The first non-negative integer.
    b (int): The second non-negative integer.
    
    Returns:
    int: The greatest common divisor of 'a' and 'b'.
    """
    return math.gcd(a, b)

def calculate_least_common_multiple(a, b):
    """
    Calculate the least common multiple (LCM) of two integers 'a' and 'b'.
    
    Parameters:
    a (int): The first non-negative integer.
    b (int): The second non-negative integer.
    
    Returns:
    int: The least common multiple of 'a' and 'b'.
    """
    return abs(a * b) // math.gcd(a, b)

def calculate_binary_to_decimal(num):
    """
    Convert a binary number to its decimal representation.
    
    Parameters:
    num (str): A string representing the binary number as a base-2 integer.
    
    Returns:
    int: The decimal representation of the binary number.
    """
    return sum(int(digit) * (2 ** ((len(num) - 1) - index)) for index, digit in enumerate(reversed(num)))

def calculate_fraction_sum(a, b):
    """
    Calculate the sum of two fractions represented as a and b over their denominators.
    
    Parameters:
    a (Fraction): The first fraction (a/b).
    b (Fraction): The second fraction (b/c).
    
    Returns:
    Fraction: The sum of the two fractions.
    """
    return Fraction(a.numerator, a.denominator) + Fraction(b.numerator, b.denominator)

def calculate_power(base, exponent):
    """
    Calculate the power of a number 'base' raised to the given exponent 'exponent'.
    
    Parameters:
    base (int): The base number.
    exponent (int): The exponent used for calculating the power.
    
    Returns:
    Fraction: The result of raising 'base' to the power of 'exponent'.
    """
    return Fraction(base, 1) ** exponent

def main():
    n = int(input("Enter a non-negative integer: "))
    print(f"Factorial of {n} is {calculate_factorial(n)}")
    primes = find_prime_factors(n)
    print(f"Prime factors of {n} are {primes}")
    gcd_result = calculate_gcd(a, b) if n else 0
    lcm_result = calculate_least_common_multiple(a, b)
    decimal_num = calculate_binary_to_decimal(1)
    fraction_sum = calculate_fraction_sum(a, b)
    power_result = calculate_power(base, exponent)

if __name__ == "__main__":
    main()
