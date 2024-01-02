# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:14:43 2023

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
    f=open(file="selectionsort.csv",mode="w")
    for i in arr:
        f.write(str(i)+"\n")
def selectionsort(arr,start,end):
    min=arr[0]
    temp=0
    for x in range(start,end):
        min=arr[x]
        for y in range(start+x,(end)):
            if arr[y]<min:
                temp=min
                min=arr[y]
                arr[x]=min
                arr[y]=temp
                
        arr[x]=min   
        
    return arr
start=time.time()         
x=30000
result=randomarray(x)
print(result)
array=selectionsort(result,0,x)
print(array)
end=time.time()
run=end-start
print(run)
writefile(array)