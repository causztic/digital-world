#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:31:03 2017

@author: yaojie
"""
import math


def func(x):
    return x**3 * math.exp(-1)


def trapezoidal(a, b):
    return round((b - a) * (func(b) + func(a)) / 2.0, 2)

print trapezoidal(5, 6.5)
print trapezoidal(5, 5.5)
print trapezoidal(6, 6.5)
print trapezoidal(6, 2.5)
