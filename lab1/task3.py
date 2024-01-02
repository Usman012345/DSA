# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:16:35 2023

@author: ApriZon
"""
import numpy as np
def minimun(array,a,b):
    arr=[]
    for x in range(a,b):
        arr.append(array[x])
    arr.sort()  
    smallest=arr[0]
    for x in range(a,b):
        if smallest==array[x]:
            smallest=x
            return smallest
        
arr=[3,4,7,8,0,1,23,-2,-5]
a=int(input("Enter starting index"))
b=int(input("Enter ending index"))
smallest=minimun(arr,a,b)
print(smallest)


