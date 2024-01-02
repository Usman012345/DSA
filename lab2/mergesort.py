# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:42:26 2023

@author: ApriZon
"""
import time
import numpy as np
from numpy import random
import sys
sys.setrecursionlimit(60000)

def randomarray(size):
        arr=random.randint(-15000,15000,size=(size))
        return arr
def writefile(arr):
    f=open(file="insertionsort.csv",mode="w")
    for i in arr:
        f.write(str(i)+"\n")
def merge(L,R):
    result=[]
    i=0
    j=0
    while i < len(L) and j < len(R):
        if L[i]<R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1
    while i<len(L):
        result.append(L[i])
        i+=1
    while j<len(R):
        result.append(R[j])
        j+=1
    return result
            
def mergesort(arr,start,end,middle):
    if len(arr)<=1:
        return arr
    L=[]
    R=[]
    for i in range(0,int(middle)):
        L.append(arr[i])
    for j in range(int(middle),end):
        R.append(arr[j])
    L=mergesort(L, 0, len(L), len(L)/2)
    R=mergesort(R,0,len(R),len(R)/2)
    return merge(L,R)
start=time.time()         
x=30000
result=randomarray(x)
print(result)
array=mergesort(result,0,x,int(x/2))
print(array)
end=time.time()
run=end-start
print(run)
writefile(array)