# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:47:24 2019

import random

@author: Tom Balcombe
"""

xlist = []
ylist = []
hamminglist = []

def hammingA(x,y):
    for i in x:
        xlist.append(i)
    for i in y:
        ylist.append(i)
    if len(xlist) != len(ylist):
        print("Length does not Match")
        return()
    hammingB(x,y)

def hammingB(x,y):
    xindex = 0
    ham = 0
    for a in xlist:
        if a == ylist[xindex]:
            ham = ham+1
        xindex = xindex+1
    hamminglist.append(ham)
    print("Hamming distance is:",len(xlist)-ham)

test1 = "234455"
test2 = "232255"

hammingA(test1,test2)
