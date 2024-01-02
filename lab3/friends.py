# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:18:10 2023

@author: ApriZon
"""
import time
import numpy as np
import sys
sys.setrecursionlimit(6000000)
def selectionsort(arr,start,end):
    min=arr[0]
    temp=0
    for x in range(start,end):
        min=arr[x]
        for y in range(start+x,(end)):
            if arr[y][0]<min[0]:
                temp=min
                min=arr[y]
                arr[x]=min
                arr[y]=temp
                
        arr[x]=min   
        
    return arr
def friendsFaster(array):
    x=len(arr)
    element1=[]
    element2=[]
    paired=0
    z=0
    i=0
    t=0
    if (array[i][0]>=array[t][0] and array[i][0]<=array[t][1]) or(array[i][1]>=array[t][0] and array[i][1]<=array[t][1]) :
           element1.append(i+1)
           element2.append((t+1))
           paired=1
           if paired==1:
               z+=1
               paired=0
           t+=1 
           if t==x:
               i+=1        
    if i<x:
        friendsFaster(array)
    if i==x:
        pair=list(zip(element1,element2)) 
        return pair
def firendSlower(array):
    x=len(arr)
    element1=[]
    element2=[]
    paired=0
    z=0
    i=0
    while(i<x):
        for t in range(i+1,x):
                if (array[i][0]>=array[t][0] and array[i][0]<=array[t][1]) or(array[i][1]>=array[t][0] and array[i][1]<=array[t][1]) :
                       element1.append(i+1)
                       element2.append((t+1))
                       paired=1
                       if paired==1:
                           z+=1
                           paired=0
        i+=1
    pair=list(zip(element1,element2))    
    return pair
def friends(array,x):
   pair=[]
   paired=0
   z=0
   i=0
   while(i<x):
       for t in range(i+1,x):
               if (array[i][0]>=array[t][0] and array[i][0]<=array[t][1]) or(array[i][1]>=array[t][0] and array[i][1]<=array[t][1]) :
                      pair.append(str([i+1,t+1]))
                      paired=1
                      if paired==1:
                          z+=1
                          paired=0
       i+=1
       
   return pair
   
x=int(input("Enter the number of entries "))
arr=np.empty((x,2),dtype=int)
for i in range (x):
    y=int(input("Enter the entry time "))
    z=int(input("Enter the leave time "))
    arr[i]=[y,z]
option=int(input("Enter which function you want \n 1.Friends \n 2.FrendSlower \n 3.FriendsFaster \n"))
start=time.time()
if option==1:
    result=friends(arr,x)
elif option==2:
    result=firendSlower(arr)
elif option==3:
    # a= selectionsort(arr, 0, len(arr))
    result= friendsFaster(arr)
end=time.time()
run=end-start
#print(a)
print(run)
print(result)