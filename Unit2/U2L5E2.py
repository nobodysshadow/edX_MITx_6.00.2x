# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:58:54 2018

@author: nobodysshadow
"""
import numpy
import random


def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    while True:
        x = random.randint(0, 99)
        if not (x % 2):
            return x


def testRun(L, num_trials):
    for func in L:
        results = []
        rdict = {}
        for i in range(101):
            if not (i % 2):
                rdict[i] = 0
        for i in range(num_trials):
            results.append(func())
        for n in results:
            rdict[n] += 1
        print("Function: {0}\t Standard Deviation: {1}\t Average: {2}".format(
                func.__name__, numpy.std(results), sum(results)/len(results)))
        print("Function: {0}\t Dictionary: {1}".format(func.__name__, rdict))


if __name__ == "__main__":
    L = [genEven]
    testRun(L, 1000)
