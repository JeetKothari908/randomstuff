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
# Initialize WebDriver
driver = webdriver.Chrome()
#driver = webdriver.Chrome(r'C:\Users\jeetd\downloads\chromedriver')
wait = WebDriverWait(driver, 25)
driver.get("https://www.reddit.com/r/dogs")  # Replace "subreddit" with the desired subreddit

# Counter for the number of iterations
iteration_count = 0
max_iterations = 1000  # Specify the number of iterations

# Main loop
while iteration_count < max_iterations:
    # Find and click on a specific post
    count = iteration_count + 1
    post_xpath = "/html/body/shreddit-app/div/div[2]/div[2]/shreddit-post[" + str(count) + "]"  # Adjust the post XPath as needed
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,-500)", "")

    time.sleep(1)
    post_element = driver.find_element("xpath",post_xpath)
    post_element.click()

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    # Use keyboard shortcuts (Ctrl + P and Enter) to print the post
    time.sleep(4)  # Give time for the page to fully load before sending keys
    title = driver.find_element("xpath",'/html/body/shreddit-app/div/div[2]/shreddit-post/div[3]')
    title = title.text
    title = title.replace(" ", "_")


    def remove_special_characters(input_string):
        # Define a regular expression pattern to match special characters
        pattern = r'[^\w\s]'

        # Use the re.sub() function to replace special characters with an empty string
        cleaned_string = re.sub(pattern, '', input_string)

        return cleaned_string
    title = remove_special_characters(title)
    pyautogui.hotkey('ctrl', 'p')  # Open print dialog
    time.sleep(3)  # Wait for print dialog to open
    pyautogui.press('enter')  # Press the 'Enter' key to printS
    time.sleep(3)  # Wait for print dialog to open
    pyautogui.click(x=243, y=500)
    pyautogui.typewrite(title)
    pyautogui.press('enter')  # Press the 'Enter' key to print
    # Close the tab and switch back to the original tab
    time.sleep(3)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    pyautogui.scroll(-1000)  # scroll down 10 "clicks"

    # Increment the iteration count
    iteration_count += 1

# Close the browser window
driver.quit()
