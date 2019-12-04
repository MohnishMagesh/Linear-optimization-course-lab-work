import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp
from sympy import *

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[2,3],[4,5],[6,7]])
# c = np.matmul(a,b)

# print(c)

def f(x):
    # return (-m.pow(x,2))/(m.pow(x,3)+m.cos(x))  #/a/
    # return m.sin(x)/m.pow(x,0.5) #/c/
    # return m.cos(x)/m.pow(x,0.5) #/d/
    # return (x-1) * m.pow((x-3),2) * m.pow((x+7),-2) #/e/
    # return m.pow(x,4)
    # return m.pow(x,8)
    return 3*(x**2) + 2*x + 6

def quadFit(a,b,x0_initial,x1_initial,x2_initial):
    # x0_initial = 1
    # x1_initial = 2
    # x2_initial = 4

    E = m.pow(10,-4)

    x0 = x0_initial
    x1 = x1_initial
    x2 = x2_initial

    new_lb = 0
    new_ub = 0

    while(True):

        try:
            alpha = sp.Symbol('alpha')
            temp_real = f(alpha)
            temp0 = sp.diff(f(alpha),alpha)
            temp_g = sp.diff(temp0,alpha)
        except:
            pass

        key = False
        try:
            temp_g = int(temp_g)
            key = True
        except:
            pass

        if key==True:
            x1 = sp.Symbol('alpha')
            temp0 = f(alpha)
            eq1 = Eq(temp0)
            sol = solve(eq1,alpha)
            avg_min_max = (sol[0] + sol[1]) / 2
            new_lb = avg_min_max
            new_ub = avg_min_max
            break


        ya = f(x0)
        yb = f(x1)
        yc = f(x2)

        up = ((ya * (m.pow(x1,2) - m.pow(x2,2))) + (yb * (m.pow(x2,2) - m.pow(x0,2))) + (yc * (m.pow(x0,2) - m.pow(x1,2))))
        down = ((ya * (x1 - x2)) + (yb * (x2 - x0)) + (yc * (x0 - x1)))
        x_new = (0.5 * up) / down

        # x_new = b - 0.5*(((x1-x0)**2 * (yb-yc))-((x1-x2)**2 * (yb-ya)))/(((x1-x0) * (yb-yc))-((x1-x2) * (yb-ya))+0.0001)

        x_val = [x0, x1, x2, x_new]
        avg = (x0 + x1 + x2 + x_new)/4
        diff = []
        odd_one_out = 0
        for i in range(0,3):
            var = x_val[i] - avg
            diff.append(abs(var))

        maxim = max(diff)
        for i in range(0,3):
            if diff[i]==maxim:
                odd_one_out = x_val[i]

        new_x_val = []
        for i in x_val:
            if i==odd_one_out:
                continue
            new_x_val.append(i)

        x0 = new_x_val[0]
        x1 = new_x_val[1]
        x2 = new_x_val[2]

        new_lb = min(new_x_val)
        new_ub = max(new_x_val)

        # Tolerance condition
        if abs(new_ub - new_lb) < E:
            break

    print("New domain:")
    print('[{},{}]'.format(new_lb,new_ub))
    print('Extrema value is = {}'.format(f(new_lb)))

quadFit(-5,5,1,2,4)
