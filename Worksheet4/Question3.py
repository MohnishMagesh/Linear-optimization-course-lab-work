import math as m
import numpy as np
import random as rd
from math import e as euler

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[2,3],[4,5],[6,7]])
# c = np.matmul(a,b)

# print(c)

def f(x):
    return (x-1)*((x-3)**2)

def quadFit(a,b):
    x0_initial = 1
    x1_initial = 2
    x2_initial = 4

    E = m.pow(10,-2)

    x0 = x0_initial
    x1 = x1_initial
    x2 = x2_initial

    new_lb = 0
    new_ub = 0

    while(True):

        ya = f(x0)
        yb = f(x1)
        yc = f(x2)

        up = (((x1-x0)**2)*(yb-yc))-(((x1-x2)**2)*(yb-ya))
        down = ((x1-x0)*(yb-yc)-(x1-x2)*(yb-ya))
        x_new = x1 - (0.5 * (up/down))

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

quadFit(0,5)
