#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:51:52 2017

@author: yaojie
"""
import names
from random import randint

def average(marks):
    return reduce(lambda x,y: x+y, marks) / len(marks)

def printAverage(name, id, marks):
    print "{} of id {} has scored an average of {}".format(name, id, average(marks))

def printPassOrFail(name, id, marks):
    result = ( "Pass" if average(marks) >= 50 else "Fail")
    print "{} of id {} has has a result of {}".format(name, id, result)

def printGrade(name, id, marks):
    avg = average(marks)
    grade = 'F'
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    print "{} of id {} has an average grade of {} and grade of {}".format(name, id, avg, grade)

def printGradeArray(students):
    for i in students:
        printGrade(i["name"], i["id"], i["marks"])

students = []
for i in range(1,41):
    students.append({"id": i, "name": names.get_full_name(), "marks": [randint(0,100) for _ in range(3)]})

printGradeArray(students)