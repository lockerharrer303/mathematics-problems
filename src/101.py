import sympy

def f(x):
    return sympy.Symbol('x')

g = lambda x: 2*x - 3

h = lambda x: (x**2) * g(x)
