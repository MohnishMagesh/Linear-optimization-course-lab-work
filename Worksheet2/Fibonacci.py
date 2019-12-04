import math as m

fib = [1,1]

for i in range(2,200):
    x = fib[i-1] + fib[i-2]
    fib.append(x)

def f(x):
    return x * m.exp(-x)
    # return m.pow(x,3) * m.pow(m.exp(1),m.pow(-x,2))
    # return x * m.pow((1+m.pow(x,2)),-1) #/v/
    # return m.pow(x,2) + (54/x)
    # return m.pow(x,5) * m.exp(-abs(x)) #/iv/
    # return (1 - m.pow(x,2)) * m.pow((1 + m.pow(x,2)),-1) #/vi/

def fibSearch(a,b,n):
    a_1 = a
    b_1 = b
    E = m.pow(10,-6)

    L_fixed = b - a

    x1 = 0
    x2 = 0

    k = 2

    iterations = 0

    while(k>0 and k<n):
        L_prime = (fib[n-k+1]/fib[n+1]) * L_fixed
        x1 = a_1 + L_prime
        x2 = b_1 - L_prime

        if (f(x1) <= f(x2)):
            b_1 = x2
        if (f(x1) > f(x2)):
            a_1 = x1
        if (abs(b_1 - a_1) < E):
            k = -2

        k+=1
        iterations+=1

    print('No of iterations are:')
    print(iterations)

    print('the initial interval is reduced, new interval is:')
    print('[{}, {}]'.format(a_1, b_1))

fibSearch(0,5,100)
