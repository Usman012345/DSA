# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:17:38 2023

@author: ApriZon
"""

def multiply_int(a,b):
    arrA=[int(x) for x in str(a)]
    arrB=[int(x) for x in str(b)]
    if len(arrA)==1 and len(arrB)==1:
        return a*b
    carry=0
    result=[0]*(len(arrA)+len(arrB))
    for x in reversed(range(0,len(arrA))):
        for y in reversed(range(0,len(arrB))):
               p= (arrA[x]*arrB[y])+carry+result[x+y+1]
               print(p)
               carry=int(p/10)
               if p>10:
                   p=int(p%10)
               result[x+y+1]=(p)
    return result
               
c=int(input("which function you want to work \n 1.multiply int \n 2.multiply string \n 3.visulaize karatsuba, \n 4.Multiply_Recursive "))
a=input("Enter 1st digit")
b=input("Enter 2nd digit")
if c==1:
   result= multiply_int(str(a),str(b))
for i in result:
    print(i,end="")