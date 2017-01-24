#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:33:39 2017

@author: yaojie
"""
# 1
print type("This is the first Week!")
print "This is the first Week!"
print type(24)
print 24
print type(2.4)
print 2.4
print type("24")
print "24"
# print type(’2.4’) Error
print type("""2.4""")
# print type(’’’2.4’’’) Error
print 10300
print 10,300
print 10.300
print type(10.300)

# 2
print int(1.1)
print int(9.81)
print int(-9.81)
# print int("9.81")
# print int("9.81m/s2")
print float("9.81")
print str(9.81)
print type(str(9.81))
print str(int(9.81))
print type(str(int(9.81)))

# 3
"""
 3ai)
 name 'pi' is not defined
 3.14159
 3.14
 3.14

 <type 'str'>
 <type 'int'>
 <type 'float'>
"""
# 4
# 23days is error
days23 = 23
# day 23 is error
mymoney2 = 23
# mymoney$ = 23 is error
myclass = 23
# class = 23 is error
my_grade = 23
# my_grade_is_B+ is error

# 5
print "COORDINATES"
class Coordinate (object):
    x = 3.2
    y = -1.5
p1 = Coordinate()
p2 = Coordinate()
p2.x = 0.3
p2.y = 1.0

print type(p1)
print type(p2)
print type(Coordinate)
print p1.x, p1.y
print p2.x, p2.y

# 6
print 5 + 3 #8
print 5 - 3 #5
print 5 * 3 #15
print 5 ** 3 #125
print 5 / 3 #1
print 5 // 3 #1
print 5 / 3.0 # 1.6666666666666667
print 5.0 / 3 # 1.6666666666666667
print 5 % 3 # 2

# 7
17-3*7/4+1 # 13
2**2**4*3  # 196608

# 8
3, 5
3, 1
3, 6

# 9