#!/usr/bin/python
import numpy as np
import calculus #from cw5
import math


def arclength(g, a, b, n):
    xlist = np.linspace(a, b, n+1)
    f = np.vectorize(g)
    ylist = f(xlist)
    difflist = calculus.diff(f, a, b, n)[1]
    s = np.zeros(n+1)
    #s will hold the incremental values of each indivual arc length at first
    il = np.vectorize(incremental_lengther)
    s[1:] = il(difflist[1:])
    #now traverse backwards to sum individual points
    for i in xrange(n, -1, -1):
        s[i] = np.sum(s[:i+1])
    return s

def incremental_lengther(derivative):
    return (1 + derivative**2) ** .5


def sin(x):
    return math.sin(x)

def zeroX(x):
    return 0

def test_arclength(f1 = sin, f2 = zeroX):
    """
    Checks that for sin(x) and f(x) = 0, the arclengths
    are identical when using the mesh that increments by pi
    
    """
    assert (arclength(f1, 0, 100*math.pi, 100) == arclength(f2, 0, 100*math.pi, 100)).all()

