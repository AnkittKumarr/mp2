import numpy as np
import matplotlib.pyplot as plt

x_values = np.array([1, 2, 3, 4])
y_values = np.array([6, 11, 18, 27])


degree = 2

coefficients = np.polyfit(x_values, y_values, degree)


polynomial_function = np.poly1d(coefficients)


x_range = np.linspace(min(x_values), max(x_values), 100)
y_fit = polynomial_function(x_range)


plt.scatter(x_values, y_values, color='blue', label='Data Points')
plt.plot(x_range, y_fit, color='red', label='Polynomial Fit (Degree {})'.format(degree))


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Fit (Degree {})'.format(degree))
plt.legend()

plt.grid(True)
plt.show()
