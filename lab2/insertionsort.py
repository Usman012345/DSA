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
    f=open(file="insertionsort.csv",mode="w")
    for i in arr:
        f.write(str(i)+"\n")
def insertionsort(arr,start,end):
    x=start
    sorted=0
    temp=0
    while(x<=end):
      if sorted==1:
            x=0
            sorted=0
      for y in range(x+1,(end)):
            
            if arr[y]<arr[x] and y-1==x:
                temp=arr[x]
                temp2=arr[y]
                arr[x]=arr[y]
                arr[y]=temp
                #x=y
                sorted=1
                for z in reversed(range(0,y-1)):
                    if arr[z]>arr[x]:
                        temp=arr[x]
                        temp2=arr[z]
                        arr[x]=arr[z]
                        arr[z]=temp
                        #x=z
                        #sorted=1
                    else:
                        break
            else: 
                break
      x+=1   
        #starty+=1    
    return arr 
start=time.time()         
x=30000
result=randomarray(x)
print(result)
array=insertionsort(result,0,x)
print(array)
end=time.time()
run=end-start
print(run)
writefile(array)