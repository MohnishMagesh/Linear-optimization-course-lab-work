import sympy
from sympy import *
import numpy

def fun(x1,x2):
    f = x1**2 + x2**2
    # f =((x1)**2)+((x2)**2)+x1*x2
    return f

def dfun(a,b):
    x1= Symbol('x1')
    x2= Symbol('x2')
    function = ((x1)**2)+((x2)**2)+x1*x2
    df=Derivative(function,x1)
    df1=Derivative(function, x2)
    x=(df.doit().subs({x1:a,x2:b}))
    y=(df1.doit().subs({x1:a,x2:b}))
    d=numpy.array([x,y])
    return d

b=0.0001
s=0.9
def gradientDescent(x1,x2,a):
    grad=dfun(x1,x2)
    d=numpy.multiply(-1,grad)
    a1=a
    x=numpy.array([x1,x2])
    p=numpy.multiply(a1,d)
    LHS=numpy.add(p,x)
    m=LHS[0]
    n=LHS[1]
    value_x1=fun(m,0)
    value_x2=fun(0,n)
    value=fun(m,n)
    funCurrent=numpy.array((value_x1,value_x2))
    transposeValue=funCurrent.T
    matrixMultiply=numpy.multiply(transposeValue,d)
    con=a*b
    finalRHS1=matrixMultiply[0]+matrixMultiply[1]
    finalRHS2=con*finalRHS1
    RHS=fun(x1,x2)+finalRHS2

    if value <= RHS:
        print("Wolfe condition 1  satisfied")
        print("enter wolfe condition 2")
        LHS_armijo=s*finalRHS1
        transposeValue_new=funCurrent.T
        matrixMultiply_new=numpy.multiply(transposeValue_new,d)
        RHS_armijo=s*(matrixMultiply_new[0]+matrixMultiply_new[1])
        if LHS_armijo>=RHS_armijo:
            print("the following is the point",m,n)
        else:
            print("Armijo condition not satisfied")
            a1=0.5*a
            gradientDescent(1,2,a1)
    else:
        print("Wolfe condition 1 not satisfied")
        a1=0.5*a
        gradientDescent(1,2,a1)


gradientDescent(1,2,1)
