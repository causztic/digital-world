#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:49:30 2017

@author: yaojie
"""

from functions import is_larger, letter_grade, list_sum, minmax_in_list, is_palindrome, list_sum_newbie

print is_larger(2 , -1)
print is_larger(-1 , 2)
print is_larger(2 , 2)
print ''

for mark in [102,100,83,75,67,52,-2]:
    print letter_grade(mark)
print ''

print "Test case 1: [4.25, 5.0, 10.75] "
value = [4.25 ,5.0 ,10.75]
print list_sum (value), list_sum_newbie(value)

print " Test case 2: [5.0] "
value = [5.0]
print list_sum (value), list_sum_newbie(value)
print " Test case 3: [] "
print list_sum ([]), list_sum_newbie([])
print ''


for idx, l in enumerate([[1,2,3,4,5],[1,1,3,0],[3,2,1],[0,10],[1],[],[1,1,1,1,1]]):
    print "Test case {}: {}".format(idx+1, l)
    print minmax_in_list(l)
print ''

for idx, n in enumerate([1,22,12321,441232144,441231144,144,12,1441]):
    print "Test case {}: {}".format(idx+1, n)
    print is_palindrome(n)
print ''