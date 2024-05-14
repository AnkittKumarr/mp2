import matplotlib.pyplot as plt

def f(x, y):
    return y + x

def euler_method(h, x_end):
    x_values = [0]
    y_values = [0]
    x = 0
    y = 0
    while x < x_end:
        y_next = y + h * f(x, y)
        x += h
        x_values.append(x)
        y_values.append(y_next)
        y = y_next
    return x_values, y_values

h = 0.2
x_end = 1.0


x_values, y_values = euler_method(h, x_end)


for x, y in zip(x_values, y_values):
    print(f"x = {x:.1f}, y = {y:.4f}")





plt.plot(x_values, y_values, label='Euler Method (h=0.2)', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximated Solution using Euler Method')
plt.legend()
plt.grid(True)
plt.show()
