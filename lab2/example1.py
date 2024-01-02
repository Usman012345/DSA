# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 08:30:46 2023

@author: ApriZon
"""

import time
import sys
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())
def factorial(n):
     if n==0:
         return 1
     else:
         return n*factorial(n-1)
start=time.time()
n=int(1500)
result=factorial(n)
end=time.time()
run=end-start
print("The time taken is ",run)