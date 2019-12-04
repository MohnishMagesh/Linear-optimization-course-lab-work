import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def f(x1,x2):
    # return 0.5*(x1**2) + x1*x2 + (x2**2)
    # return x1**2 + x1*x2 + x2**2 + 5
    # return (3*sp.sin(sp.sqrt(x1**2+x2**2))-(1.5*sp.exp(-(x1**2+x2**2-3*x1-6*x2+14))))*sp.asin(x2/(sp.sqrt(x1**2+x2**2)))
    # return sp.sin(x1+x2)
    return x1**2+x2**2

def nd_x1(x1_value,x2_value):
    h = 0.000001
    return (f(x1_value+h,x2_value)-f(x1_value,x2_value))/(h)

def nd_x2(x1_value,x2_value):
    h = 0.000001
    return (f(x1_value,x2_value+h)-f(x1_value,x2_value))/(h)

value_nd_x1 = nd_x1(1,1)
value_nd_x2 = nd_x2(1,1)
print(value_nd_x1)
print(value_nd_x2)
