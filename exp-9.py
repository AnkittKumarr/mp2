import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Given data
R = 100  # Resistance (ohms)
C = 0.01  # Capacitance (farads)

# Function to calculate the emf at time t
def emf(t):
    return 400 * np.cos(2 * t)

# Function to calculate the charge using Euler's method
def euler_method(h, t_end):
    t_values = [0]
    Q_values = [0]  # Initial charge is 0
    t = 0
    Q = 0
    while t < t_end:
        dQ_dt = emf(t) - Q / (R * C)
        Q_next = Q + h * dQ_dt
        t += h
        t_values.append(t)
        Q_values.append(Q_next)
        Q = Q_next
    return t_values, Q_values

# Step size and endpoint for Euler's method
h = 0.01
t_end = 10  

# Perform Euler's method
t_values, Q_values = euler_method(h, t_end)


I_values = [(emf(t) - Q / (R * C)) / R for t, Q in zip(t_values, Q_values)]


table = [["Time (s)", "Charge (C)", "Current (A)"]]
table.extend([[t, Q, I] for t, Q, I in zip(t_values, Q_values, I_values)])

print(tabulate(table, headers="firstrow", tablefmt="pretty"))


plt.plot(t_values, Q_values, label='Charge', color='b')
plt.plot(t_values, I_values, label='Current', color='r')
plt.xlabel('Time (seconds)')
plt.ylabel('Charge (coulombs) / Current (amperes)')
plt.title('Charge and Current in RC Circuit')
plt.legend()
plt.grid(True)
plt.show()
