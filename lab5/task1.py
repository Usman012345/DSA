# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 19:20:15 2023

@author: ApriZon
"""

import time
import numpy as np
import sys
sys.setrecursionlimit(60000)
from numpy import random
def randomarray(size):
        arr=random.randint(-5,5,size=(size))
        return arr
def writefile(arr):
    f=open(file="quicksort.csv",mode="w")
    for i in arr:
        f.write(str(i)+"\n")
def quicksort(arr,start,end):
    mid=int(end/2)
    if start<end:
        q=partition(arr,start,end)
        quicksort(arr,start,q-1)
        quicksort(arr,q+1,end)
    return arr
def partition(arr,start,end):
    x=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j]<=x:
            i=i+1
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            
    temp2=arr[i+1]
    arr[i+1]=arr[end]
    arr[end]=temp2
    return i+1
start=time.time()         
x=10
result=randomarray(x)
print(result)
array=quicksort(result,0,x-1)
print(array)
end=time.time()
run=end-start
print(run)
writefile(array)