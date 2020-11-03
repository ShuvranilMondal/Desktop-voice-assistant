import pyttsx3                        # this moudle use for covert text to speech
import speech_recognition as sr       # this moudel use for voice recognation 
import datetime                       # this moudel use to know current time
import wikipedia                      # this moudel use to search wikipedia 
import os
import webbrowser
import smtplib
from time import ctime
import time


MASTER = ' MR NIL'
current_time = ctime()


def speek(text):
    mytext = pyttsx3.init()
    voices = mytext.getProperty('voices')
    # for voice in voices:
    #     voice =  mytext.setProperty('voice', voice[0].id)   #this line for female voice
    newvoicerate = 180
    mytext.setProperty('rate', newvoicerate)
    mytext.say(text)
    mytext.runAndWait()


def wiseMe():
    hour = datetime.datetime.now().hour
    
    if hour >= 0 and hour <= 12:
        speek("good morning sir")
    elif hour >= 12 and hour <= 18:
        speek('good afternoon sir')
    elif hour >= 18 and hour <= 20:
        speek('good evening sir')
    else:
        speek("good night sir ")
    speek(F"i am jervis..{MASTER} how may i help you..")

def wise():
    temp = ''
    hour = datetime.datetime.now().hour
    
    if hour >= 0 and hour <= 12:
        speek("ok sir have a good day")
    elif hour >= 12 and hour <= 18:
        speek('ok sir have a good afternoon')
    elif hour >= 18 and hour <= 20:
        speek('ok sir have a good evening')
    else:
        speek("ok sir good night ")
    return temp
    
def takeCommend(ask = False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            print(ask)
        print('Listening...')
        audio = r.listen(source)
        query = ""
        
        try :
            print('Recognizing....')
            query = r.recognize_google(audio, language= "en-in")
            print(f"you said: {query}\n")

        except Exception as e:
            print('sorry sir say that again')
            query = takeCommend()
        return query

        

speek('initializing jervis')
wiseMe()




def respond(query):

    if  'wikipedia' in query.lower():
        speek('ok sir i am searching for you..')
            # query = query.replace('wikipdea', '')
        results = wikipedia.summary(query, sentences =1)
        print(results)
        speek(results)
        

    elif 'open youtube' in query.lower():
            # webbrowser.open("youtube.com")
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speek('ok sir')
        

    elif 'facebook' in query.lower():
            # webbrowser.open("youtube.com")
        url = 'facebook.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        speek('ok sir')
        webbrowser.get(chrome_path).open(url)
        
            
    elif 'coldplay' in query.lower():
            # webbrowser.open("youtube.com")
        url = 'https://www.youtube.com/watch?v=dvgZkm1xWPE'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        speek('ok sir')
        webbrowser.get(chrome_path).open(url)
        
        
    elif "time" in query.lower():
        speek(current_time)

    elif 'search' in query.lower():
        speek("what do you want to search for ?")
        search = takeCommend("what do you want to search for ?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speek('ok sir')
        print(search)
    elif "sleep" in query.lower():
        speek(wise())
        exit()



time.sleep(1)
while 1:
    query = takeCommend()
    respond(query)