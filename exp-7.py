import matplotlib.pyplot as plt

# Given data
Ta = 0  # Ambient temperature (°F)
T0 = 100  # Initial temperature of the metal bar (°F)
T_final = 50  # Final temperature after 20 minutes (°F)
t_final = 20  # Time when final temperature is reached (minutes)

# (a) Find the cooling constant k
k = -1 / t_final * (T_final - Ta)

# (b) Solve the ODE using Euler's method
def euler_method(h, t_end):
    t_values = [0]
    T_values = [T0]
    t = 0
    T = T0
    while t < t_end:
        T_next = T + h * (-k * (T - Ta))
        t += h
        t_values.append(t)
        T_values.append(T_next)
        T = T_next
    return t_values, T_values

# Step size and endpoint for Euler's method
h = 0.2
t_end_euler = 10  # 10 minutes for (b)

# Perform Euler's method
t_values_euler, T_values_euler = euler_method(h, t_end_euler)

# (c) Plot the graph
plt.plot(t_values_euler, T_values_euler, label='Euler Method', marker='o')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Variation with Time')
plt.legend()
plt.grid(True)
plt.show()

# (a) Find the time it will take the bar to reach the temperature of 25°F
t_25 = None
for t, T in zip(t_values_euler, T_values_euler):
    if T <= 25:
        t_25 = t
        break

if t_25 is not None:
    print(f"(a) Time to reach 25°F: {t_25:.2f} minutes")
else:
    print("The bar does not reach 25°F within the given time.")

# (b) Find the temperature of the bar after 10 minutes
# Find the temperature closest to 10 minutes
index_10_minutes = min(range(len(t_values_euler)), key=lambda i: abs(t_values_euler[i] - 10))
T_10_minutes = T_values_euler[index_10_minutes]
print(f"(b) Temperature after 10 minutes: {T_10_minutes:.2f} °F")
