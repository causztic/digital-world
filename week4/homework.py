#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:13:24 2017

@author: yaojie
"""
from collections import Counter


def f_to_c(f):
    return round((float(f) - 32) * (5.0 / 9), 1)


def f_to_c_approx(f):
    return round((f - 30) / 2.0, 1)


def get_conversion_table():
    return [[i, f_to_c(i), f_to_c_approx(i)] for i in range(0, 101, 10)]


def get_conversion_table2():
    array = [[], [], []]
    for i in range(0, 101, 10):
        array[0].append(i)
        array[1].append(f_to_c(i))
        array[2].append(f_to_c_approx(i))
# for part c you can do an if string check. But I lazy


def max_list(inlist):
    return [max(l) for l in inlist]


def multiplication_table(n):
    if n < 1:
        return None
    return [[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]


def most_frequent(li):
    m = 0
    arr = []
    for i in Counter(li).most_common():
        if i[1] >= m:
            m = i[1]
            arr.append(i[0])
        else:
            break
    return arr


def diff(p):
    d = {}
    p.pop(0, None)  # remove constant
    for k, v in p.iteritems():
        d[k - 1] = k * v
    return d
