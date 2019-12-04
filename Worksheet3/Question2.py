import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def x_coor(x):
    return x

def y_coor(y):
    return y

def minimize_dist(xM,yN):
    xA = 1.5
    yA = 2.5
    xB = 12
    yB = 3.5
    yM = 0
    xN = 15
    return m.pow(m.pow(xA-xM,2)+m.pow(yA-yM,2),0.5) + m.pow(m.pow(xN-xM,2)+m.pow(yN-yM,2),0.5) + m.pow(m.pow(xB-xN,2)+m.pow(yB-yN,2),0.5)
    # return m.pow(m.pow(1.5-x1,2)+m.pow(2.5-0,2),0.5) + m.pow(m.pow(15-x1,2)+m.pow(x2-0,2),0.5) + m.pow(m.pow(12-15,2)+m.pow(3.5-x2,2),0.5)
    # return sp.sqrt((1.5-x1)**2+(2.5-0)**2) + sp.sqrt((15-x1)**2+(x2-0)**2) + sp.sqrt((12-15)**2+(3.5-x2)**2)

def min_dist():
    xA = 1.5
    xEND = 15

    x_axis = np.linspace(xA,xEND,1000)
    y_axis = np.linspace(0,3.5,1000)

    distances_list = []

    index = 0
    for x in x_axis:
        for y in y_axis:
            value = minimize_dist(x,y)
            distances_list.append(value)

    print(min(distances_list))
min_dist()
