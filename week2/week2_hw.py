#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:58:11 2017

@author: yaojie
"""
import math
# question 1
def celsius_to_fahrenheit(c):
    return float(c)*9.0/5+32

# question 2
def area_vol_cylinder(radius,length):
    area = radius*radius*math.pi
    return area, area*length

# question 3
def wind_chill_temp(temp, windspeed):
    return 35.74+0.6215*temp-35.75*windspeed**0.16+0.4275*temp*windspeed**0.16


# question 4
def bmi(weight, height):
    pound = 0.45359237
    inch = 0.0254
    return (weight*pound)/(height*inch)**2


# question 5
def investment_val(ia, air, num):
    return round(ia*(1+air/1200)**(num*12),2)