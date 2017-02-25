#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 09:29:47 2017

@author: yaojie
"""

from functions import leap_year, day_of_week_jan1, num_days_in_month, display_calendar, print_space_display_calendar, factorial
import unittest
import math
import random

class Week5Tests(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(leap_year(4))
        self.assertTrue(leap_year(400))
        self.assertFalse(leap_year(100))
        self.assertFalse(leap_year(1))
    
    def test_jan1(self):
        self.assertEqual(day_of_week_jan1(1800), 3)
        self.assertEqual(day_of_week_jan1(2099), 4)
        self.assertIsNone(day_of_week_jan1(1799))
        self.assertIsNone(day_of_week_jan1(2100))

    def test_num_days_in_month(self):
        self.assertEqual(num_days_in_month(2, True), 29)
        self.assertEqual(num_days_in_month(2, False), 28)
    
    def test_calendar(self):
        calendar = display_calendar(2015)
        print calendar
        print "START"
        print print_space_display_calendar(calendar)
        print "END"
    def test_factorial(self):
        r = random.randint(1, 100)
        self.assertEqual(math.factorial(r), factorial(r))
        self.assertEqual(factorial(0), 1)

if __name__ == '__main__':
    unittest.main()
