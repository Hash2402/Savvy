import sys
import pyttsx3
import speech_recognition as s
import datetime as dt
import os 
import sys
import requests
import pywhatkit as pk
import webbrowser
from requests import get
from pynput.keyboard import Controller as ck
import wikipedia

#import dependencies 
import user

from user import *
time_n=dt.datetime.now()
time_n=str(time_n)
time_now=(dt.datetime.now().strftime("%H-%M"))
li=(time_now.split("-"))
a=int(li[0])
b=int(int(li[1])+2)
print(time_now)
print(Users)

Users={"Name":"Password"}

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice', voices[1].id) 

def voice_check():
    for voice in voices:
        print(voice, voice.id)
        engine.setProperty('voice', voice.id)
        engine.say("Hi its me ")
        engine.runAndWait()
        engine.stop()


#speak
def sav(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#get input
def v_input():
    rec=s.Recognizer()
    with s.Microphone() as source:
        s1="Waiting for your Command"
        print(s1)
        rec.pause_threshold =1
        audio=rec.listen(source,phrase_time_limit=5)
    try:
        print("Understanding!!")
        comand=rec.recognize_google(audio,language="en-in")
        print("You said :- ",comand)
    except Exception as e :
        sav("Didn't get that one ")
        
        return v_input()
    return comand
    
def type_on():
      #content to be written
    time_now=int(dt.now().strftime("%H-%M"))

def new_us():
#from user import *
    sav("Creating new user")

    sav("What should i call you")
    user_name=v_input()
    user_str="Hey"+user_name+"Please set a password"
    sav(user_str)
    passwd=v_input()

    Users[user_name]=passwd
    return "User created"
    
    

    
    
if __name__=="__main__":
    sav("Hi \nI am Savvy")
    i=0
    while True:
        
        
            
        task=v_input().lower()  
        
        if "open notepad"in task:
            not_path="C:\\Windows\\notepad.exe"
            if os.path.exists(not_path):
                os.startfile(not_path)
            else:
                sav("Specify Drive")
                Drive=v_input()
                new_path=Drive+":\\Windows\\notepad.exe"
                print(new_path)
                os.startfile(new_path)
        elif "open command prompt" in task:
            os.system("start cmd")
            
        elif 'wikipedia' in task:
            sav("Searching wikipedia...")
            task = task.replace("wikipedia","")
            result = wikipedia.summary(task, sentences = 2)
            sav(result)
            
        elif "ip" in task :
            res=get('https://api.ipify.org').text
            sav(res)

        elif "send a message" in task:
            #print("Hl")
            sav("What is the message ")
            msg=v_input()
            pk.sendwhatmsg("+919322095558",msg,a,b)
        elif "search" and "file" in task :
            sav("What is the File Name")
            msg=v_input

        elif "time" in task:
            sav(time_now)
            print(time_n)
        
        
        elif "open  ms word " in task :
            not_path="C:\\Windows\\word.exe"
            if os.path.exists(not_path):
                os.startfile(not_path)
            else:
                sav("Specify Drive")
                Drive=v_input()
                new_path=Drive+":\\Windows\\Word.exe"
                print(new_path)
                os.startfile(new_path)

        elif "open powerpoint" in task :
            not_path="C:\\Windows\\PowerPoint.exe"
            if os.path.exists(not_path):
                os.startfile(not_path)
            else:
                sav("Specify Drive")
                Drive=v_input()
                new_path=Drive+":\\Windows\\PowerPoint.exe"
                print(new_path)
                os.startfile(new_path)
                
        elif 'open google' in task:
            webbrowser.open("google.com") 

        elif 'open youtube' in task:
            webbrowser.open("youtube.com")
            
        elif 'open stack overflow' in task:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in task:
            webbrowser.open("github.com")

        elif 'open adcet website' in task:
            webbrowser.open("https://adcet.ac.in/ADCET/")
            
        elif "Open camera" in task :
            not_path="C:\\Windows\\.exe"
            if os.path.exists(not_path):
                os.startfile(not_path)
            else:
                sav("Specify Drive")
                Drive=v_input()
                new_path=Drive+":\\Windows\\PowerPoint.exe"
                print(new_path)
                os.startfile(new_path)

        elif "exit"  in task:
            sys.exit()
        
        
        
