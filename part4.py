# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:03:03 2023

@author: ApriZon
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
url ="https://www.ncbi.nlm.nih.gov/geoprofiles/?term=genbank" 
r="C:/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=r)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.ncbi.nlm.nih.gov/geoprofiles/?term=genbank")
time.sleep(10)
content=driver.page_source
soup=BeautifulSoup(content,"html.parser")
CourseCode=[]
NO=[]
Description=[]
CLO1=[]
CLO2=[]
CLO3=[]
CLO4=[]
Textbook1=[]
Textbook2=[]
Instructor=[]
Semester=[]
links = []
textlist=[]
clos_=[]
"""
for x in soup.findAll("div", attrs={"class": "rprt"}):
    anchor = x.find('a', href=True)
    if anchor:
        link = anchor["href"]
        links.append(link)
"""
for x in range(0,1):
    textlist=[]
    clos_=[]
    driver.get(url)
    time.sleep(10)
    content_ = driver.page_source
    soup_ = BeautifulSoup(content_,"html.parser")
    no_ = soup_.find('div',attrs={"class":"rprtnum nohighlight"})
    no=no_.find('span')
    #_no=no_(len(no_)-1)
    #no=_no(len(_no)-1)
    print(no.text.strip())
    if no!=None:
        NO.append(no.text.strip())
    else:
        NO.append("None")
    """
    coursecode=soup_.find('div',attrs={"id":"CourseCode"})
    if coursecode!=None:
        CourseCode.append(coursecode.text.strip())
    else:
        CourseCode.append("None")
    description=soup_.find('p',attrs={"id":"CourseDescription"})
    if description !=None:
        Description.append(description.text.strip())
    else:
        Description.append("None")
    clos = soup_.find('ul', attrs={"id": "CourseClos"})
    print(clos)
    if clos!=None:
        clositems = clos.find_all('li')
        print(clositems)
        for clo in clositems:
            if clo!=None:
                clos_.append (clo.text.strip())
            else:
                clos_.append("No Clo found")
    print(clos_)
    if len(clos_)>0:
        CLO1.append(clos_[0])
    else:
        CLO1.append("None")
    if len(clos_)>1:
        CLO2.append(clos_[1])
    else:
        CLO2.append("None")
    if len(clos_)>2:
        CLO3.append(clos_[2])
    else:
        CLO3.append("None")
    if len(clos_)>3:
        CLO4.append(clos_[3])
    else:
        CLO4.append("None")
        
    textbooks=soup_.find('ul',attrs={"id":"CourseBooks"})
    if textbooks!=None:
        textbooks_=textbooks.find_all('li')
    for text__ in textbooks_:
        if text__!=None:
            textlist.append(text__.text.strip())
        else:
            textlist.append("No book found")
    if len(textlist)>0:
        Textbook1.append(textlist[0])
    else:
        Textbook1.append("None")
    if len(textlist)>1:
        Textbook2.append(textlist[1])
    else:
        Textbook2.append("None")
print(len(Title))
print(len(CourseCode))
print(len(Description))
print(len(CLO1))
print(len(CLO2))
print(len(CLO3))
print(len(CLO4))
print(len(Textbook1))
print(len(Textbook2))
df = pd.DataFrame({'Title': Title, 'CourseCode': CourseCode, 'Description': Description,'ClO1':CLO1,'CLO2':CLO2,'CLO3':CLO3,'CLO4':CLO4,'Textbook1':Textbook1,'Textbook2':Textbook2})
df.to_csv('Courses.csv', index=False, encoding='utf-8')
"""