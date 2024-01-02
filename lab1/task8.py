# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 18:55:27 2023

@author: ApriZon
"""

def sortarr(a,b):
    for x in range(0,len(b)):
        for y in range(0,len(a)):
            if b[x]<a[y]:
                a.insert(y, b[x])
    return a         

A=[0,3,4,10,11]
B=[1,8,13,24]
result=sortarr(A,B)
print(result)