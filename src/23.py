def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
numbers = [12, 37, 64, 89, 15]
for number in numbers:
    print(f"Factorization of {number}: {prime_factors(number)}")
