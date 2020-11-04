import pyttsx3                        # this module use for convert text to speech
import speech_recognition as sr       # this module use for voice recognation 
import datetime                       # this module use to know current time
import wikipedia                      # this module use to search wikipedia 
import os                             # this module use to interact with your operating system
import webbrowser                     # this module use to web browsing
import smtplib                        # this module use to send email
from time import ctime                # acces current time 
import time                           # access current time and date according to the time zone

# this variable stored user/master name
MASTER = ' MR NIL'                   
current_time = ctime() #call real time clock and date

# this is text voice function 
def speek(text):
    mytext = pyttsx3.init()
    voices = mytext.getProperty('voices')
    # for voice in voices:
    #     voice =  mytext.setProperty('voice', voice[0].id)                        #this line for female voice
    newvoicerate = 180      #(control speed of your voice)
    mytext.setProperty('rate', newvoicerate)
    mytext.say(text)
    mytext.runAndWait()

#this function will active - initial time of your  program
def wiseMe():
    hour = datetime.datetime.now().hour
    
    if hour >= 0 and hour <= 12:         #this line indicate range of 12am to 12 pm (time)
        speek("good morning sir")
    elif hour >= 12 and hour <= 15:
        speek('good afternoon sir')
    elif hour >= 15 and hour <= 20:
        speek('good evening sir')
    else:
        speek("good night sir ")
    speek(F"i am jervis..{MASTER} how may i help you..")

#this function will active when user wanted to exit jervis(you may skipe this function and added  comments in wiseMEe function )
def wise():
    temp = ''
    hour = datetime.datetime.now().hour
    
    if hour >= 0 and hour <= 12:
        speek("ok sir have a good day")
    elif hour >= 12 and hour <= 15:
        speek('ok sir  good afternoon')
    elif hour >= 15 and hour <= 20:
        speek('ok sir  good evening')
    else:
        speek("ok sir good night ")
    return temp

# this is voice input function through microphone   
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

        
#this is just a simple welcom comment 
speek('initializing jervis')  
wiseMe()



# this is the main part of this program//in this function we define actual tasks which are performend by your system
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
        speek('ok sir i will opening  youtube for you')
        

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

    elif "music" in query.lower():
        url = 'https://www.youtube.com/watch?v=J61mtatKT1I&list=RDJ61mtatKT1I&start_ra'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        speek('ok sir')
        webbrowser.get(chrome_path).open(url)
    
    elif "play youtube" in query.lower():
        speek("what do you want to search for ?")
        search = takeCommend("what do you want to search for ?")
        url = 'https://youtube.com/search?q=' + search
        webbrowser.get().open(url)
        speek("okk sir i am finding for you")
        print(search)

    elif "movies file" in query.lower():
        code_path = 'E:\movie'
        speek("please wait sir")
        os.startfile(code_path)
        speek("here is your movies sir")

    # when user pass comment 'sleep' loop will be brake and shutdown the program 
    elif "sleep" in query.lower():
        speek(wise())
        exit()     



    elif 'email' or 'gmail' in query.lower():
        url = 'https://mail.google.com/mail/u/0/#inbox'
        speek('please wait sir i am opening your inbox')
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        speek('here your emails sir ')
        webbrowser.get(chrome_path).open(url)
        


    


#system will wait for your next command for i second  
time.sleep(1)
while 1:
    query = takeCommend()
    respond(query)
