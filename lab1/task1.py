# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 09:54:57 2023

@author: ApriZon
"""

import numpy as np

X=[22,2,1,7,11,13,5,2,9]
y=int(input("Enter number"))
arr=[]
for x in range(0,len(X)):
    if y==X[x]:
        arr.append(x)
    
print(arr)