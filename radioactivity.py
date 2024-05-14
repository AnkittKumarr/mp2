import numpy as np
import matplotlib.pyplot as plt

# Define the radioactive decay function
def radioactive_decay(N, k):
    return -k * N

# Function to solve the ODE using Euler's method
def euler_method(N0, k, t_final, dt):
    t_values = np.arange(0, t_final + dt, dt)
    N_values = np.zeros_like(t_values)
    N_values[0] = N0

    for i in range(1, len(t_values)):
        N_values[i] = N_values[i-1] + dt * radioactive_decay(N_values[i-1], k)

    return t_values, N_values

# Parameters
N0 = 50  # Initial mass in mg
k = -np.log(1 - 0.1) / 2  # Decay constant calculated from the given information
t_final = 5  # Final time in hours
dt = 0.01  # Time step for Euler's method

# Solve the ODE using Euler's method
t_values, N_values = euler_method(N0, k, t_final, dt)

# Plot the graph
plt.plot(t_values, N_values, label='Mass vs. Time')
plt.xlabel('Time (hours)')
plt.ylabel('Mass (mg)')
plt.title('Radioactive Decay')
plt.legend()
plt.grid(True)
plt.show()
