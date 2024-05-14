import numpy as np
import matplotlib.pyplot as plt

E = 5  # EMF (volts)
R = 50  # Resistance (ohms)
L = 1  # Inductance (henrys)
t_end = 20  # Time (seconds)

# Define the ODE function
def ode_function(t, I):
    return (E - R * I) / L

# Euler's method for solving ODE
def euler_method(h, t_end):
    t_values = [0]
    I_values = [0]  # Initial current is 0
    t = 0
    I = 0
    while t < t_end:
        I_next = I + h * ode_function(t, I)
        t += h
        t_values.append(t)
        I_values.append(I_next)
        I = I_next
    return t_values, I_values

# Step size for Euler's method
h = 0.01  

# Perform Euler's method
t_values, I_values = euler_method(h, t_end)

# Plot the graph
plt.plot(t_values, I_values, label='Current', color='b')
plt.xlabel('Time (seconds)')
plt.ylabel('Current (amperes)')
plt.title('Current in RL Circuit')
plt.legend()
plt.grid(True)
plt.show()

# Current at t = 20 seconds
I_20_seconds = I_values[-1]
print(f"Current at t = 20 seconds: {I_20_seconds:.4f} Amperes")
