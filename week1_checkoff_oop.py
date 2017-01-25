# This is exactly the same as week1_checkoff except it is object oriented.

import names
from random import randint

class Student:

    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
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
        return reduce(lambda x,y: x+y, self.marks) / len(self.marks)

    def printAverageMarks(self):
        print "{} of id {} has scored an average of {}".format(self.name, self.id, self.averageMarks())

    def printPassOrFail(self):
        result = ( "Pass" if self.averageMarks() >= 50 else "Fail" )
        print "{} of id {} has has a result of {}".format(self.name, self.id, result)

    def printGrade(self):
        print "{} of id {} has an average grade of {} and grade of {}".format(self.id, self.name, self.averageMarks(), self.grade)

def printGradeArray(students):
    for i in students:
        i.printGrade()

students = []
for i in range(1,41):
    students.append(Student(i, names.get_full_name(), [randint(0,100) for _ in range(3)]))

printGradeArray(students)