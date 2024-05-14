# #Question 3 >>>


# from scipy.integrate import quad
# import numpy as np
# import math
# # Using trapezoidal 

# def func1(x):
#     return math.log(x)

# def trapezoidal(x0, xn, n):
#     h = (xn-x0)/n

#     integration = func1(x0) + func1(xn)

#     for i in range (1,n):
#         k = x0 + i*h
#         integration += 2*func1(k)
    
#     integration *= h/2
#     return integration

# def func2(x):
#     return 1 / (1 + x**2)

# def trapezoidal(x0, xn, n):
#     h = (xn - x0) / n

#     integration = (func2(x0) + func2(xn)) / 2  

#     for i in range(1, n):
#         k = x0 + i * h
#         integration += func2(k)

#     integration *= h
#     return integration

# def simpsons(ll, ul, n):
#     h = (ul - ll) / n

#     x = list()
#     fx = list()

#     i = 0
#     while i <= n:
#         x.append(ll + i * h)
#         fx.append(func1(x[i]))
#         i += 1

#     result = 0
#     i = 0

#     while i <= n:
#         if i == 0 or i == n:
#             result += fx[i]
#         elif i % 2 != 0:
#             result += 4 * fx[i]
#         else:
#             result += 2 * fx[i]
#         i += 1
#     result *= (h / 3)
#     return result


# def simpsons(ll, ul, n):
#     h = (ul - ll) / n

#     x = list()
#     fx = list()

#     i = 0
#     while i <= n:
#         x.append(ll + i * h)
#         fx.append(func2(x[i]))
#         i += 1

#     result = 0
#     i = 0

#     while i <= n:
#         if i == 0 or i == n:
#             result += fx[i]
#         elif i % 2 != 0:
#             result += 4 * fx[i]
#         else:
#             result += 2 * fx[i]
#         i += 1
#     result *= (h / 3)
#     return result

# #actual integration --


# def func(x):
#     return np.log(x)

# lower_limit = 1
# upper_limit = 4

# actual_log, error = quad(func, lower_limit, upper_limit)

# print("Integration of log(x) using scipy's quad function:", actual_log)


# def func(x):
#     return 1 / (1 + x**2)

# lower_limit = 0
# upper_limit = 3

# actual_quad, error = quad(func, lower_limit, upper_limit)

# print("Integration of 1/(1 + x^2) using scipy's quad function:", actual_quad)

# def rel_error(actual_val, calculated_val):
#     return abs(actual_val - calculated_val)/actual_val



# lower_limit_quad = 0
# upper_limit_quad = 3
# lower_limit_log = 1
# upper_limit_log = 4
# sub_interval = 4


# #Trapezoidal rule >>
# #log x
# trap_log = trapezoidal(lower_limit_log, upper_limit_log, sub_interval)
# print("Integration of logx using trapezoidal rule: " + str(trap_log))

# #1/(1+x**2)
# trap_quad = trapezoidal(lower_limit_quad, upper_limit_quad, sub_interval)
# print("Integration of 1/(1+x**2) using trapezoidal: " + str(trap_quad))


# #simpsons rule >>
# #log x
# simp_log = simpsons(lower_limit_log, upper_limit_log, sub_interval)
# print("Integration of log(x) using Simpson's rule:", simp_log)

# #1/(1+x**2)
# simp_quad = simpsons(lower_limit_quad, upper_limit_quad, sub_interval)

# print("Integration of 1/(1+x**2) using Simpson's rule:", simp_quad)



# #error calculation

# print("trapezoidal relative error ( log ): " + str(rel_error(actual_log, trap_log)))
# print("trapezoidal relative error ( quad ): " + str(rel_error(actual_quad, trap_quad)))
# print("simpsons relative error ( log ): " + str(rel_error(actual_log, simp_log)))
# print("simpsons relative error ( quad ): " + str(rel_error(actual_quad, simp_quad)))




#Question 2 >>>


def func(x):
    if 0<=x<1:
        return 0
    elif 1<=x<2:
        return 10
    elif 2<=x<3:
        return 12
    elif 3<=x<4:
        return 14
    else:
        return 0

def trap_rule(a, b, n):
    h = (b-a)/n
    sum = func(a) + func(b)

    for i in range(1,n):
        sum = sum + 2*func(a+i*h)
    return sum*h/2

l = float(input("l: "))
u = float(input("u: "))
n = int(input("n: "))

result_integration = trap_rule(l,u,n)
    


print("Integration of v(t) from 0 to 3 using trapezoidal method:", result_integration)



