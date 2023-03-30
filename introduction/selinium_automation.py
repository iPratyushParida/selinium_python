'''
Created on 30-Mar-2023

@author: Pratyush Kumar
'''
print("hello world of python selinium")
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://github.com/")
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.quit()
