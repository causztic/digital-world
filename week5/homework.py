#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:32:51 2017

@author: yaojie
"""
from functions import construct_cal_year

def get_data():
    return raw_input("Enter integer pair (hit Enter to quit): \n")


def extract_values(s):
    n1, n2 = s.split(" ")
    return (int(n1), int(n2))


def calc_ratios(t):
    """calculates the ratio between two numbers in a list"""
    if t[1] == 0:
        return None
    return float(t[0]) / t[1]

def display_calendar(calendar_year, month):
    calendar = construct_cal_year(calendar_year)[1:]
    if month == None:
        return pretty_display_calendar(calendar)
    else:
        return pretty_display_month(month - 1, calendar, False)


def pretty_display_month(month, months, padding=True):
    s = ""
    s += months[month][0] + "\n"
    s += "  S  M  T  W  T  F  S\n"
    for days in months[month][1:]:
        s += days
        if months[month].index(days) != (len(months[month]) - 1):
            s += "\n"
        if padding and months[month].index(days) == (len(months[month]) - 1):
            s += "\n"
    return s


def pretty_display_calendar(months):
    s = ""
    for month in range(0, 12):
        s += pretty_display_month(month, months)
        if month != 11:
            s += "\n"
    return s

print display_calendar(2002, None)
