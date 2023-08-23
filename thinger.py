# Licensed to the Software Freedom Conservancy (SFC) under one
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
import keyboard
# Initialize WebDriver
while True:
    pyautogui.scroll(-5000)
    time.sleep(1)
    if keyboard.is_pressed("a"):
        print("You pressed 'a'.")
        break
    # scroll down 10 "clicks"

