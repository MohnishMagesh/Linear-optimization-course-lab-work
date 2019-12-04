import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def f(x1,x2):
    # return 0.5*(x1**2) + x1*x2 + (x2**2)
    return x1**2 + x1*x2 + x2**2 + 5
    # return (3*sp.sin(sp.sqrt(x1**2+x2**2))-(1.5*sp.exp(-(x1**2+x2**2-3*x1-6*x2+14))))*sp.asin(x2/(sp.sqrt(x1**2+x2**2)))

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
    expr_f = expr.subs(x1, x1_value)
    return expr_f

def conjugateGradientDescent():
    # initial Point
    x1 = 10
    x2 = -5

    nextPT_x1 = 10
    nextPT_x2 = -5

    iterations = 0
    firstIteration = True

    # Value is initialized for reference
    d_k_plus1 = 0

    while(True):
        iterations+=1
        print('Iteration number {}'.format(iterations))
        x1 = nextPT_x1
        x2 = nextPT_x2
        gradient_d_k = np.array([gradient_x1(x1,x2),gradient_x2(x2,x1)])
        print('Gradient_d_k is currently {}'.format(gradient_d_k))
        if firstIteration:
            d_k = -1 * gradient_d_k
            firstIteration = False
        else:
            d_k = d_k_plus1
        print('d_k is currently {}'.format(d_k))


        # Next point is xk+1 = xk + alpha * dk
        alpha = sp.Symbol('alpha')
        nextPT_x1 = x1 + alpha * d_k[0]
        nextPT_x2 = x2 + alpha * d_k[1]
        func_expr = f(nextPT_x1,nextPT_x2)
        print(func_expr)

        temp = sp.diff(func_expr,alpha)
        list_1 = sp.solve(temp,alpha)
        print(list_1)
        # Values of alpha
        list_2 = []
        for i in list_1:
            try:
                if(i>0 or i<=0):
                    list_2.append(i)
            except:
                continue

        print('Possible values of alpha {}'.format(list_2))
        value_list = min(list_2)
        print ('Alpha minimized is {}'.format(value_list))
        nextPT_x1 = (x1 + value_list * d_k[0])
        nextPT_x2 = (x2 + value_list * d_k[1])
        print('x_{} is ({},{})'.format(iterations,nextPT_x1,nextPT_x2))
        gradient_d_k_plus1 = np.array([gradient_x1(nextPT_x1,nextPT_x2),gradient_x2(nextPT_x2,nextPT_x1)])
        print('Gradient_d_k_plus1 is currently {}'.format(gradient_d_k_plus1))

        # Check if Gradient_d_k_plus1 is 0 for Minima
        if(gradient_d_k_plus1[0]==0 and gradient_d_k_plus1[1]==0):
            print('FINAL MINIMA is ({},{})'.format(nextPT_x1,nextPT_x2))
            break

        # Choosing beta by fletcher-reeves
        gT = np.transpose(gradient_d_k_plus1)
        gT_minus1 = np.transpose(gradient_d_k)
        beta_k_plus1 = (np.matmul(gT,gradient_d_k_plus1))/(np.matmul(gT_minus1,gradient_d_k))
        print('Value of beta({}) is {}'.format(iterations,beta_k_plus1))

        # Choosing conjugate direction
        d_k_plus1 = -gradient_d_k_plus1 + beta_k_plus1*d_k
        print('Conjugate direction is {}'.format(d_k_plus1))
        print('')


conjugateGradientDescent()
