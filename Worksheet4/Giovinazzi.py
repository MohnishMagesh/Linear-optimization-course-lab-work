import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def f(x1,x2):
    # return x1*(x2**2)
    return (x1**2)+(x2**2)
    # return (x1-x2)**2 + (x2+x1)**2 #/a/
    # return (1-x1)**2 + 100*((x2-x1**2)**2) #/b/
    # return (1.5-x1+x1*x2)**2 + (2.25-x1+(x1*(x2**2)))**2 + (2.625-x1+(x1*(x2**3)))**2 #/c/
    # return sp.sqrt((1.5-x1)**2+(2.5)**2) + sp.sqrt((15-x1)**2+(x2)**2) + sp.sqrt((3)**2+(3.5-x2)**2)

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

def gradDescent():
    # initial Point
    x1 = 2
    x2 = 2

    # Set same as initial point
    nextPT_x1 = 2
    nextPT_x2 = 2

    iterations = 0

    while(iterations<200):
        iterations+=1
        print('Iteration number {}'.format(iterations))
        x1 = nextPT_x1
        x2 = nextPT_x2
        gradient_d_k = np.array([gradient_x1(x1,x2),gradient_x2(x2,x1)])
        print('Gradient_d_k is currently {}'.format(gradient_d_k))
        norm_d_k = m.pow(m.pow(gradient_x1(x1,x2),2)+m.pow(gradient_x2(x2,x1),2),0.5)
        print('Norm is currently {}'.format(norm_d_k))
        d_k = -1 * gradient_d_k
        print('d_k is {}'.format(d_k))
        d_k_0_norm = d_k[0]/norm_d_k
        print('d_k_0_norm is {}'.format(d_k_0_norm))
        d_k_1_norm = d_k[1]/norm_d_k
        print('d_k_1_norm is {}'.format(d_k_1_norm))
        d_k = np.array([d_k_0_norm,d_k_1_norm])
        print('x_{} is ({},{})'.format(iterations-1,x1,x2))
        print('d_{} is {}'.format(iterations-1,d_k))

        # Next point is xk+1 = xk + alpha * dk
        alpha = sp.Symbol('alpha')
        nextPT_x1 = x1 + alpha * d_k[0]
        nextPT_x2 = x2 + alpha * d_k[1]
        func_expr = f(nextPT_x1,nextPT_x2)
        # print(func_expr)
        temp = sp.diff(func_expr,alpha)
        list_1 = sp.solve(temp,alpha)
        list_2 = []
        for i in list_1:
            try:
                if(i>0 or i<=0):
                    list_2.append(i)
            except:
                continue

        print('List 2 {}'.format(list_2))
        value_list = min(list_2)
        print ('Alpha minimized is {}'.format(value_list))
        nextPT_x1 = (x1 + value_list * d_k[0])
        nextPT_x2 = (x2 + value_list * d_k[1])
        print(nextPT_x1)
        print(nextPT_x2)
        gradient_d_kk_vir = np.array([gradient_x1(nextPT_x1,nextPT_x2),gradient_x2(nextPT_x2,nextPT_x1)])
        print(gradient_d_kk_vir)
        if(abs(gradient_d_kk_vir[0])<0.0001 and abs(gradient_d_kk_vir[1])<0.0001):
            print('Minima of the function is ({},{})'.format(nextPT_x1,nextPT_x2))
            break

gradDescent()
