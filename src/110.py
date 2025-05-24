# Problem: Finding the smallest positive integer n such that 2^n is less than or equal to 1000

n = 5
while True:
    if 2 ** n <= 1000:
        break
    n += 1

print(n)
