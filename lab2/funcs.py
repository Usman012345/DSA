# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 08:01:04 2023

@author: ApriZon
"""
import numpy as np
from numpy import random
def randomarray(size):
        arr=random.randint(-100,100,size=(size))
        return arr
x=int(input("Enter the size of array"))
result=randomarray(x)
print(result)