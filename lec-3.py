import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad



def square_wave(x, n_terms, L):
    a0 = 0
    f_x = a0 / 2
    for n in range(1, n_terms + 1):
        an = 1 / L * quad(lambda x: square_wave_function(x, L) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn = 0.0
        if n % 2 != 0:  
            bn = 1 / L * quad(lambda x: square_wave_function(x, L) * np.sin(n * np.pi * x / L), -L, L)[0]
        f_x += an * np.cos(n * np.pi * x / L) + bn * np.sin(n * np.pi * x / L)
        # print(an)
        # print(bn)
    return f_x


def square_wave_function(x, L):
    if -L <= x < 0:
        return -1
    elif 0 <= x <= L:
        return 1

def triangular_wave_function(x, L):
    if -L <= x < 0:
        return -x
    elif 0 <= x <= L:
        return x

def half_wave_rectifier(x, L):
    if 0 < x < L:
        return np.sinx
    elif L < x < 2*np.pi:
        return 0
    


        
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