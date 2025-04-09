# Problem statement: Find all pairs of positive integers (x, y) such that x^2 + y^2 = 100

for x in range(1, int(10**0.5)):
    for y in range(x, int(10**0.5)):
        if x**2 + y**2 == 100:
            print(f"x = {x}, y = {y}")
