import math as m

golden_ratio = 1.618034
one_by_gr = 0.618034

def f(x):
    # return ((4*m.pow(x,3))+(m.pow(x,2))-(7*x)+(14))
    # return x * m.exp(-x)
    # return m.pow(x,3) * m.exp(m.pow(-x,2))
    # return x * m.pow((1+m.pow(x,2)),-1)
    # return (1 - m.pow(x,2)) * m.pow((1 + m.pow(x,2)),-1)
    # return m.pow(x,2) * m.exp(m.pow(-x,2))
    # return (1 - m.pow(x,2)) * m.pow((1 + m.pow(x,2)),-1)
    # return m.pow(x,5) * m.exp(-abs(x))
    return m.pow(m.pow(1.5-x,2)+m.pow(2.5-0,2),0.5) + m.pow(m.pow(12-x,2)+m.pow(3.5-0,2),0.5)

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

    print('the initial interval is reduced, new interval is:')
    print('[{}, {}]'.format(a_1, b_1))
    print('')
    print('Minimum is:')
    print(f(a_1))
    print('')

goldenSearch(1.5, 12)
