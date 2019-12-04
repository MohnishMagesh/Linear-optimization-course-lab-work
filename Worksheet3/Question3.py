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
    xM = 3.375
    xN = 9
    xB = 12

    x_axis_section_1 = np.linspace(xA,xM,10000)
    x_axis_section_2 = np.linspace(xN,xB,10000)

    distances_list = []

    index = 0
    for x in x_axis_section_1:
        value = minimize_dist(x)
        distances_list.append(value)

    for x in x_axis_section_2:
        value = minimize_dist(x)
        distances_list.append(value)

    print(min(distances_list))

min_dist()
