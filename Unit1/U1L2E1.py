# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:27:48 2018

@author: nobodysshadow
"""
'''
Exercise 1
Here is the lecture from 6.00.1x on generators. Additionally, you can also take a look at Chapter 8.3 in the textbook.
For the following problem, consider the following way to write a power set generator. The number of possible combinations to put n items into one bag is . Here, items is a Python list. If need be, also check out the docs on bitwise operators (<<, >>, &, |, ~, ^).

generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
As above, suppose we have a generator that returns every combination of objects in one bag. We can represent this as a list of 1s and 0s denoting whether each item is in the bag or not.
Write a generator that returns every arrangement of items such that each is in one or none of two different bags. Each combination should be given as a tuple of two lists, the first being the items in bag1, and the second being the items in bag2.

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.
      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
Note this generator should be pretty similar to the powerSet generator above.

We mentioned that the number of possible combinations for N items into one bag is . How many possible combinations exist when there are two bags? Think about this for a few minutes, then click the following hint to confirm if your guess is correct. Remember that a given item can only be in bag1, bag2, or neither bag -- it is not possible for an item to be present in both bags!

How many possible combinations exist for N items into two bags?
With two bags, there are  possible combinations available.
With one bag we determined there were  possible combinations available by representing the bag as a list of binary bits, 0 or 1. Since there are N bits, and they can be one of two possibilities, there must be  possibilities.
With two bags there thus must be  possible combinations. You can imagine this by representing the two bags as a list of "trinary" bits, 0, 1, or 2 (a 0 if an item is in neither bag; 1 if it is in bag1; 2 if it is in bag2). With the "trinary" bits, there are N bits that can each be one of three possibilities - thus there must be  possible combinations.

Functions referenced in the grader:
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
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),('painting', 90, 9), ('radio', 20, 4),('vase', 50, 2),('book', 10, 1),('computer', 200, 20))]

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]
'''

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

# My Version
'''
def yieldAllCombos(items):
  """
  Generates all combinations of N items into two bags, whereby each item is in one or zero bags.
  Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
  """
  N = len(items)
  # enumerate the 2**N possible combinations
  for i in range(2**N):
    combo1 = []
    for j in range(N):
      combo2 = []
      # test bit jth of integer i
      if (i >> j) % 2 == 1:
        try:
          combo1.index(items[j].getName())
        except ValueError:
          combo1.append(items[j].getName())
      else:
        try:
          combo2.index(items[j].getName())
        except ValueError:
          combo2.append(items[j].getName())
      yield (combo1, combo2)
'''

# Correct Version
def yieldAllCombos(items):
  """
  Generates all combinations of N items into two bags, whereby each item is in one or zero bags.
  Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
  """
  N = len(items)
  # Enumerate the 3**N possible combinations
  for i in range(3**N):
    bag1 = []
    bag2 = []
    for j in range(N):
      if (i // (3 ** j)) % 3 == 1:
        bag1.append(items[j])
      elif (i // (3 ** j)) % 3 == 2:
        bag2.append(items[j])
    yield (bag1, bag2)

print('items = buildItems()')
items = buildItems()
print('combos = yieldAllCombos(items)')
combos = yieldAllCombos(items)
print('Testing all the correct combinations exist in your solution')
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())

print('items = buildRandomItems(2)')
items = buildRandomItems(2)
print('combos = yieldAllCombos(items)')
combos = yieldAllCombos(items)
print('Testing all the correct combinations exist in your solution')
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())
print(combos.__next__())

'''
items = buildItems()
combos = yieldAllCombos(items)
Testing all the correct combinations exist in your solution
('', 'clock ')
('', 'painting ')
('', 'radio ')
('', 'vase ')
('', 'book ')
('', 'computer ')
('clock ', '')
('clock ', 'painting ')
('clock ', 'radio ')
('clock ', 'vase ')
('clock ', 'book ')
('clock ', 'computer ')
('', 'clock ')
('painting ', '')
('painting ', 'radio ')
('painting ', 'vase ')
('painting ', 'book ')
('painting ', 'computer ')
('clock ', '')
('clock painting ', '')
('clock painting ', 'radio ')
('clock painting ', 'vase ')
('clock painting ', 'book ')
('clock painting ', 'computer ')
('', 'clock ')
('', 'painting ')
('radio ', '')
('radio ', 'vase ')
('radio ', 'book ')
('radio ', 'computer ')
('clock ', '')
('clock ', 'painting ')
('clock radio ', '')
('clock radio ', 'vase ')
('clock radio ', 'book ')
('clock radio ', 'computer ')
('', 'clock ')
('painting ', '')
('painting radio ', '')
('painting radio ', 'vase ')
('painting radio ', 'book ')
('painting radio ', 'computer ')
('clock ', '')
('clock painting ', '')
('clock painting radio ', '')
('clock painting radio ', 'vase ')
('clock painting radio ', 'book ')
OUTPUT TRUNCATED
'''

'''
items = buildRandomItems(1)
combos = yieldAllCombos(items)
Testing all the correct combinations exist in your solution
('', '0 ')
('0 ', '')
('', '')
('<0, 50.0, 9.0> ', '')
('', '<0, 50.0, 9.0> ')
'''