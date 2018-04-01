# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:40:24 2018

@author: nobodysshadow
"""
# Unit1 - Lecture 2 - Exercise 2
import random

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'

def buildItems():
    return [Item(n,v,w) for n,v,w in (
        ('clock ', 175, 10),
        ('painting ', 90, 9),
        ('radio ', 20, 4),
        ('vase ', 50, 2),
        ('book ', 10, 1),
        ('computer ', 200, 20)
        )]

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]

def yieldAllCombos(items):
  """
  Generates all combinations of N items into two bags, whereby each item is in one or zero bags.
  Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
  """
  N = len(items)
  for i in range(3**N):
    combo1 = []
    combo2 = []
    for j in range(N):
      if (i >> j) % 2 == 1:
        combo1.append(items[j].getName())
      elif (i >> j) % 2 == 0:
        combo2.append(items[j].getName())
    yield (combo1, combo2)

# Solution posted by a peer student!
'''
Good example for creating a powerset (finding all possoble combination)
https://stackoverflow.com/questions/1482308/whats-a-good-way-to-combinate-through-a-set

'''
from itertools import *

def powerSet(iterables):
    combo = []
    for r in range(len(iterables) + 1):
        combo.append(list(combinations(iterables,r)))
    return combo

test = powerSet(['a', 'b', 'c'])
print(test)