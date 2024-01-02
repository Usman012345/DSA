# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:13:40 2023

@author: ApriZon
"""

import matplotlib.pyplot as plt
import pandas as pd
def line_chart():
    data = pd.read_csv("E:\DSA lab\lab4\part1_data\dailySteps_merged.csv")
    list1=data['StepTotal'].values.tolist()
    list2=data['ActivityDay'].values.tolist()
    plt.plot(list2,list1)
    plt.show()
def bar_chart():
    data=pd.read_csv("E:\DSA lab\lab4\part1_data\dailyActivity_merged.csv")
    list1=data['TotalDistance'].values.tolist()
    list2=data['ActivityDate'].values.tolist()
    plt.bar(list2,list1,width=1,color=['red','green'])
    plt.show()

def scatter_chart():
    data=pd.read_csv("E:\DSA lab\lab4\part1_data\sleepDay_merged.csv")
    list1=data['TotalTimeInBed'].values.tolist()
    list2=data['SleepDay'].values.tolist()
    plt.scatter(list2, list1)
    plt.show()
def pie_chart():
    data=pd.read_csv("E:\DSA lab\lab4\part1_data\hourlySteps_merged.csv")
    list1=data['StepTotal'].values.tolist()
    plt.pie(list1)
    plt.show()
x=int(input("Option"))
if x==1:
    line_chart()
if x==2:
    bar_chart()
if x==3:
    scatter_chart()
if x==4:
    pie_chart()