import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui
import mouse
import wikipedia
import webbrowser
from selenium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import youtube_dl

url = input('What is the url of the spotfiy playlist?')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=r'C:\Users\jeetd\downloads\chromedriver')
wait = WebDriverWait(driver, 25)
driver.maximize_window()
driver.get(url)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[1]/div[5]/div/span[2]')))
songnum = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[1]/div[5]/div/span[2]')
songnum = songnum.text
print(songnum)
message5a = songnum.find("songs")
message5a = int(message5a)
message5a = message5a * -1
message5a =- message5a
songnum = songnum[0:message5a]
print(message5a)
print(songnum)
songnum = int(songnum)
print(songnum)
anumber = '1'
song = []
artist = []
album = []
image = []
songnamepath = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[' + anumber + ']/div/div[2]/div/div'
artinamepath = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[' + anumber + ']/div/div[2]/div/span/a'
albunamepath = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[' + anumber + ']/div/div[3]/span/a'
imagnamepath = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[' + anumber + ']/div/div[2]/img'
numbering = 1
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div')))
time.sleep(0.5)
thingaaa = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div').click()
def getstuff():
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,songnamepath)))
    songele = driver.find_element(By.XPATH, songnamepath)
    artistele = driver.find_element(By.XPATH, artinamepath)
    albumele = driver.find_element(By.XPATH, albunamepath)
    #imagele = driver.find_element(By.XPATH, imagnamepath)
    song.append(songele.text)
    artist.append(artistele.text)
    album.append(albumele.text)
    #image.append(imagele.text)
while numbering < 54:
    getstuff()
    anumber = int(anumber)
    anumber = anumber + 1
    anumber  = str(anumber)
    songnamepath = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[' + anumber + ']/div/div[2]/div/div'
    artinamepath = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[' + anumber + ']/div/div[2]/div/span/a'
    albunamepath = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[' + anumber + ']/div/div[3]/span/a'
    imagnamepath = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[2]/div[3]/div/div[2]/div[2]/div[' + anumber + ']/div/div[2]/img'
    print(numbering)
    print(anumber)
    time.sleep(0.5)
    pyautogui.press('down')
    numbering = numbering + 1
    print(len(song))
    print(song)
    print(artist)
    print(album)
    #works :)
driver.close();
numbering = 1
array = 0
url = []
while numbering < 54:
    youtub2 = 'https://www.youtube.com/results?search_query=' + song[array] + artist[array] + 'lyrics'
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path=r'C:\Users\jeetd\downloads\chromedriver')
    wait = WebDriverWait(driver, 25)
    driver.maximize_window()

    driver.get(youtub2)
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "video-title"))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[2]/a')))
    url.append(driver.current_url)
    driver.close()
    print(url)
    array = array + 1
    numbering = numbering + 1
def download(video_url, songname):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info[songname]}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
numbering = 0
while numbering < 54:
    download(url[numbering], song[numbering])
    numbering = numbering + 1

#THIS IS BULLSHIT I HATE SPOTIFY DEVS THEY CAN ALL GO DIE IN A DITCH ALONE
#im calmer now, but i still hate them
#just going to cap songs at 53 for now- this is kinda annoying tbh
