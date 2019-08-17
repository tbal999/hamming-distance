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
    ham = 0
    for index, a in enumerate(xlist):
        if a == ylist[index]:
            ham = ham+1
    hamminglist.append(ham)
    print("Hamming distance is:",len(xlist)-ham)


test1 = input("Type in first string:" )
test1str = str(test1)
test2 = input("Type in second string:" )
test2str = str(test2)

hammingA(test1str,test2str)
