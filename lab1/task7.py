# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:37:00 2023

@author: ApriZon
"""
def rowsum(a):
    sum=0
    row=[]
    for x in range(0,len(a)):
        for i in range(0,len(a[x])):
             sum+=a[x][i]       
        row.append(sum)  
        sum=0
    print(row)
def columnsum(a):
    sum=0
    column=[]
    for x in range(0,len(a)):
        for i in range(0,len(a[x])):
             sum+=a[i][x]       
        column.append(sum)  
        sum=0
    print(column)
    
    
    
    
A=[[1,13,13],[5,11,6],[4,4,9]]
x=input("Enter whether you want to find sum a row or columnwise: ")
if x=="row":
    rowsum(A)
if x=="column":
    columnsum(A)
    