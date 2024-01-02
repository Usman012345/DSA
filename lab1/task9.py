# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 19:14:46 2023

@author: ApriZon
"""
def Palindrome(x):
    if x[::-1]==x:
        return "Palindrome"
    else:
        return "non Palindrome"
        


x=input("Enter the word ")
result=Palindrome(x)
print(result)