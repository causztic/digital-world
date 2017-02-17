 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:41:55 2017

@author: yaojie
"""
def compound_value_months(ms, air, n):
    mir = air/12
    value = 0
    i = 0
    while i < n: 
        value = (ms+value)*(1+mir)
        i += 1
    return round(value, 2)

def find_average(li):
    new_li = []
    s = 0
    count = 0
    for l in li:
        count += len(l)
        s+= sum(l)
        length = float(len(l) or 1)
        new_li.append(sum(l)/length)
    return new_li, s/float(count or 1)

def transpose_matrix(m):
    return [[i[j] for i in m] for j in range(len(m[0]))]

def get_details(name, ks, li):
    for l in li:
        if l["name"] == name:
            return l[ks]
    return None

def get_base_counts(DNA):
    invalid = 'The input DNA string is invalid'
    d = {}
    total = 0
    for item in ["A", "T", "C", "G"]:
        c = DNA.count(item)
        if c:
            d[item] = c
            total += c
    if total != len(DNA):
        return invalid
    else:
        return d