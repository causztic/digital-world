#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:16:35 2017

@author: yaojie
"""
from week2 import fahrenheit_to_celsius, position_velocity, minutes_to_years_days, Coordinate, area_of_triangle,compound_val_sixth_months

print fahrenheit_to_celsius(32)
print fahrenheit_to_celsius(-40)
print fahrenheit_to_celsius(212)

print position_velocity (5.0 , 10.0)
print position_velocity (5.0 , 0.0)
print position_velocity (0.0 , 5.0)

print minutes_to_years_days (1000000000)
print minutes_to_years_days (2000000000)

print " Test Case 1 "
p1 = Coordinate(1.5, -3.4)
p2 = Coordinate(4.6, 5)
p3 = Coordinate(9.5, -3.4)

print area_of_triangle(p1,p2,p3)

print " Test Case 2 "
p1 = Coordinate(2.0, -3.4)
p2 = Coordinate(4.6, 5)
p3 = Coordinate(9.5, -1.4)

print area_of_triangle(p1,p2,p3)

print " Test Case 3 "
p1 = Coordinate(1.5, 3.4)
p2 = Coordinate(4.6, 5)
p3 = Coordinate(-1.5, 3.4)

print area_of_triangle(p1,p2,p3)

print " Test Case 4 "
p1 = Coordinate(-1.5, 3.4)
p2 = Coordinate(4.6, 5)
p3 = Coordinate(4.3, -3.4)

print area_of_triangle(p1,p2,p3)


print compound_val_sixth_months (100 ,0.05)
print compound_val_sixth_months (100 ,0.03)
print compound_val_sixth_months (200 ,0.05)
print compound_val_sixth_months (200 ,0.03)


msa = raw_input("Enter the monthly saving amount: ")
air = raw_input("Enter annual interest rate: ")
print "After the sixth month, the account value is {}".format(round(compound_val_sixth_months(float(msa), float(air)), 2))