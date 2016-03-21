#!/usr/bin.python
"""
sin_Taylor_series_diffeq.py
Author: Michael Seaman


"""

import math
import numpy as np

def aj(x, i, prev):
    return -(x ** 2) * prev / (4*i**2 + 2*i)

def sin_Taylor(x, n):
    """
    Uses the taylor series approximation to guess the value of sin(x)
    given n values in the series
    method aj is called upon, but sj is imbedded within this function
    returns the sum of the series to n and the next value in the series
    """
    if n == 0:
        return 0, aj(x, 1,x)
    aj_array = np.zeros(n+1)
    aj_array[0] = x
    for i in xrange(n):
        aj_array[i+1] = aj(x, i+1,aj_array[i])
    #print aj_array
    return np.sum(aj_array[:n-1]), aj_array[len(aj_array)-1]


def test_zero_sin_Taylor():
    assert sin_Taylor(0, 100)[0] == 0 and abs(sin_Taylor(2*math.pi, 100)[0]) < 1.0E-5

def test_sin_Taylor_v_math_sin():
    assert abs(sin_Taylor(4, 100)[0] - math.sin(4)) < 1.0E-5