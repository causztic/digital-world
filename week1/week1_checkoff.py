# if you cannot run the code, go to your command line (not the one in spyder) and type in
# pip install names

import names
from random import randint

# This function calculates the average score.
def average(marks):
    # Sum of marks is divided by the length of the marks to get the average mark across all marks.
    return sum(marks) / len(marks)

# This function prints out the average score.
def printAverage(name, id, marks):
    print "{} of id {} has scored an average of {}".format(name, id, average(marks))
    # there are various ways to print variables in strings, and this is one of them.

# This function prints out whether the student has passed or failed.
def printPassOrFail(name, id, marks):
    result = ( "Pass" if average(marks) >= 50 else "Fail" )
    # result is assigned "Pass" if average marks is over 50, otherwise it is assigned "Fail".
    print "{} of id {} has has a result of {}".format(name, id, result)

# This function prints out the grades of a student.
def printGrade(name, id, marks):
    # Conditionals will be covered in Week 3!
    # The best way to learn is to read the code to yourself and think it through, and practice!
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

# This function takes in a list of students and passes it to the function above to print them individually.
def printGradeArray(students):
    for i in students:
        printGrade(i["name"], i["id"], i["marks"])

# Over here it's generating a random list of 40 students as individual dictionaries with the help of external libraries.
# Dictionaries and lists are covered in Week 4.
# If you have trouble understanding the code, feel free to approach me and I'll explain it to you!

students = []

for i in range(1,41):
    students.append({"id": i, "name": names.get_full_name(), "marks": [randint(0,100) for _ in range(3)]})

# students.append({"id": raw_input("enter id"), "name": raw_input("enter name"), "marks": [int(raw_input("marks")) for _ in range(3)]})

printGradeArray(students)