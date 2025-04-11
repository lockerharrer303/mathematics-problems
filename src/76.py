import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equation y'' = -10y
def dYdt(y, t):
    return -10 * y[1]

# Initial condition: y(0) = [1, 2], dy/dt(0) = [0, 3]
initial_condition = np.array([1, 2])
time_points = np.linspace(0, 5, 1000)

solution = odeint(dYdt, initial_condition, time_points)
y_values = solution[:, 0]  # y(t) = y'
t_values = solution[:, 1]

plt.plot(time_points, y_values, label='y(t)')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.title('Differential Equation Solution')
plt.legend()
plt.grid(True)
plt.show()
