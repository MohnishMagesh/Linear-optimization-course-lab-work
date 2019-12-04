import math as m
import numpy as np
import random as rd
from math import e as euler
import sympy as sp

def f(x1,x2):
    # return (x1-x2)**2 + (x2+x1)**2 #/a/
    # return (x1**2)+(x2**2)
    return (x1+x2-5)**0.5
    # return (1-x1)**2 + 100*((x2-x1**2)**2) #/b/
    # return (1.5-x1+x1*x2)**2 + (2.25-x1+(x1*(x2**2)))**2 + (2.625-x1+(x1*(x2**3)))**2 #/c/
    # return sp.sqrt((1.5-x1)**2+(2.5-x2)**2) + sp.sqrt((12-x1)**2+(3.5-x2)**2)
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

def approximateLS():
    # initial point
    x1 = 5
    x2 = 5

    nextPT_x1 = 5
    nextPT_x2 = 5

    alpha = 1
    alpha_temp = 1
    rf = 0.5
    beta = 0.0001
    sigma = 0.9

    # tolerance condition
    Length_now = 10 # This is just a random value

    iterations = 0

    while(Length_now>0.000001):
        iterations+=1
        print('Iteration number {}'.format(iterations))
        print('Point currently at is ({},{})'.format(nextPT_x1,nextPT_x2))
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
        # d_k=d_k/norm_d_k
        # //print('Norm is currently {}'.format(norm_d_k))
        # d_k = np.array([-gradient_x1(x1,x2)/norm_d_k,-gradient_x2(x2,x1)/norm_d_k])
        #d_k = np.array([-gradient_x1(x1,x2)/norm_d_k,-gradient_x2(x2,x1)/norm_d_k])
        print('x_{} is ({},{})'.format(iterations-1,x1,x2))
        print('d_{} is {}'.format(iterations-1,d_k))

        # Next point is xk+1 = xk + alpha * dk
        nextPT_x1 = x1 + alpha * d_k[0]
        nextPT_x2 = x2 + alpha * d_k[1]
        gradient_d_k_plus_1 = np.array([gradient_x1(nextPT_x1,nextPT_x2),gradient_x2(nextPT_x2,nextPT_x1)])
        # d_k_plus_1 = np.array([(-gradient_x1(nextPT_x1,nextPT_x2)),-gradient_x2(nextPT_x2,nextPT_x1)])
        print('x_{} is ({},{})'.format(iterations,nextPT_x1,nextPT_x2))

        while(alpha>0.1):
            # ARMIJO's CONDITION
            gradT = np.transpose(gradient_d_k)
            directional_derivative = np.matmul(gradT, d_k)
            print(directional_derivative)
            arm_truth = (f(nextPT_x1,nextPT_x2) < f(x1,x2) + (beta * alpha * (directional_derivative)))
            print('f(x1,x2)={}'.format(f(x1,x2)))
            print('f(nextPT_x1,nextPT_x2)={}'.format(f(nextPT_x1,nextPT_x2)))
            print('LHS:')
            print(f(nextPT_x1,nextPT_x2))
            print('RHS:')
            print(f(x1,x2) + (beta * alpha * (directional_derivative)))
            print('Armijo condition is {}'.format(arm_truth))
            if(arm_truth):
                # WOLFE's CONDITION
                gradTNP = np.transpose(gradient_d_k_plus_1)
                directional_derivative_k = np.matmul(gradTNP, d_k)
                print(directional_derivative_k)
                wolfe_truth = (directional_derivative_k >= (sigma * directional_derivative))
                print('Wolfe\'s condition:-')
                print('LHS = {}'.format(directional_derivative_k))
                print('RHS = {}'.format(sigma * directional_derivative))
                print('Wolfe condition is {}'.format(wolfe_truth))
                if(wolfe_truth):
                    break
                elif(wolfe_truth==False):
                    alpha = alpha * rf
                    continue
            elif(arm_truth==False):
                alpha = alpha * rf

        # tolerance condition
        Length_now = (f(x1,x2) - f(nextPT_x1,nextPT_x2))/(abs(f(x1,x2)))
        print(Length_now)
        print(alpha)

    print('Minimised interval is {}'.format(Length_now))
    print('Point of minima is ({},{})'.format(x1,x2))
approximateLS()
