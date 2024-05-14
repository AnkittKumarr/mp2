import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def ode_function(t, M):
    return -0.693147181 / 2 * M  # ln(0.5) / 2


def euler_method(h, t_end):
    t_values = [0]
    M_values = [50]
    t = 0
    M = 50
    while t < t_end:
        M_next = M + h * ode_function(t, M)
        t += h
        t_values.append(t)
        M_values.append(M_next)
        M = M_next
    return t_values, M_values


def print_and_plot(t_values, M_values, label):
    print("t\t|\tM")
    print("-----------------")
    for t, M in zip(t_values, M_values):
        print(f"{t:.1f}\t|\t{M:.4f}")

    plt.plot(t_values, M_values, label=label, marker='o')
    plt.xlabel('Time (hours)')
    plt.ylabel('Mass (mg)')
    plt.title('Decay of Radioactive Material')
    plt.legend()
    plt.grid(True)
    plt.show()


h = 0.2
t_end = 6

# Using Euler's method
t_values_euler, M_values_euler = euler_method(h, t_end)
print_and_plot(t_values_euler, M_values_euler, 'Euler Method')

# Using built-in solver
M0 = 50
t_span = (0, 6)
sol = solve_ivp(ode_function, t_span, [M0], t_eval=np.linspace(0, 6, 100))
t_values_builtin = sol.t
M_values_builtin = sol.y[0]
print_and_plot(t_values_builtin, M_values_builtin, 'Built-in Solver')


M_4_hours = np.interp(4, t_values_builtin, M_values_builtin)
print(f"Mass after 4 hours: {M_4_hours:.4f} mg")

t_half = np.interp(M0 / 2, M_values_builtin[::-1], t_values_builtin[::-1])
print(f"Time at which the material has decayed to one half of its initial mass: {t_half:.4f} hours")
