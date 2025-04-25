def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 2:
        factors.append(num)
    return factors

def main():
    n = int(input("Enter a positive integer: "))
    print(f"Sum of squares: {sum_of_squares(n)}")
    print(f"Fibonacci numbers up to {n}:")
    for i in range(1, n + 1):
        if i == sum_of_squares(i):
            print(f"Fibo({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    main()
