import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def square_wave(x, n_terms, L):
    a0 = 0.5  
    square_wave = a0 / 2
    for n in range(1, n_terms + 1):
        an, _ = quad(lambda x: np.cos(n * np.pi * x / L), -L, L)
        bn = 0.0
        if n % 2 != 0:
            bn = 1 / L * quad(lambda x: square_wave_function(x, L) * np.sin(n * np.pi * x / L), -L, L)[0]
        square_wave += an * np.cos(n * np.pi * x / L) + bn * np.sin(n * np.pi * x / L)
    return square_wave



def square_wave_function(x, L):
    if -L <= x < 0:
        return -1
    elif 0 <= x <= L:
        return 1



x_values = np.linspace(-20, 20, 1000)
n_terms = 20
L = np.pi
square_wave_values = square_wave(x_values, n_terms, L)
plt.figure(figsize=(10, 6))
plt.plot(x_values, square_wave_values, label='Square Wave')
plt.title('Square Wave using Fourier Series Formula')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()