# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:47:34 2018

@author: nobodysshadow
"""
import numpy
import random


def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    for i in range(10, 21, 2):
        return i


def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number
    between 9 and 21
    '''
    return random.choice([10, 12, 14, 16, 18, 20])


def testRun(L, num_trials):
    for func in L:
        results = []
        rdict = {}
        for i in [10, 12, 14, 16, 18, 20]:
            rdict[i] = 0
        for i in range(num_trials):
            results.append(func())
        for n in results:
            rdict[n] += 1
        print("Function: {0}\t Standard Deviation: {1}\t Average: {2}".format(
                func.__name__, numpy.std(results), sum(results)/len(results)))
        print("Function: {0}\t Dictionary: {1}".format(func.__name__, rdict))


if __name__ == "__main__":
    L = [deterministicNumber, stochasticNumber]
    testRun(L, 1000)
