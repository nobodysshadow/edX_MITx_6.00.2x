# -*- coding: utf-8 -*-
# UNIT 3 - Lecture 8 - Inferential Statistics - Exercise 4
# You have a bucket with 3 red balls and 3 green balls. Assume that once you
# draw a ball out of the bucket, you don't replace it. What is the probability
# of drawing 3 balls of the same color?
# Write a Monte Carlo simulation to solve the above problem. Feel free to write
# a helper function if you wish.
"""
Created on Thu Apr 25 10:29:54 2018
@author: nobodysshadow
"""
import numpy as np
import random
import time

def noReplacementSimulation_V1(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # random.seed(time.time())
    success = 0
    for i in range(numTrials):
        balls = ["R","R","R","G","G","G"]
        draws = []
        for b in range(3):
            draws.append(random.choice(balls))
        if draws[0] == draws[1] and draws[0] == draws[2]:
            success += 1
    return abs((success/float(numTrials)))


def noReplacementSimulation_v2(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    #random.seed(0)
    numNeedles = 10
    estimates = []
    for n in range(numTrials):
        success = 0
        for i in range(numNeedles):
            balls = ["R","R","R","G","G","G"]
            draws = []
            for b in range(3):
                draws.append(random.choice(balls))
            if draws[0] == draws[1] and draws[0] == draws[2]:
                success += 1
        estimates.append(3.5*(success/(9*numNeedles)))
    sDev = np.std(estimates)
    curEst = sum(estimates)/len(estimates)
    return curEst

def oneTrial():
    '''
    Simulates one trial of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns True if all three balls are the same color,
    False otherwise.
    '''
    balls = ['r', 'r', 'r', 'g', 'g', 'g']
    chosenBalls = []
    for t in range(3):
        # For three trials, pick a ball
        ball = random.choice(balls)
        # Remove the chosen ball from the set of balls
        balls.remove(ball)
        # and add it to a list of balls we picked
        chosenBalls.append(ball)
    # If the first ball is the same as the second AND the second is the same as the third,
    #  we know all three must be the same color.
    if chosenBalls[0] == chosenBalls[1] and chosenBalls[1] == chosenBalls[2]:
        return True
    return False

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTrue = 0
    for trial in range(numTrials):
        if oneTrial():
            numTrue += 1

    return float(numTrue)/float(numTrials)


def noReplacementSimulation_ext1(numTrials):   
    success = 0
    for t in range(numTrials):
        balls = ["R","R","R","G","G","G"]
        first = random.choice(balls)
        balls.remove(first)
        second = random.choice(balls)
        if second == first:
            balls.remove(second)
            third = random.choice(balls)
            if third == second:
                success += 1
    return float(success)/numTrials


def noReplacementSimulation_ext2(numTrials):
    return sum(sum(random.sample((0,0,0,-3,-6,9),3))==0  
               for n in range(numTrials)) / numTrials

test1 = 5000
test2 = 5
print("Test1:\t\t{:0.4f}".
      format(noReplacementSimulation(test1)))

result = []
for i in range(test2):
    result.append(noReplacementSimulation(test1))
print("Test2:\t\t{:0.4f}".
      format(np.mean(result)))
