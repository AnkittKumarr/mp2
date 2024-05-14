#trapezoidal rule integration ---


def func(x):
    return 1/(1+x**2)

def trapezoidal(x0, xn, n):
    h = (xn-x0)/n

    integration = func(x0) + func(xn)

    for i in range (1,n):
        k = x0 + i*h
        integration += 2*func(k)
    
    integration *= h/2
    return integration

lower_limit = float(input("enter lower limit: "))
upper_limit = float(input("enter upper limit: "))
sub_interval = int(input("enter the number of intervals: "))

result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration is: " + str(result))



#simpsons method integration --
#1/3 rule

import math

def func(x):
    return math.log(x)

def simpsons(ll, ul, n):
    h = (ul-ll)/2

    x = list()
    fx = list()

    i= 0
    while i<=n:
        x.append(ll+i*h)
        fx.append(func(x[i]))
        i +=1


    result = 0
    i = 0
    
    while i<=n:
        if i == 0 or i == n :
            result += fx[i]
        elif i%3 != 0:
            result+= 3*fx[i]
        else:
            result+= 2*fx[i]
        i += 1
    result *=(h/3)
    return result

lower_limit = float(input("enter lower limit: "))
upper_limit = float(input("enter upper limit: "))
sub_interval = 6


# 3/8 rule 
def func(x):
    return math.log(x)

def simpsons(ll, ul, n):
    h = (ul-ll)/2

    x = list()
    fx = list()

    i= 0
    while i<=n:
        x.append(ll+i*h)
        fx.append(func(x[i]))
        i +=1


    result = 0
    i = 0

    while i<=n:
        if i == 0 or i == n :
            result += fx[i]
        elif i%2 != 0:
            result+= 4*fx[i]
        else:
            result+= 2*fx[i]
        i += 1
    result *=(3*h/8)
    return result

lower_limit = float(input("enter lower limit: "))
upper_limit = float(input("enter upper limit: "))
sub_interval = 6


