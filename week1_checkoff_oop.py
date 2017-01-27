# This is exactly the same as week1_checkoff except it is object oriented.
# It can be improved with properties! https://www.programiz.com/python-programming/property

import names
from random import randint

class Student:

    def __init__(self, name, uid, marks):
        self.name = name
        self.uid = uid
        self.marks = marks
        self.setGrade()

    def setGrade(self):
        avg = self.averageMarks()
        self.grade = 'F'
        if avg >= 90:
            self.grade = 'A'
        elif avg >= 80:
            self.grade = 'B'
        elif avg >= 70:
            self.grade = 'C'
        elif avg >= 60:
            self.grade = 'D'

    def averageMarks(self):
        return sum(self.marks) / len(self.marks)

    def printAverageMarks(self):
        print "{} of uid {} has scored an average of {}".format(self.name, self.uid, self.averageMarks())

    def printPassOrFail(self):
        result = ( "Pass" if self.averageMarks() >= 50 else "Fail" )
        print "{} of uid {} has has a result of {}".format(self.name, self.uid, result)

    def printGrade(self):
        print "{} of uid {} has an average grade of {} and grade of {}".format(self.uid, self.name, self.averageMarks(), self.grade)

def printGradeArray(students):
    for i in students:
        i.printGrade()

students = []
for i in range(1,41):
    students.append(Student(i, names.get_full_name(), [randint(0,100) for _ in range(3)]))

printGradeArray(students)