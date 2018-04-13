# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 20:10:16 2018

@author: nobodysshadow
"""

import numpy
import random


def dist1():
    return random.random() * 2 - 1


def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1


def dist3():
    return int(random.random() * 10)


def dist4():
    return random.randrange(0, 10)


def dist5():
    return int(random.random() * 10)


def dist6():
    return random.randint(0, 10)


def testRun(L, num_trials):
    for func in L:
        results = []
        for i in range(num_trials):
            results.append(func())
        print("Function: {0}\t Standard Deviation: {1}\t Average: {2}".format(
                func.__name__, numpy.std(results), sum(results)/len(results)))


if __name__ == "__main__":
    L = [dist1, dist2, dist3, dist4, dist5, dist6]
    testRun(L, 1000000)
