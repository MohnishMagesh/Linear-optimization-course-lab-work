from matplotlib import pyplot as plt
import math as m
import numpy as np
from math import e as euler

x_axis = np.linspace(0,10,10000)
y_axis = []
for x in x_axis:
    # var = x * m.exp(-x) #/i/
    # var = ((4*m.pow(x,3))+(m.pow(x,2))-(7*x)+(14))
    # var = m.pow(x,3) * m.pow(euler,m.pow(-x,2)) #/iii/
    var = m.pow(x,5) * m.exp(-abs(x)) #/iv/
    # var = x * m.pow((1+m.pow(x,2)),-1) #/v/
    # var = (1 - m.pow(x,2)) * m.pow((1 + m.pow(x,2)),-1) #/vi/
    # var = m.pow(x,2) * m.exp(m.pow(-x,2)) #/ii/
    y_axis.append(var)



plt.plot(x_axis, y_axis)
plt.show()
