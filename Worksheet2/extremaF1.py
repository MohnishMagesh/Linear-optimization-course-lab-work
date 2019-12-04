import math as m
import random as rd

def f(x):
    var = m.exp(-x)
    return (var - (x * var))

def bisection(x1,x2):
    if(f(x1)*f(x2)>=0):
        print('Wrong values assumed')

    xm = 1

    while((x2-x1)>=0):
        xm = (x1 + x2)/2

        if(f(xm) == 0):
            break

        if(f(xm)*f(x1) < 0):
            x2 = xm
        else:
            x1 = xm

    print('value of root:')
    print(xm)

bisection(0.5,3)
