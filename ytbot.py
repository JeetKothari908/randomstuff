import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
import time
import pandas as pd
import numpy as np
import pyautogui
import mouse




youtube = input("do you want to search things on youtube? ")
if youtube == 'yes':
    searching = input("what do you want to search? ")
    views = input('how many view do you want? ')
    views = int(views)
    starter = 0
    x = int(starter)
    while x < views:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
        wait = WebDriverWait(driver, 25)
        driver.get(searching)
        wait.until(expected_conditions.element_to_be_clickable((By.ID,"button" )))
        button = find_element_by_id('button')
        button.click()
        x += 1
        time.sleep(1)
    time.sleep(30)
    driver.close()
