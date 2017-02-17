#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:18:40 2017

@author: yaojie
"""
from functions import find_average,compound_value_months, transpose_matrix, get_details, get_base_counts

for ms, air, n in [[100,0.05,6],[100,0.03,7],[200,0.05,8],[200,0.03,1]]:
    print compound_value_months(ms, air, n)

print find_average([[13.13 ,1.1 ,1.1] ,[] ,[1 ,1 ,0.67]])
print find_average([[],[],[]])
print find_average([[3,4],[5,6,7],[-1,2,8]])

print transpose_matrix([[1 ,2 ,3] , [4 ,5 ,6] , [7 ,8 ,9]])
print transpose_matrix([[1 ,2 ,3,4] , [5 ,6,7,8] , [9,10,11,12]])
print transpose_matrix([[1 ,2 ,3] , [4 ,5 ,6] , [7 ,8 ,9],[10,11,12]])

phonebook =[{ 'name': 'Andrew' , 'mobile_phone' :9477865 , 'office_phone' :6612345 , 'email': 'andrew@sutd.edu.sg'} ,{ 'name': 'Bobby' ,'mobile_phone' :8123498 , 'office_phone' :6654321 , 'email': 'bobby@sutd.edu.sg' }]
print get_details ( 'Andrew' , 'mobile_phone' , phonebook )

print get_base_counts("AACCGT")
print get_base_counts("AACCGTACTGGTCGATCGATCGGATCG")
print get_base_counts("AACaCGT")