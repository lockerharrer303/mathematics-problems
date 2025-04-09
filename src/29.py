import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define equation
equation = x**2 + 3*x*y - y**2 + 4*x - 6*y + 5

# Solve the equation
solution = sp.solve(equation, (x, y))

# Display the solution
print(solution)
