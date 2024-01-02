
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:21:55 2023

@author: ApriZon
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

service = Service(executable_path="C:/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
driver.get("https://www.flipkart.com/gaming-laptops-store?otracker=nmenu_sub_Electronics_0_Gaming%20Laptops&otracker=nmenu_sub_E")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
# print(soup)
for a in soup.findAll('div', attrs={'class': '_3YgSsQ'}):
    print(a)
    name = a.find('a', attrs={'class': 's1Q9rs'})
    price = a.find('div', attrs={'class': '_30jeq3'})
    rating = a.find('div', attrs={'class': '_3LWZlK'})
    if name is None:
        products.append("0")
    else:
        products.append(name.text)

    if price is None:
        prices.append("0")
    else:
        prices.append(price.text)

    if rating is None:
        ratings.append("0")
    else:
        ratings.append(rating.text)

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')