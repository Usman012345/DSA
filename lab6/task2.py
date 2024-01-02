# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:17:20 2023

@author: ApriZon
"""

import time
import numpy as np
import sys
sys.setrecursionlimit(60000)
from numpy import random
def randomarray(size):
        arr=random.randint(0,5,size=(size))
        return arr
def maximum(arr):
    x=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>x:
            temp=x
            x=arr[i]
            arr[i]=temp
    y=x
    count=0
    while(y!=0):
        y=int(y/10)
        count+=1
    return count
def writefile(arr):
    f=open(file="bubblesort.csv",mode="w")
    for i in arr:
        f.write(str(i)+"\n")
def radixsort(arr,maximum):
    b=np.zeros(10)
    z=1
    i=0
    for t in range(0,maximum):
        for f in range(0,t):
            z=z*10
        for x in range(0,len(arr)):
            y=int( arr[x]/z)
            y=int(y%10)
            b[y].append(arr[x])
        for h in b:
            arr[i]=h
            i+=1
    return arr
            
start=time.time()         
x=10
result=randomarray(x)
print(result)
y=maximum(result)
array=radixsort(result,y)
print(array)
end=time.time()
run=end-start
print(run)
#writefile(array)