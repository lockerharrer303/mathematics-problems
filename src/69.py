def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1 or n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

fibonacci(15)
