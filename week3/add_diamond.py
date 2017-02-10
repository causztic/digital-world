#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:03:37 2017

@author: yaojie
"""

import sys
import random
from homework import is_prime

height = int(sys.argv[1])
patterns = [['o','x'],['*','+'],['@','#']]
pattern = random.choice(patterns)
count = 1

def stars(number):
    str = ''
    for i in range(count, count+number):
        if is_prime(i):
            str += (pattern[0] + " ")
        else:
            str += (pattern[1] + " ")
    return str

for i in range(height-1,0,-1) + range(0,height):
    j = (height-i)*2-1
    print ' '*i*2, stars(j)
    count+=j