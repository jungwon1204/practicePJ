import numpy as np

import matplotlib.pyplot as plt



def numerical_diff(f,x):

    h = 1e-4 #0.0001

    return (f(x+h)-f(x-h))/2*h



# y=0.01x^2+0.1x

def function_1(x):

    return x**3



x = np.arange(-100.0,150.0, 0.1)

y = function_1(x)

#y = numerical_diff(function_1, x)

plt.xlabel("x")

plt.ylabel("f(x)")

plt.plot(x,y)

plt.show()