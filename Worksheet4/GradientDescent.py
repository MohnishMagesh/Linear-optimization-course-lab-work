import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def f(x1,x2):
    return (x1-x2)**2 + (x1+x2)**2

# partial derivative wrt to x1
def gradient_x1(x1_value,x2_value):
    x1 = sp.Symbol('x1')
    x2 = sp.Symbol('x2')
    temp = sp.diff(f(x1,x2),x1)
    expr = temp.subs(x1, x1_value)
    return expr

# partial derivative wrt to x2
def gradient_x2(x2_value,x1_value):
    x1 = sp.Symbol('x1')
    x2 = sp.Symbol('x2')
    temp = sp.diff(f(x1,x2),x2)
    expr = temp.subs(x2, x2_value)
    return expr

def value_gradx1(xt):
    x1 = xt
    temp1 = gradient_x1()
    return temp1

def value_gradx2(xt):
    x2 = xt
    temp2 = gradient_x2()
    return temp2

alpha_fixed = 1

def gradientDescent(alpha, beta, rf, sigma):
    # pick starting point
    x1 = 1
    x2 = 1
    # x1 = rd.randint(-10,10)
    # x2 = rd.randint(-10,10)
    # first point will then be x_0 = (x1,x2)

    # Tolerance condition
    E = m.pow(10,-4)
    # Length of current interval
    Length_now = m.pow(10,-3)

    while(Length_now>=E):
        gradient_d_k = np.array([gradient_x1(x1,x2),gradient_x2(x2,x1)])
        d_k = np.array([-gradient_x1(x1,x2),-gradient_x2(x2,x1)])
        print(d_k)

        # Next point by x_1 = x_0 + alpha*d_0
        nextPT_x1 = x1 + alpha * d_k[0]
        nextPT_x2 = x2 + alpha * d_k[1]
        gradient_d_kplus1 = np.array([gradient_x1(nextPT_x1,nextPT_x2),gradient_x2(nextPT_x2,nextPT_x1)])
        d_kplus1 = np.array([-gradient_x1(nextPT_x1,nextPT_x2),-gradient_x2(nextPT_x2,nextPT_x1)])
        print('x_1 = ({},{})'.format(nextPT_x1,nextPT_x2))

        # f(x_0)
        func_value0 = f(x1,x2)
        print('f(x_k) = {}'.format(func_value0))

        #f(x_1)
        func_value_nextPT = f(nextPT_x1,nextPT_x2)
        print('f(x_k+1) = {}'.format(func_value_nextPT))

        while(True):

            # ARMIJO's CONDITION
            # f(x_(k+1)) < f(x_(k)) + beta * alpha * [grad(x_(k))T * d_k]
            gradT = np.transpose(gradient_d_k)
            directional_derivative_k_k = np.matmul(gradT, d_k)
            # print(directional_derivative)
            armijo_condition = func_value_nextPT < func_value0 + (beta * alpha * directional_derivative_k_k)
            if(armijo_condition==False):
                alpha = alpha * rf
                continue
            # WOLFE's condition
            # [grad(x_(k+1))T * d_k] >= sigma * [grad(x_(k))T * d_k]
            gradTNT = np.transpose(gradient_d_kplus1)
            directional_derivative_k_kplus1 = np.matmul(gradTNT, d_k)
            print(directional_derivative_k_kplus1)
            wolfe_condition = directional_derivative_k_kplus1 >= sigma * directional_derivative_k_k
            if(wolfe_condition==False):
                alpha = alpha * rf
                continue

            x1 = nextPT_x1
            x2 = nextPT_x2

            print('Local minima occurs at ({},{})'.format(nextPT_x1,nextPT_x2))

            Length_now = abs(func_value0 - func_value_nextPT)/(abs(func_value0))
            break

beta = m.pow(10,-4)
reduction_factor = 0.5
sigma = 0.9

gradientDescent(alpha_fixed, beta, reduction_factor, sigma)
