#!/usr/bin/python
"""
Cw5 the pinacle of grupwork and efficienceyc and comroodery

Calculus module implementing
discrete function function
differentiation function
and trapezoidal integration function

"""


import numpy as np
import math

def diff(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = np.zeros(len(x))
    z = np.zeros(len(x))
    h = (b-a)/float(n)
    for i in xrange(len(x)):
        y[i] = f(x[i])
    for i in xrange(len(x)-1):
        z[i] = (y[i+1] - y[i])/h
    z[n] = (y[n] - y[n-1])/h
    return y, z

def sin(x):
    return math.sin(x)

def diff2(f, a, b, n):
    #x, y = discrete_func(f, a, b, n)
    matrix = []
    h = ( b - a ) / float(n)
    count = -1
    for i in range(n):
        for j in range(n):
            matrix[i].append(0)
        if(count >= 0 and count < n - 1):
            matrix[i][count] = 1 / (2 * h)
            matrix[i][count++ + 2] = -1 / (2 * h)
    matrix[0][0] = -1 / h
    matrix[0][1] = 1 / h
    matrix[-1][-1] = 1 / h
    matrix[-1][-2] = -1 / h
    print matrix


def discrete_func(f, a, b, n):
    x = np.linspace(a, b, n+1)
    g = np.vectorize(f)
    y = g(x)
    return x, y




