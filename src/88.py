import math

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return -1.0

print(square_root(4))
