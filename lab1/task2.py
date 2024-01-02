# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:06:41 2023

@author: ApriZon
"""

import numpy as np

X=[22,2,1,7,11,13,5,2,9]
X.sort()
y=int(input("Enter number"))
arr=[]
f=0
for x in range(0,len(X)):
    if y==X[x]:
        arr.append(x)
        f=1
        continue
    else:
        continue
    if f==1:
        break
print(arr)