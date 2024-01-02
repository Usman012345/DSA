# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 09:19:27 2023

@author: ApriZon
"""
def sum(x):
    s=0
    while x!=0:
        s=s+x%10
        x=x/10

    print(int(s))
        
    
x=int(input("Enter the number"))
b=len(str(x))
s=0
method=int(input("Chose method   1. iterative    2.recursive"))
if method==1:
    for i in range(0,b):
        s=s+x%10
        x=x/10
        
    print(int(s))
if method==2:
    sum(x)