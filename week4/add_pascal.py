#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:13:54 2017

@author: yaojie
"""

# pascal wew
import sys, math
iterations = int(sys.argv[1])

def binomial(x, y):
    binom = math.factorial(x) / (math.factorial(y) * math.factorial(x - y))
    return binom

for x in range(iterations + 1):
    string = ""
    for y in range(x+1):
        string += str(binomial(x,y)) + " "
    print string
