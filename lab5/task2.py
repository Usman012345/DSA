# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:34:22 2023

@author: ApriZon
"""

import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pandas as pd
class Mainwindow(QMainWindow):
    def __init__(self):
        
        super(Mainwindow,self).__init__()
        loadUi("task2.ui",self)
        self.resize(1365, 1000)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Closebutton.clicked.connect(lambda: self.close())
        self.City.currentIndexChanged.connect(self.fill_values)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Agentname.setFont(font)
       # self.scrollArea.scrollContentsBy(9, 10)
       # self.scrollArea.scroll(0,10)
       # self.setupUi(QMainWindow)
        
       # self.setStyleSheet('font-size: 40px')
        
    def fill_values(self,index):
        tehsil=[["Tehsil","lahore cantt","Raiwand","Gulberg"],["Tehsil","Murree","Kotli sattian"],["Tehsil","Chak Jhumra","Jaranwala"],["Tehsil","Daska","Pasrur"]]
        self.Tehsil.clear()
        if self.City.currentIndex()==1:
            self.Tehsil.addItems(tehsil[0])
        elif self.City.currentIndex()==2:
            self.Tehsil.addItems(tehsil[1])
        elif self.City.currentIndex()==3:
            self.Tehsil.addItems(tehsil[2])
        elif self.City.currentIndex()==4:
            self.Tehsil.addItems(tehsil[3])
        #self.City.currentIndexChanged.connect(self.fill_values)
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())