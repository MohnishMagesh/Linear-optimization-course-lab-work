import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def f(x1,x2):
    # return 0.5*(x1**2) + x1*x2 + (x2**2)
    # return x1**2 + x1*x2 + x2**2 + 5
    return (3*sp.sin(sp.sqrt(x1**2+x2**2))-(1.5*sp.exp(-(x1**2+x2**2-3*x1-6*x2+14))))*sp.asin(x2/(sp.sqrt(x1**2+x2**2)))

# partial derivative wrt to x1
def gradient_x1():
    x1 = sp.Symbol('x1')
    x2 = sp.Symbol('x2')
    temp = sp.diff(f(x1,x2),x1)
    # expr = temp.subs(x1, x1_value)
    # expr_f = expr.subs(x2, x2_value)
    # return expr_f
    return temp

# partial derivative wrt to x2
def gradient_x2():
    x1 = sp.Symbol('x1')
    x2 = sp.Symbol('x2')
    temp = sp.diff(f(x1,x2),x2)
    # expr = temp.subs(x2, x2_value)
    # expr_f = expr.subs(x1, x1_value)
    # return expr_f
    return temp

blah = gradient_x1()
blah1 = gradient_x2()

print(blah)
print(blah1)
