# EXPERIMENT NO>>> 6 ------------------------------------


import numpy as np
import matplotlib.pyplot as plt


def f(t, N):
    k = 0.693 / 2  # Decay constant
    return -k * N


def runge_kutta(h, t_end, N0):
    t_values = [0]
    N_values = [N0]
    t = 0
    N = N0
    while t < t_end:
        k1 = h * f(t, N)
        k2 = h * f(t + h / 2, N + k1 / 2)
        k3 = h * f(t + h / 2, N + k2 / 2)
        k4 = h * f(t + h, N + k3)
        N += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
        t_values.append(t)
        N_values.append(N)
    return t_values, N_values

N0 = 50  # Initial mass in mg


t_end = 4  # Time in hours

# Step size for Runge-Kutta method
h = 0.1


t_values, N_values = runge_kutta(h, t_end, N0)

plt.plot(t_values, N_values, label='Runge-Kutta Method')
plt.xlabel('Time (hours)')
plt.ylabel('Mass of material (mg)')
plt.title('Radioactive Decay of Material using Runge-Kutta Method')
plt.legend()
plt.grid(True)
plt.show()



# EXPERIMENT NO >> 7  ----------------------------------------------

# import numpy as np
# import matplotlib.pyplot as plt

# # Constants
# T_r = 0  # Room temperature in Fahrenheit
# T_0 = 100  # Initial temperature of the bar in Fahrenheit
# k = 0.1  # Rate of temperature change constant in (1/min)

# # Differential equation describing the rate of temperature change
# def dT_dt(T, t):
#     return -k * (T - T_r)

# # Runge-Kutta method
# def runge_kutta(f, T0, t0, tf, h):
#     n = int((tf - t0) / h)
#     t = np.linspace(t0, tf, n+1)
#     T = np.zeros(n+1)
#     T[0] = T0
#     for i in range(1, n+1):
#         k1 = h * f(T[i-1], t[i-1])
#         k2 = h * f(T[i-1] + 0.5 * k1, t[i-1] + 0.5 * h)
#         k3 = h * f(T[i-1] + 0.5 * k2, t[i-1] + 0.5 * h)
#         k4 = h * f(T[i-1] + k3, t[i-1] + h)
#         T[i] = T[i-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
#     return t, T

# # Solve using Runge-Kutta method
# t_values, T_values = runge_kutta(dT_dt, T_0, 0, 20, 0.1)

# # (a) Find the time it will take the bar to reach the temperature of 25°F
# for i, temp in enumerate(T_values):
#     if temp <= 25:
#         time_to_25F = t_values[i]
#         break

# # (b) Find the temperature of the bar after 10 minutes
# temperature_after_10min = np.interp(10, t_values, T_values)

# # (c) Plot the graph
# plt.plot(t_values, T_values)
# plt.xlabel('Time (min)')
# plt.ylabel('Temperature (°F)')
# plt.title('Temperature Variation of the Bar')
# plt.grid(True)
# plt.show()

# print("(a) Time it will take the bar to reach the temperature of 25°F:", time_to_25F, "minutes")
# print("(b) Temperature of the bar after 10 minutes:", temperature_after_10min, "°F")





# EXPERIMENT NO >> 8 ---------------------------------

# import numpy as np
# import matplotlib.pyplot as plt

# # Constants
# R = 50  # Resistance in Ohms
# L = 1   # Inductance in Henrys
# V = 5   # EMF in Volts

# # Differential equation describing the RL circuit
# def dI_dt(I, t):
#     return (-R/L) * I + V/L

# # Runge-Kutta method
# def runge_kutta(f, I0, t0, tf, h):
#     n = int((tf - t0) / h)
#     t = np.linspace(t0, tf, n+1)
#     I = np.zeros(n+1)
#     I[0] = I0
#     for i in range(1, n+1):
#         k1 = h * f(I[i-1], t[i-1])
#         k2 = h * f(I[i-1] + 0.5 * k1, t[i-1] + 0.5 * h)
#         k3 = h * f(I[i-1] + 0.5 * k2, t[i-1] + 0.5 * h)
#         k4 = h * f(I[i-1] + k3, t[i-1] + h)
#         I[i] = I[i-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
#     return t, I

# # Solve using Runge-Kutta method
# t_values, I_values = runge_kutta(dI_dt, 0, 0, 20, 0.1)

# # Plot the graph
# plt.plot(t_values, I_values)
# plt.xlabel('Time (s)')
# plt.ylabel('Current (A)')
# plt.title('Current in RL Circuit')
# plt.grid(True)
# plt.show()

# # Find the current at time 20 seconds
# current_at_20s = np.interp(20, t_values, I_values)
# print("Current in the circuit at time 20 seconds:", current_at_20s, "Amperes")



# EXPERIMENT NO >> 9 ---------------------------------


# import numpy as np
# import matplotlib.pyplot as plt

# # Constants
# R = 100        # Resistance in Ohms
# C = 0.01       # Capacitance in Farads

# # EMF function
# def V(t):
#     return 400 * np.cos(2 * t)

# # Differential equation for charge on the capacitor
# def dQ_dt(Q, t):
#     return (V(t) - Q/C) / R

# # Runge-Kutta method
# def runge_kutta(f, Q0, t0, tf, h):
#     n = int((tf - t0) / h)
#     t = np.linspace(t0, tf, n+1)
#     Q = np.zeros(n+1)
#     Q[0] = Q0
#     for i in range(1, n+1):
#         k1 = h * f(Q[i-1], t[i-1])
#         k2 = h * f(Q[i-1] + 0.5 * k1, t[i-1] + 0.5 * h)
#         k3 = h * f(Q[i-1] + 0.5 * k2, t[i-1] + 0.5 * h)
#         k4 = h * f(Q[i-1] + k3, t[i-1] + h)
#         Q[i] = Q[i-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
#     return t, Q

# # Solve using Runge-Kutta method
# t_values, Q_values = runge_kutta(dQ_dt, 0, 0, 10, 0.01)

# # Calculate current through the resistor
# I_values = [(V(t) - Q/C) / R for t, Q in zip(t_values, Q_values)]

# # Plot the graph
# plt.figure(figsize=(10, 5))
# plt.plot(t_values, Q_values, label='Charge (Coulombs)')
# plt.plot(t_values, I_values, label='Current (Amperes)')
# plt.xlabel('Time (s)')
# plt.ylabel('Charge (C) / Current (A)')
# plt.title('Charge and Current in RC Circuit')
# plt.legend()
# plt.grid(True)
# plt.show()
