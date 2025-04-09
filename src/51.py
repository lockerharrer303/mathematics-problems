import math
a = 2
b = 3
c = 4.0

if a < b + c:
    print("a is less than (b + c)")
else:
    print("a is not less than (b + c)")
    
if a > b - c:
    print("a is greater than (b - c)")
else:
    print("a is not greater than (b - c)")

if a * b < c * d:
    print("a times b is less than c times d")
else:
    print("a times b is not less than c times d")

if math.sqrt(a) > 2 + math.sqrt(b):
    print("the square root of a is greater than (2 + the square root of b)")
else:
    print("the square root of a is not greater than (2 + the square root of b)")

if a * b == c ** 3:
    print("a times b equals to c cubed")
else:
    print("a times b is not equal to c cubed")
