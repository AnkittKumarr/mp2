import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5])
Y = np.array([3, 4, 5, 6, 8])


X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = np.sum((X - X_mean) * (Y - Y_mean))
den = np.sum((X - X_mean) ** 2)

m = num / den

b = Y_mean - m * X_mean

best_fit_line = m * X + b

plt.scatter(X, Y, label='Data Points', )
plt.plot(X, best_fit_line, color='red', label='Best Fit Line')
plt.plot(X, Y, linestyle='dotted', color='purple')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('linear function best fit graph')
plt.legend()
plt.grid(True)
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt


# X = np.array([1, 2, 3, 4])
# Y = np.array([6, 11, 18, 27])
# deg = 2  








