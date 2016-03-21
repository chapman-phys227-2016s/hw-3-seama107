#!/usr/bin/python
"""
Loan.py
Calculates the amount left to be paid on a loan
given the initial amount, N months, and the interest rate p
"""

import numpy as np


def simple_loan(L, N, p):
    """
    Returns a pair of numpy arrays, one of values for a loan L,
    and the other of the monthly charges to be paid
    over the course of N months with interest rate p as an
    integer
    """
    x_n = np.zeros(N+1)
    x_n[0] = L
    y_n = np.zeros(N+1) 
    for i in xrange(1, N+1):
        y_n[i] = p * x_n[i-1] / 1200 + (L/N)
        x_n[i] = x_n[i-1] + p * x_n[i-1] / 1200 - y_n[i]
    return x_n, y_n

def test_zero_loan():
    """
    Tests simple_loan on L = 0, where x_n and y_n should
    end up both being 0 throughout
    """
    function_output = simple_loan(0, 12, 5)
    x_n = function_output[0]
    y_n = function_output[1]
    test_zeros = np.zeros(13)
    assert np.all(x_n == test_zeros)
    assert np.all(y_n == test_zeros)

def test_zero_interest():
    """
    Tests simple_loan on p = 0 where y_n should be constant
    throughout
    """
    y_n = simple_loan(120, 12, 0)[1]
    y_test = np.empty(13)
    y_test.fill(10)
    y_test[0] = 0
    assert np.all(y_n == y_test)