import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def x_coor(x):
    return x

def y_coor(y):
    return y

def minimize_dist(xR):
    xA = 1.5
    yA = 2.5
    xB = 12
    yB = 3.5
    yR = 0
    return m.pow(m.pow(xA-xR,2)+m.pow(yA-yR,2),0.5) + m.pow(m.pow(xB-xR,2)+m.pow(yB-yR,2),0.5)


def min_dist():
    xA = 1.5
    xB = 12

    x_axis = np.linspace(xA,xB,10000)

    distances_list = []

    index = 0
    for x in x_axis:
        value = minimize_dist(x)
        distances_list.append(value)

    print(min(distances_list))

min_dist()
