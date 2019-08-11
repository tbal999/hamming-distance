# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:47:24 2019

import random

@author: Tom Balcombe
"""
import random

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
    print(ham)

test1 = "12831298371298371978312"
test2 = "12312467628312309819284"

hammingA(test1,test2)
