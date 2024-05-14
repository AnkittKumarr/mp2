#half wave rectifier
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def fourier_coefficients(n_terms, L):
    a_coefficients = []
    b_coefficients = []
    for n in range(1, n_terms + 1):
        an, _ = quad(lambda x: half_wave_function(x) * np.cos(n * np.pi * x / L), -L,L)
        bn, _ = quad(lambda x: half_wave_function(x) * np.sin(n * np.pi * x / L), -L, L)
        an *= 1 / L
        bn *= 1 / L
        a_coefficients.append(an)
        b_coefficients.append(bn)
    return a_coefficients, b_coefficients
def half_wave_function(x):
    if 0 < x < np.pi:
        return np.sin(x)
    else:
        return 0
def half_wave(x, n_terms, L):
    a0 = 0
    half_wave = a0 / 2
    for n in range(1, n_terms + 1):
        an = 1 / L * quad(lambda x: half_wave_function(x) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn = 0.0
        if n % 2 != 0:  
            bn = 1 / L * quad(lambda x: half_wave_function(x) * np.sin(n * np.pi * x / L), -L, L)[0]
        half_wave += an * np.cos(n * np.pi * x / L) + bn * np.sin(n * np.pi * x / L)
    return half_wave
x_values = np.linspace(-20, 20, 1000)
n_terms = 20 
L = np.pi
a_coefficients, b_coefficients = fourier_coefficients(n_terms, L)
half_wave_values = half_wave(x_values, n_terms, L)
plt.plot(x_values, half_wave_values, label='half wave')
plt.title('half Wave using Fourier Series Formula')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
print("Fourier Coefficients:")
for n in range(len(a_coefficients)):
    an = a_coefficients[n]
    bn = b_coefficients[n]
    print("Coefficient a" + str(n+1) + " is about " + str(round(an, 4)) + ", and coefficient b" + str(n+1) + " is about " + str(round(bn, 4)))
# plt.bar(range(1, n_terms+1), a_coefficients, label='an')
# plt.title('Fourier Coefficients (an) vs. n')
# plt.xlabel('n')
# plt.ylabel('an')
# plt.grid(True)
# plt.legend()
# plt.show()
# plt.bar(range(1, n_terms+1), b_coefficients, label='bn')
# plt.title('Fourier Coefficients (bn) vs. n')
# plt.xlabel('n')
# plt.ylabel('bn')
# plt.grid(True)
# plt.legend()
# plt.show()