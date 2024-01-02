# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:16:09 2023

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
def minimum(arr):
    x=arr[0]
    for i in range(0,len(arr)):
        if arr[i]<x:
            temp=x
            x=arr[i]
            arr[i]=temp
    return x
def maximum(arr):
    x=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>x:
            temp=x
            x=arr[i]
            arr[i]=temp
    return x
def writefile(arr):
    f=open(file="bubblesort.csv",mode="w")
    for i in arr:
        f.write(str(i)+"\n")
def countingsort(arr,maximum,minimum):
    size=maximum+minimum+1
    print(size)
    b=np.zeros(size)
    t=0
    q=0
    x=1
    for z in range(0,len(b)):
        
        for i in range(0,len(arr)):
            if arr[i]==int(z):
                b[z]+=(int(x))
    for j in range(0,len(b)):
        t=b[j]
        for k in range(0,int(t)):
            arr[q]=j
            q+=1
    return arr
            
start=time.time()         
x=10
result=randomarray(x)
print(result)
y=maximum(result)
x=minimum(result)
array=countingsort(result,y,x)
print(array)
end=time.time()
run=end-start
print(run)
#writefile(array)