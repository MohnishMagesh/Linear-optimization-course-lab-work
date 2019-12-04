import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp
from sympy import solve, Eq

def f(x1,x2):
    # return (x1-x2)**2 + (x2+x1)**2
    # return (1-x1)**2 + (100 * ((x2-(x1**2))**2))
    # xR = x1
    # yR = x2
    # xA = 1.5
    # yA = 2.5
    # xB = 12
    # yB = 3.5
    # return m.pow(m.pow(xA-xR,2)+m.pow(yA-yR,2),0.5) + m.pow(m.pow(xB-xR,2)+m.pow(yB-yR,2),0.5)
    # return sp.sqrt((1.5-x1)**2+(2.5-x2)**2) + sp.sqrt((12-x1)**2+(3.5-x2)**2)

# partial derivative wrt to x1
def gradient_x1(x1_value,x2_value):
    x1 = sp.Symbol('x1')
    x2 = sp.Symbol('x2')
    temp = sp.diff(f(x1,x2),x1)
    expr = temp.subs(x1, x1_value)
    expr_f = expr.subs(x2, x2_value)
    return expr_f

# partial derivative wrt to x2
def gradient_x2(x2_value,x1_value):
    x1 = sp.Symbol('x1')
    x2 = sp.Symbol('x2')
    temp = sp.diff(f(x1,x2),x2)
    expr = temp.subs(x2, x2_value)
    expr_f = expr.subs(x1, x2_value)
    return expr_f

def gradientDescent():
    x1 = 2
    x2 = 0

    d_k = np.array([-gradient_x1(x1,x2),-gradient_x2(x2,x1)])
    print(d_k)

    alpha = sp.Symbol('alpha')

    # coordinates of next point
    # Next point by x_1 = x_0 + alpha*d_0
    nextPT_x1 = x1 + alpha * d_k[0]
    nextPT_x2 = x2 + alpha * d_k[1]
    gradient_d_kplus1 = np.array([gradient_x1(nextPT_x1,nextPT_x2),gradient_x2(nextPT_x2,nextPT_x1)])
    d_kplus1 = np.array([-gradient_x1(nextPT_x1,nextPT_x2),-gradient_x2(nextPT_x2,nextPT_x1)])


    temp = sp.diff(f(nextPT_x1,nextPT_x2),alpha)
    print(temp)
    eq1 = Eq(temp)
    sol = solve(eq1,alpha)
    alpha_val = sol[0]
    print('Alpha value is = {}'.format(alpha_val))

    # Check if gradient is zero or not
    d_kplus1 = np.array([-gradient_x1(nextPT_x1.subs(alpha,alpha_val),nextPT_x2.subs(alpha,alpha_val)),-gradient_x2(nextPT_x2.subs(alpha,alpha_val),nextPT_x1.subs(alpha,alpha_val))])
    print(d_kplus1)

gradientDescent()
