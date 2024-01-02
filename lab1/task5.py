# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:31:34 2023

@author: ApriZon
"""
import numpy as np
def reverse(s):
       print(*s[::-1])
       
       
s="university of Engineering and Technology Lahore"
arr=s.split(" ")
x=int(input("Enter the number of word"))
reverse(arr[x])