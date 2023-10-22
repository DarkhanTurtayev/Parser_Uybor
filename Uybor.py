import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import csv
import pandas as pd
from pandas import DataFrame
import numbers
import random
import numpy as np
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from datetime import date, datetime
import os, sys
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


ROOT = tk.Tk()
ROOT.geometry("400x200")

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Parse Uybor for search",
                                  prompt="Enter URL")

url = USER_INP
driver = webdriver.Chrome()
driver.get(url)


pagination = '&page='
try:

    page_last = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[3]/div/main/div[3]/nav/ul/li[8]/a').text
    page_last_num = int(re.search(r'\d+', page_last).group())
    print(page_last_num)
except:
    page_last_num = simpledialog.askinteger(title='How Many Pages?', prompt='Enter')    

clear_url = url.replace('&page=','')


links = []

for x in range(1, page_last_num + 1):
    try:
        
        current_url = clear_url + pagination + str(x)
        driver.get(current_url)
        driver.maximize_window
        time.sleep(2)
     

        for i in range(1,30):  
            try:
                var_link ='//*[@id="__next"]/div[2]/div[3]/div/main/div[2]/div[' + str(i) + ']/div/div/div/a[2]'
                link = driver.find_element(By.XPATH, var_link).get_attribute('href')   
            except Exception as _ex:
                link = None
            links.append(link)  

    except Exception as _ex:
        pass


'''
dt = DataFrame ({'Links': links})
filename_links = asksaveasfilename()
dt.to_excel(filename_links + '.xlsx')

dt = pd.read_excel(r'/Users/macstudiod/Desktop/links.xlsx')
df = pd.DataFrame(dt)
links = dt['links'].values.tolist()
driver = webdriver.Chrome()
'''
prices = []
pricesm2 = []
m2 = []
floors = []
adresses = []
links_new = []


for y in links:
    try:   
        driver.get(y)
        links_new.append(y)
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div[1]/div[1]').text
        except:
            price = None
        prices.append(price)


        try:
            pricem2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div[1]/div[2]').text
        except:
            pricem2 = None
        pricesm2.append(pricem2)

        try:
            sm2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div[2]/div/div[2]/div/div[2]').text

        except:
            sm2 = None
        m2.append(sm2)

        try:
            floor = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/section/div[2]/div/div[3]/div/div[2]').text
        except:
            floor = None
        floors.append(floor)

        try:
            adress = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[3]/main/section[2]/div[2]').text
        except:
            adress = None
        adresses.append(adress)
    except:
        pass    



df = DataFrame (
    {
        'Link': links_new,
        'Price': prices,
        'Prices per m2': pricesm2,
        'Square': m2,
        'Floors': floors,
        'Adress': adresses

    }

)

filename = asksaveasfilename()
df.to_excel(filename + '.xlsx')

