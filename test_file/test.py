from sympy import *
 
x = symbols('x') #x를 기호변수화
fx = 4 * x ** 4 + 3 * x ** 3 +  2 * x ** 2 + x + 1
 
fprime = Derivative(fx, x).doit() #x에 대해서 미분
print("fx 의 도함수는 : ", fprime, "입니다")
fdoubleprime = Derivative(fprime, x).doit() # fprime 에 대하여 미분
print("fx의 이계도함수는 : ", fdoubleprime, "입니다")
a = solve(fdoubleprime, x)
print(a)
