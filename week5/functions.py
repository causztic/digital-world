#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 09:07:56 2017

@author: yaojie
"""

import random
import calendar as cal

craps = set([2,3,12])
naturals = set([7,11])

def roll_two_dices():
    return random.randint(1,6), random.randint(1,6)

def print_lose():
    print "You lose"

def print_win():
    print "You win"

def print_point(p):
    print "your points are %d" % p

def is_craps(n):
    return n in craps

def is_naturals(n):
    return n in naturals

def play_craps():
    point =-1
    while True:
        n1,n2 = roll_two_dices()
        sumn = n1 + n2
        print 'You rolled %d + %d = %d' % (n1, n2, sumn)
        if point == -1:
            if is_craps(sumn):
                print_lose()
                return 0
            elif is_naturals(sumn):
                print_win()
                return 1
            point = sumn
            print_point(point)
        else:
            if sumn  == 7:
                print_lose()
                return 0
            elif sumn == point:
                print_win()
                return 1
                
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return (year % 400 == 0)
        else:
            return True
    else:
        return False

                
def day_of_week_jan1(year):
    # d = R(1+5R(A -1, 4)+4R(A-1,100) + 6R(A-1, 400), 7)
    if year >= 1800 and year <= 2099:
        d = (1+5*((year-1) % 4) + 4*((year-1) % 100) + 6*((year-1) % 400)) % 7    
        return d

def num_days_in_month(month_num, leap_year):    
    num_days = [31, 28, 31, 30, 31, 30,31,31,30,31,30,31]
    if leap_year and month_num == 2:
        return 29
    else:
        return num_days[month_num-1]

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    li =  [cal.month_name[month_num]]
    day = 1 - first_day_of_month
    count = 0
    temp = [""]
    while day <= num_days_in_month:
        if day <= 0:
            temp.append("  ")
        elif day < 10:
            temp.append(" %d" % day)
        else:
            temp.append(str(day))
        day += 1
        count += 1
        if count % 7 == 0 or (num_days_in_month - day) < 0:
            li.append(" ".join(temp))
            temp = [""]
    return li
    
def construct_cal_year(year):
    l = [year]
    current_first_day_of_month = day_of_week_jan1(year)
    for month in range(1, 13):
        is_leap = leap_year(year)
        num_days = num_days_in_month(month, is_leap)
        month_list = construct_cal_month(month, current_first_day_of_month, num_days)
        l.append(month_list)
        current_first_day_of_month = (len(month_list[-1].split(" ")) - 1) % 7
    return l
    
# month printing for part d
def print_cal_month( list_of_str ):
    ret_val = ''
    for l in list_of_str:
        ret_val += l.replace( ' ' , '*')
        ret_val += '\n'
    return ret_val

# year printing for part f
def print_space_display_calendar( calendar ):
    temp = calendar.replace( ' ' , '*')
    return temp.replace( '\n' , '+\n')
    
def display_calendar(calendar_year):
    s = ""
    months = construct_cal_year(calendar_year)[1:]
    for month in range(0, 12):
        # add month
        s += months[month][0] + "\n"
        s += "  S  M  T  W  T  F  S\n"
        for days in months[month][1:]:
            s += days
            if not (month == 11 and months[month].index(days) == (len(months[month]) - 1)):
                s += "\n"
        if month != 11:
            s += "\n"
    return s
    
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 0:
        return n * factorial(n-1)