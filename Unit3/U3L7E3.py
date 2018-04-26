# -*- coding: utf-8 -*-
# UNIT 3 - Lecture 7 - Inferential Statistics - Exercise 3
# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and
# outputs the standard deviation of the lengths of the strings. Return float
# ('NaN') if L is empty.
# Recall that the standard deviation is computed by this equation:
# sqrt(sum((t-u)^2)/N)
# where: 
# u is the mean of the elements in X.
# sum((t-u)^2) means the sum of the quantity (t-u)^2 for t in X.
# That is, for each element (that we name t) in the set X, we compute the
# quantity . We then sum up all those computed quantities.
# N is the number of elements in X.
# Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.
# Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'],
# stdDevOfLengths(L) should return 1.8708.
# If you want to use numpy arrays, you should import numpy as np and use
# np.METHOD_NAME in your code.
"""
Created on Thu Apr 24 15:14:54 2018
@author: nobodysshadow
"""
import numpy as np


def stdDevOfLengths(L: list):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    N = len(L)  # Number of elements
    if N == 0:
        return float('NaN')
    tot = 0.0
    for x in L:
        tot += len(x)
    mean = tot/float(N)
    tot = 0.0
    for x in L:
        tot += (len(x) - mean)**2
    std = (tot/N)**0.5
    return std


L1 = ['a', 'z', 'p']
L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
L3 = []
print("TestCase L1: expected 0.0000\tgot {:0.4f}".format(stdDevOfLengths(L1)))
print("TestCase L2: expected 1.8708\tgot {:0.4f}".format(stdDevOfLengths(L2)))
print("TestCase L3: expected NaN\tgot {:0.4f}".format(stdDevOfLengths(L3)))


# Last Question of Exercise 4
L4 = [10, 4, 12, 15, 20, 5]
L4std = np.std(L4)
L4mean = np.mean(L4)
print("coefficient of variation of [10, 4, 12, 15, 20, 5] to 3 decimal places =       {:0.3f}".format(L4std/L4mean))
