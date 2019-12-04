# Using golden search method

import math as m

golden_ratio = 1.618034
one_by_gr = 0.618034

def f(xR):
    return m.pow(m.pow(1.5-xR,2)+m.pow(2.5-0,2),0.5) + m.pow(m.pow(12-xR,2)+m.pow(3.5-0,2),0.5)

def goldenSearch(a, b):
    a_1 = a
    b_1 = b
    E = m.pow(10,-8)

    x1 = 0
    x2 = 0

    L_fixed = b - a

    iterations = 2

    while(iterations>0):
        L_prime = m.pow(one_by_gr,iterations) * L_fixed
        x1 = a_1 + L_prime
        x2 = b_1 - L_prime

        if (f(x1) <= f(x2)):
            b_1 = x2
        if (f(x1) > f(x2)):
            a_1 = x1
        if ((b_1 - a_1) < E):
            print('No. of iterations is:')
            print(iterations-2)
            print('')
            iterations = -2

        iterations+=1

    print('the x-axis point is :')
    print('[{}, {}]'.format(a_1, b_1))
    print('')
    print('Minimum is:')
    print(f(a_1))
    print('')

# For using golden search we require upper bound and lower bound
goldenSearch(1.5, 12)
