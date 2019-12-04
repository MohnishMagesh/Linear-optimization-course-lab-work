import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def transpose():
    matrix = np.array([1,2,3])
    matrixT = np.transpose(matrix)
    print(matrixT)

def multiply():
    matrix1 = np.array([1,2,3])
    matrix2 = np.array([[2,3],[7,8],[4,1]])
    multM = np.matmul(matrix1,matrix2)
    print(multM)

def determinant():
    M = np.array([[1,2,3],[4,32,5],[1,49,7]])
    print(np.linalg.det(M))

def inverse():
    M = np.array([[1,2,3],[4,32,5],[1,49,7]])
    print(np.linalg.inv(M))

transpose()
multiply()
determinant()
inverse()
