from matplotlib import pyplot as plt
import math as m
import numpy as np
from math import e as euler

x_axis = np.linspace(0.01,5,10000)
y_axis = []
for x in x_axis:
    # var = (-m.pow(x,2))/(m.pow(x,3)+m.cos(x)) #/a/
    # var = (m.pow(x,4) - m.pow(x,3) - m.pow(x,2)) * m.pow(euler,m.pow(-x,2)) #/b/
    # var = m.sin(x)/m.pow(x,0.5) #/c/
    # var = m.cos(x)/m.pow(x,0.5) #/d/
    var = (x-1) * m.pow((x-3),2) * m.pow((x+7),-2)
    y_axis.append(var)

plt.plot(x_axis, y_axis)
plt.show()
