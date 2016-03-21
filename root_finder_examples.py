#!\usr\bin\python
"""
root_finder_examples.py
Author: Michael Seaman
implements the Newtonian method, Bisection method, and secant method
for finding roots to functions
"""

import numpy as np

def Newton(f, x, dfdx, epsilon=1.0E-7, N=100):
    """
    Uses Newtons method to approximate the location of a root in f(x),
    given the derivative dfdx and number of steps N, and the margin of error
    epsilon. returns a 3-tuple of x, n, and f(x)
    """
    n = 0
    f_value = f(x)
    while abs(f_value) > epsilon and n <=N:
        x = x - f_value/float(dfdx(x))
        n += 1
        f_value = f(x)
    return x, n, f(x)

def Bisection(f, a, b, epsilon = 1.0E-5):
    """
    Uses the bisection method to find an approximate root on f(x)
    returns root, iterations, and the approximate f(root)
    """
    fa = f(a)
    if fa * f(b) > 0:
        return
    i = 0
    while b-a > epsilon:
        i+= 1
        m = (a+b)/2.0
        fm = f(m)
        if fa * fm <= 0:
            b = m
        else:
            a = m
            fa = fm
    return m, i, f(m)

def Secant(f, x_minus2, x_minus1, epsilon = 1.0E-4, N = 10000):
    """
    Uses the Secant method to solve for f(x) = 0 given the values 
    to start at x_-2 and x_-1. returns a 3-tuple of x, n, and f(x)
    """
    x = x_minus2
    n = 0
    while abs(f(x)) > epsilon and n <=N:
        n+= 1
        temp = x
        x = x_minus1 - ( (f(x_minus1)*(x_minus1 - x_minus2))/(f(x_minus1) - f(x_minus2)) )
        x_minus2 = x_minus1
        x_minus1 = temp
    return x, n, f(x)


def f_1(x):
    return x**3 + x - 27

def dfdx_1(x):
    return 3*x**2 + 1

def f_2(x):
    return -5*x + 10

def dfdx_2(x):
    return -5

def f_3(x):
    return x**2 + 1


def test_Bisection_on_positive_func():
    assert Bisection(f_3, -100, 100) == None

def test_Bisection_on_root():
    assert ( abs(Bisection(f_2, -100, 100)[0] -2) < 1.0E-5 and Bisection(f_2, -100, 100)[2] < 1.0E-5 )

def test_Newton_linear():
    """
    Tests the newtonian method on a line -5x + 10
    regardless of the input for x, the equation should finish in
    one step
    """
    xTestList = np.linspace(-300,300, 87)
    vectorized_Newton = np.vectorize(Newton)
    outputList = vectorized_Newton(f_2, xTestList, dfdx_2)
    stepList = outputList[1]
    zeroList = outputList[2]
    assert( np.all(stepList) == 1 and np.all(zeroList) < 1.0E-7 )

