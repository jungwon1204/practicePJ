import numpy as np

import matplotlib.pyplot as plt


from sympy import *
 
x = symbols('x') #x를 기호변수화
fx = 4 * x ** 4 + 3 * x ** 3 +  2 * x ** 2 + x + 1
 
fprime = Derivative(fx, x).doit() #x에 대해서 미분
print("fx 의 도함수는 : ", fprime, "입니다")
fdoubleprime = Derivative(fprime, x).doit() # fprime 에 대하여 미분
print("fx의 이계도함수는 : ", fdoubleprime, "입니다")
a = solve(fdoubleprime, x)
print(a)

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