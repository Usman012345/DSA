# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:05:19 2023

@author: ApriZon
"""

arrp=[]
arrn=[]
x=int(input("Enter the number of elements"))
arr=[]
for i in range(0,x):
    y=int(input("Enter the numbers"))
    if y>=0:
        arrp.append(y)
    else:
        arrn.append(y)
while len(arrp)>0 or len(arrn)>0:
    if len(arrn)>0:
        arrn.sort()
        arr.append(arrn[0])
        del(arrn[0])
    if len(arrp)>0:
        arrp.sort()
        arr.append(arrp[0])
        del(arrp[0])     
print(arr)
