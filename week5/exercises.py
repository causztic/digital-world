#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:46:53 2017

@author: yaojie
"""
n = 3
A = [i for i in range(n, 0, -1)]
B = []
C = []
count = 0

def move_disks(n, src, to, aux):
    #Step 1: If h>1 then first use this procedure to move the h−1 smaller disks from peg A to peg B.
    #Step 2: Now the largest disk, i.e. disk h can be moved from peg A to peg C.
    #Step 3: If h>1 then again use this procedure to move the h−1 smaller disks from peg B to peg C.
    if n > 0:
        move_disks(n-1, src, aux, to)
        to.append(src.pop())
        global count
        count += 1
        print A, B, C
        move_disks(n-1, aux, to, src)
    
move_disks(n, A, B, C)
print("Most efficient number of steps: %d" % (2**n-1))
print("Steps taken: %d" % count)