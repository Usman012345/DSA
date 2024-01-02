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
Link=[]
NO=[]
Organism=[]
Annotation=[]
Reportor=[]
Samples=[]
Datasets=[]
ID=[]
links = []
textlist=[]
samples_=[]
n=[]
"""
for x in soup.findAll("div", attrs={"class": "rprt"}):
    anchor = x.find('a', href=True)
    if anchor:
        link = anchor["href"]
        links.append(link)
"""
for x in range(0,20):
    textlist=[]
    clos_=[]
    driver.get(url)
    time.sleep(10)
    content_ = driver.page_source
    soup_ = BeautifulSoup(content_,"html.parser")
    no_ = soup_.find('div',attrs={"class":"rprtnum nohighlight"})
    no=no_.find('span')
    n=no.text.strip().split(".")
    no=n[0]
    if no!=None:
        NO.append(no)
    else:
        NO.append(0)
    link_=soup_.find('div',attrs={"class":"rsltcont"})
    anchor = link_.find('a', href=True)
    if anchor:
        link ="https:/" +anchor["href"]
    if link!=None:
        Link.append(link)
    else:
        Link.append("None")
    organism_=soup_.find_all('dl',attrs={"class":"details"})
    organism=organism_[1].find('dd')
    if organism !=None:
        Organism.append(organism.text.strip())
    else:
        Organism.append("None")    
    annotation_=soup_.find_all('dl',attrs={"class":"details"})
    annotation=annotation_[0].find('dd')
    if annotation !=None:
        Annotation.append(annotation.text.strip())
    else:
        Annotation.append("None") 
    reportor=annotation_[2].find('dd')
    if reportor !=None:
        Reportor.append(reportor.text.strip())
    else:
        Reportor.append("None")
    r=annotation_[3].find('dd')
    samples_=r.text.strip().split(",")
    _samples=samples_[2]
    s=_samples.split(" ")
    samples=s[1]
    if samples !=None:
        Samples.append(int(samples))
    else:
        Samples.append(0)
    d=annotation_[3].find('dd')
    dataset=d.text.strip()
    if dataset !=None:
        Datasets.append(dataset)
    else:
        Datasets.append(0)
    id_ = soup_.find('div',attrs={"class":"resc"})
    _id=id_.find('dd')
    print(_id.text.strip())
    if _id!=None:
        ID.append(_id)
    else:
        ID.append(0)
df = pd.DataFrame({'NO': NO, 'Annotation': Annotation, 'Reportor': Reportor,'Samples':Samples,'Dataset':Datasets,'ID':ID,'Organism':Organism,'Link':Link})
df.to_csv('Project.csv', index=False, encoding='utf-8')