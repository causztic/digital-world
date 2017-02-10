#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:48:34 2017

@author: yaojie
"""

def is_larger(n1, n2):
    return n1 > n2

def letter_grade(mark):
    if type(mark) == int and mark <= 100 and mark >= 0:
        grade = 'E'
        if mark >= 90:
            grade = 'A'
        elif mark >= 80:
            grade = 'B'
        elif mark >= 70:
            grade = 'C'
        elif mark >= 60:
            grade = 'D'
        return grade

def list_sum(values):
    if len(values) > 0:
        return float(sum(values))
        # return reduce(lambda x, y: x+y, values)
    else:
        return 0.0

def list_sum_newbie(values):
    c = len(values)
    s = 0.0
    while c > 0:
        s += values[c-1]
        c -= 1
    return s
        
def minmax_in_list(values):
    if len(values) > 0:
        maximum = values[0]
        minimum = values[0]

        for value in values[1:]:
            if value > maximum:
                maximum = value
            if value < minimum:
                minimum = value
        return minimum, maximum
    else:
        return None, None

def is_palindrome(number):
    s = str(number)
    return s == s[::-1]
#    l = len(s)
#    if l % 2 == 0:
#        # if even, take the first half == reversed of second half.
#        # e.g. l = 4, s[:l/2] would be 0,1 and 2 exclusive.
#        # s[:l/2-1] means ending at 1.
#        # normally this would result in the first item only, 
#        # but since with -1 step we can go backwards, we will take 3,2, and stop at 1 exclusive.
#        return s[:l/2] == s[:l/2-1:-1]
#    else:
#        # compares the first half with the second half, reversed.
#        return s[:l/2] == s[:l/2:-1]