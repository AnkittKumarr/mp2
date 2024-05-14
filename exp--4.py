def legendre_polynomial(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        P_prev, P = 1, x
        for i in range(2, n + 1):
            P_next = ((2 * i - 1) * x * P - (i - 1) * P_prev) / i
            P_prev, P = P, P_next
        return P

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        integral += 2 * f(a + i * h)
    integral *= h / 2
    return integral

def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        integral += 2 * f(a + i * h)
    integral *= h / 3
    return integral

n1, n2 = 3, 4  # Example polynomials, adjust as needed

integral_trapezoidal = trapezoidal_rule(lambda x: legendre_polynomial(n1, x) * legendre_polynomial(n2, x), -1, 1, 1000)
integral_simpsons = simpsons_rule(lambda x: legendre_polynomial(n1, x) * legendre_polynomial(n2, x), -1, 1, 1000)

print(f"Integral (Trapezoidal): {integral_trapezoidal}")
print(f"Integral (Simpson's): {integral_simpsons}")
