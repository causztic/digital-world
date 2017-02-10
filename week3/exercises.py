#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:35:15 2017

@author: yaojie
"""
import math

def may_ignore(var):
    if type(var) == int:
        return var + 1
    else:
        return None

def my_reverse(li):
#    new_list = []
#    for i in li:
#        new_list.insert(0, i)
#    return new_list
    return li[::-1]

# check that you dont change the old list!

def approx_pi(n):
    s = 0
    for k in range(n+1):
        numerator = float(math.factorial(4*k)*(1103+26390*k))
        denominator = float(math.factorial(k)**4*396**(4*k))
        s += numerator/denominator
    return 1/(((2*2**0.5)/9801.0)*s)

def gcd(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    return gcd(n2, n1 % n2)

def f1(x):
    return x**2

def f2(x):
    return math.sin(x)

def f3(x):
    return math.exp(-x)
    
def simpsons_rule(f, n, a, b):
    h=(b-a)/float(n)
    first_term = reduce(lambda s, j: s+f(a+2*j*h), range(1, n/2))
    second_term = reduce(lambda s, j: s+f(a+(2*j-1)*h), range(1,n/2+1))
    return round(h/3*(f(a)+2*first_term+4*second_term+f(b)),2)
    
print simpsons_rule(f1,1000,1,3)
print simpsons_rule(f2,1000,0,math.pi)
print simpsons_rule(f3,1000,0,math.pi)
    