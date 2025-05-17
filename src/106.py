import sympy as sp

x = sp.Symbol('x')
equation = x**2 - 4*x + 3
roots = sp.solve(equation, x)
print("Roots of the equation:", roots)
