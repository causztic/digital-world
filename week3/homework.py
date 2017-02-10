#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:30:13 2017

@author: yaojie
"""
import sys
import math
sys.path.append('../week2/')

from week2 import fahrenheit_to_celsius
from week2_hw import celsius_to_fahrenheit


def check_value(n1,n2,n3,x):
    return x > n1 and x > n2 and x < n3

def temp_convert(unit, number):
    if unit == 'C':
        return fahrenheit_to_celsius(number)
    elif unit == 'F':
        return celsius_to_fahrenheit(number)

def get_even_list(values):
    l = []
    for v in values:
        if v % 2 == 0:
            l.append(v)
    return l

def is_prime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if n % 2 == 0: 
        return False
    # step by 2 because all even divisions are already accounted for.
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

def f(t, y):
    return 3.0+math.exp(-t)-0.5*y

def approx_ode(h,t0,y0,tn):
    ######### h - step size
    ######### t0 - initial t value (at step 0)
    ######### y0 - initial y value (at step 0)
    ######### tn - t value at step n
    t = t0 # set time to initial time
    y = y0 # set y to initial y value
    for i in range(1,int(tn/h)+1):
        # move from 1 to the number of steps based on t.
        # if t = 3, step size = 0.1, will have 30 steps.
        # add 1 as range is exclusive.
        
        y += float(h)*f(t, y)
        # use the function
        
        t += h
        # add step size to t

    return round(y,3)

#for i in range(3, 6):
#    print approx_ode(0.1, 0, 1, i)