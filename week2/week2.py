#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:27:24 2017

@author: yaojie
"""

# question 1
def fahrenheit_to_celsius(f):
    '''converts fahrenheit to celsius'''
    return (float(f) - 32)*(5.0/9)

# question 2
def position_velocity(v0, t):
    g = 9.81
    y = v0*t-0.5*g*t**2
    y_prime = v0 - g*t
    return round(y, 2), round(y_prime, 2)

# question 3
def minutes_to_years_days(minutes):
    years = minutes / (365*24*60)
    days = (minutes - years*365*24*60)/(24*60)
    return (years, days)

def verbose_minutes_to_years_days(minutes):
    years, days = minutes_to_years_days(int(minutes))
    print "{} minutes is approximately {} years and {} days.".format(minutes, years, days)

# verbose_minutes_to_years_days(raw_input("Enter the number of minutes: "))

# question 4
class Coordinate(object):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

def area_of_triangle(p1, p2, p3):
    s1 = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    s2 = ((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2) ** 0.5
    s3 = ((p3.x - p1.x) ** 2 + (p3.y - p1.y) ** 2) ** 0.5
    s = (s1+s2+s3)/2
    area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
    return area

# question 5
def compound_val_sixth_months(ms, air):
    '''ms = monthly savings
       air = annual interest rates'''
    mir = air/12
    value = 0
    i = 0
    while i < 6: 
        value = (ms+value)*(1+mir)
        i += 1
