import numpy as np
import matplotlib.pyplot as plt


x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([3, 4, 5, 6, 8])


slope, intercept = np.polyfit(x_values, y_values, 1)
best_fit_line = slope * x_values + intercept


plt.scatter(x_values, y_values, color='blue', label='Data Points')
plt.plot(x_values, best_fit_line, color='red', label='Best Fit Line')


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Best Fit Line')
plt.legend()


plt.grid(True)
plt.show()
