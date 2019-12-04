import matplotlib.pyplot as plt
import math as m
import numpy as np

x_axis = []
y_axis = []
n = 10000000
for x in range(0,n):
    var = m.pow(x,5) * m.exp(-abs(x))
    x_axis.append(x)
    y_axis.append(var)

limit_infinite = ((y_axis[n] - y_axis[(n/100)-1])/(y_axis[(n/100)-1]))
print(limit_infinite)

plt.plot(x_axis,y_axis)
plt.show()
