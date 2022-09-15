import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import os
import subprocess
import bs4
from bs4 import BeautifulSoup as BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import requests
import time
from playsound import playsound
import winsound
from GoogleNews import GoogleNews
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#text to speech
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#for wishing
def wish():
    hour=int(datetime.datetime.now().hour)
    pos=str(hour)
    speak("hello sir nice to see you again")
    if hour >=4 and hour<12:
        speak("good morning sir ")
        speak("its" +pos+ " in the morning")
    elif hour >= 12 and hour < 16:
        speak("good afternoon sir")
        engine.say("its" +pos+ " in the afternoon")
    elif hour >=16 and hour<20:
        speak("good evening sir ")
        speak("its" +pos+ " in the evening")
    else:
        speak("night sir")

#             converting audio into text ot take command
def takecom():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        speak("command sir")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        speak("wait sir ")
        text=r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:
        speak("speak again sir")
        print("network connection  error")
        return "none"
    return text
#               main functions of shryder
#os.startfile("E:\\second_4.4.rmskin")
time.sleep(8)
print("Initializing Shryder")
speak("initializing shryder")
time.sleep(1)
speak("connecting to server")
time.sleep(1)
speak("system going online")
frequency =3000
duration=400
winsound.Beep(frequency,duration)
playsound('C:\\Users\\user\\Downloads\\sound effects\\shryder open.mp3')
wish()
while True:
    query=takecom().lower()
#      Browsers Browsers Browsers Browsers Browsers browsers
    #1
    if "wikipedia" in query.lower():
        speak("searching details sir...... please wait")
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)
    #2
    elif "open youtube" in query:
        webbrowser.open("www.youtube.com")
        speak("opening youtube")
    #3
    elif "open google" in query:
        webbrowser.open("www.google.co.in")
        speak("opening google")
    #4
    elif "open classroom" in query:
        webbrowser.open("www.classroom.google.com/h")
        speak("opening classrroom")
    #5
    elif "open spotify" in query:
        webbrowser.open("https://open.spotify.com/user/spotify")
        speak("opening music on spotify")
    #6
    elif "temperature" in query:
        search = "weather in lucknow"
        url=f"https://www.google.com/search?&q={search}"
        r=requests.get(url)
        s=BeautifulSoup(r.text,"html.parser")
        update = s.find("div",class_="BNeawe").text
        speak("its"+update+"celsius in lucknow")
#                   system operation
    #7
    elif "open whatsapp" in query:
        subprocess.call('C:\\Users\\user\\Downloads\\WhatsAppSetup.exe')
        speak("opening whatsapp")
    #8
    elif "news" in query:
        g=GoogleNews('en')
        g.search('India')
        y=g.gettext()
        speak(y)

    #9
    elif "open calculator" in query:
        subprocess.call('calc.exe')
        speak("opening calculater")
# introduction and manual command manual command manual command manual command
    elif "hello" in query:
        speak("yes sir i am Listening")

    elif 'goodbye' in query or "go offline" in query:
        speak("goodbye sir")
        speak("disconnecting to server")
        speak("going offline")
        exit()
    #
    elif "shutdown" in query:
        hour=int(datetime.datetime.now().hour)
        pos=str(hour)
        if hour >=20 and hour<24:
            speak("its"+pos+" in the night" )
            speak("perhaps you are going for sleep sir")
            speak("have a sweet dream master see you tommorow ")
        #speak('connecting to command prompt')
        speak('closing all Program')
        speak('disconnecting to servers')
        speak("shutting down system")
        os.system("shutdown /s /t 1")
    #
    elif "awesome" in query:
        speak('ohhh thank you sir for making me awesome')
        time.sleep(1)
        speak("offcourse sir")
    #
    elif "systeminfo" in query:
        os.system('cmd /k " systeminfo"')

    elif "close Browser" in query:
        os.system("TASKKILL /F /IM ".exe)

    elif "close browsers" in query or "close all browser" in query:
        path="C:\Program Files (x86)\chromedriver.exe"
        driver=webdriver.Chrome(path)
        driver.quit()
# advance#advance#advance#advance#advance#advance#advance#advance#advance


# shryder can u play a video
    elif "video" in query:
        speak("yes sir sure ")
        time.sleep(2)
        speak("so what will you watch sir ")
        z=takecom()
        path="C:\Program Files (x86)\chromedriver.exe"
        driver=webdriver.Chrome(path)
        driver.maximize_window()
        speak("opening youtube")
        driver.get("https://www.youtube.com/")
        driver.find_element_by_name('search_query').send_keys(z)
        driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()

    elif "play music" in query or "play some music" in query:
        path="C:\Program Files (x86)\chromedriver.exe"
        driver=webdriver.Chrome(path)
        driver.get("https://gaana.com/")
        driver.minimize_window()
        speak("playing music hope you will enjoy sir")

        driver.find_element_by_xpath('//*[@id="home_featuredplaylists"]/li[1]/div/div[1]/a[2]/img').click()

    elif "question" in query:
        speak("sure sir")
        speak("connecting to browser")
        path="C:\Program Files (x86)\chromedriver.exe"
        driver=webdriver.Chrome(path)
        driver.maximize_window()
        time.sleep(2)
        speak("ask your question")
        z=takecom()
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(z)
        driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()

    elif "weather" in query:
        speak("which city forecast you want to know sir")
        city=takecom()
        print(city)
        path="C:\Program Files (x86)\chromedriver.exe"
        driver=webdriver.Chrome(path)
        driver.minimize_window()
        driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
        s=driver.find_elements_by_class_name('b-forecast__table-description-content')[0].text
        speak(s)

    elif "thank you" in query:
        speak(" you're welcome roshni")
        time.sleep(10)
