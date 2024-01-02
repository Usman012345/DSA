# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:27:43 2023

@author: ApriZon
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:14:43 2023

@author: ApriZon
"""
import time
import numpy as np
import sys
sys.setrecursionlimit(60000)
from numpy import random
def randomarray(size):
        arr=random.randint(-15000,15000,size=(size))
        return arr
def writefile(arr):
    f=open(file="bubblesort.csv",mode="w")
    for i in arr:
        f.write(str(i)+"\n")
def bubblesort(arr,start,end):
    x=start
    sorted=0
    temp=0
    while(x<=end):
      if sorted==1:
            x=0
            sorted=0
      for y in range(x+1,(end)):
            
            if arr[y]<arr[x]:
                temp=arr[x]
                temp2=arr[y]
                arr[x]=arr[y]
                arr[y]=temp
                x=y
                sorted=1
            else: 
                break
      x+=1   
        #starty+=1    
    return arr 
start=time.time()         
x=30000
result=randomarray(x)
print(result)
array=bubblesort(result,0,x)
print(array)
end=time.time()
run=end-start
print(run)
writefile(array)