import numpy as np
from scipy import special

def calculate_custom_function(x):
    y = 2 * x**3 - 4 * x + 1
    z = np.cos(x)
    return y, z
