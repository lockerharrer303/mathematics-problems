import numpy as np

def calculate_derivative(function):
    """
    Calculate the derivative of a given function.
    
    Args:
        function (callable): A function that takes one argument and returns its value.
        
    Returns:
        float: The derivative of the input function.
    """
    return np.diff(np.array([function(i) for i in range(100)]), n=1)

# Example usage
def quadratic_function(x):
    """Example quadratic function."""
    return x**2

result = calculate_derivative(quadratic_function)
print("The derivative of the quadratic function is:", result)
