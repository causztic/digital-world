#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:35:46 2017

@author: yaojie
"""
import random, time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code
def interlock(word1, word2, word3):
    count = 0
    # do not check if incorrect length
    if len(word1) + len(word2) != len(word3):
        return False
    
    while count < len(word3):
        if count % 2 == 0:
            if word1[count/2] != word3[count]:
                return False
        else:
            if word2[count/2] != word3[count]:
                return False
        count += 1
    return True

def throw_dice(n, nExp):
    return round((1-(5/6.0)**n),2)

def pi_approx_by_monte_carlo(n):
    m = n
    c = 0
    while n > 0:
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            c += 1
        n -= 1
    return round(4*c/float(m),2)

def game(r, N):
    M = 0  # counter for no of wins
    gain = 0
    for experiment in range(N):
        eyes = [random.randint(1,6) for i in range(4)]
        if sum(eyes) < 9:
            M += 1
            gain += r-1
        else:
            gain -= 1
    return gain >=0

def f(t,y):
    return 4.0 - t + 2.0*y
    
# runge-kutta
def approx_ode2(h,t0,y0,tn):
    y = y0
    t = t0
    for i in range(t0, int(tn/h)):
        y = y + h*(0.5*f(t,y)+0.5*f(t+h, y)+h*f(t,y))
        t += h
    return round(y,3)
    
print approx_ode2(0.1,0,1,1)
