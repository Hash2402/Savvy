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
from ecapture import ecapture as ec
from pynput.keyboard import Controller as ck
import wikipedia
import shutil
import smtplib
import winshell

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
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('rushikeshkadam2420@gmail.com', 'rqwtlanrqclzyaza')
    server.sendmail('rushikeshkadam2420@gmail.com', to, content)
    server.close()

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
                
        elif "close notepad" in task:
            os.system("taskkill /f /im notepad.exe")
        
        elif "open command prompt" in task:
            os.system("start cmd")
            
        elif "close command prompt" in task:
            os.system("taskkill /f /im cmd.exe")
            
        elif "start typing" in task:
            query = ""
            kb_keys = {"tab space":'\t',"exclamation":'!',"double quote":'"',"hash":'#',"dollar":'$',"percent":'%',"ampersand":'&',"single quote":"'","open parenthesis": '(',
                       "close parenthesis": ')', "asterisk": '*',"plus":'+', "comma": ',', "hyphen":"-","minus":"-","full stop":".","dot":".","forward slash" :'/',"slash":"/",
                       "back slash": "\\","backward slash":"\\","colon":":","semi colon":";","less than":"<","equal to": '=',"greater than": '>',"question mark": '?',
                        "open square bracket": '[',"close square bracket":  ']',"caret": '^',"underscore": '_', "backtick":'`',"open curly bracket": '{',
                         "bar": '|',"close curly bracket": '}', "tilde":'~' }

            kb_num = {"zero":'0',"one": '1',"two": '2',"three": '3',"four": '4',"five": '5',"six": '6',"seven": '7',"eight": '8', "nine": '9'}

            sav("what would you like to write?")

            while "stop typing" not in query.lower():
                query = v_input()
                if "stop typing" in query :
                    break
                
                elif "select all" in query:
                    pyautogui.hotkey('ctrl', 'a')

                elif "new line" in query or "press enter" in query:
                    pyautogui.press('enter')

                elif "backspace" in query:
                    pyautogui.press('backspace')

                elif "clear line" in query:
                    with pyautogui.hold('shift'):
                        pyautogui.press('home')
                    pyautogui.press('backspace')

                elif "clear word" in query:
                    pyautogui.hotkey('ctrl', 'shift', 'left')
                    pyautogui.press('backspace')

                elif "undo" in query:
                    pyautogui.hotkey('ctrl', 'z')
                    
                elif "redo"in query:
                    pyautogui.hotkey('ctrl', 'y')

                else:
                    w_list = query.split(" ")
                    l_index = len(w_list)
                    index = 0
                    while index<l_index:
                        print(index)
                        if w_list[index] == "num" or w_list[index] == "nam" or w_list[index] == "number":
                            if w_list[index+1] in kb_num.values():
                                w_list[index] = ""
                            elif w_list[index+1] in kb_num.keys():
                                w_list[index] = ""
                                w_list[index+1] = kb_num[w_list[index+1]]

                        if w_list[index] == "symbol":                    
                            if w_list[index+1] in kb_keys.keys():
                                w_list[index+1] = kb_keys[w_list[index+1]]
                                w_list[index] = ""
                            elif index+2 <= len(w_list)-1 and w_list[index+1]+" "+w_list[index+2] in kb_keys.keys():
                                    w_list[index+1] = kb_keys[w_list[index+1]+" "+w_list[index+2]]
                                    w_list[index] = ""
                                    l_index -=1
                                    w_list.pop(index+2)
                            elif index+3 <= len(w_list)-1 and w_list[index+1]+" "+w_list[index+2]+" "+w_list[index+3] in kb_keys.keys():
                                    w_list[index+1] = kb_keys[w_list[index+1]+" "+w_list[index+2]+" "+w_list[index+3]]
                                    w_list[index] = ""
                                    l_index -=2
                                    w_list.pop(index+2)                                    
                                    w_list.pop(index+2)
                        index +=1

                    query1 = " ".join(w_list)

                    pyautogui.typewrite(" "+query1)
            
        elif 'wikipedia' in task:
            sav("Searching wikipedia...")
            task = task.replace("wikipedia","")
            result = wikipedia.summary(task, sentences = 2)
            sav(result)
            
        elif "press enter" in task:
            pyautogui.press('enter')
            
        elif "switch window" in task or "which window" in task:
            pyautogui.hotkey('alt', 'tab')
            
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
                
        elif "close ms word" in task:
            os.system("taskkill /f /im word.exe")

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
                
        elif "close powerpoint" in task:
            os.system("taskkill /f /im PowerPoint.exe")
                
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
            
        elif 'open code' in task:
            codepath = "C:\\Users\\SHUBHAM GAIKWAD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif "close code" in task:
            os.system("taskkill /f /im Code.exe")

        elif 'open telegram' in task:
            codepath = "C:\\Users\\SHUBHAM GAIKWAD\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(codepath)   
            
        elif "close telegram" in task:
            os.system("taskkill /f /im Telegram.exe")
            
            
        elif 'how are you' in task:
            sav("I am fine and ready to work for you.")

        elif 'what is your name' in task:
            sav("it's savvy your virtual assistant")

        elif 'tell me todays schedule' in task:
            sav("check out todo list for schedule")

        elif 'what can you do for me' in task:
            sav("I can do all tasks a assistant can do like playing music, opening apps, etc.")
            
        elif 'who is' in task:
            person = task.replace('who is', '')
            info = wikipedia.summary(person,1)
            print(info)
            sav(info)

        elif 'what is' in task:
            know = task.replace('what is', '')
            info = wikipedia.summary(know,1)
            print(info)
            sav(info)
            
            
        elif 'how to' in task:
            know = task.replace('how to', '')
            info = wikipedia.summary(know,2)
            print(info)
            sav(info)
            
            
            
        elif "delete folder" in task:
            #path input using voice .future
            path =input()
            try:
                shutil.rmtree(path)
            except FileNotFoundError:
                print("File was not found: %s" % path)

            except PermissionError:
                print("You don't have permission to delete this type of file")    
            except OSError:
                print("Your OS does not allow to delete this type of file")
            else:
                print(path+"was deleted")
            
        elif 'play music' in task:
            music_dir = 'E:\\audio'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
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
                
        #To delete all files from recycle bin          
        elif "delete recycle bin" in task:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                sav("Recycle Bin Emptied")
        
        #To find any location on map       
        elif 'show location on map' in task:
              sav('Which location you want to see?')
              location=v_input()
              url = 'https://google.nl/maps/place/' + location + '/&amp;'
              webbrowser.get().open(url)
              sav('Here is location' + location)
        
        #To take a photo and save it directly
        elif "camera" in task or "take a photo" in task:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
            
         #To create a file and write text in it directly and save it   
        elif "write a note" in task:
            sav("What should i write, sir")
            file =open("myfile.txt", "w")
            note =v_input()
            file.write(note)
            
        #To display files and text written in that files   
        elif "display notes" in task:
            sav("Showing Notes")
            file = open("myfile.txt", 'r')
            print(file.read())
            sav(file.read(6))
         
        #To send a mail directly to anyone
        elif 'send mail' in task:
            try:
                sav("What should I say?")
                content = v_input()
                sav("Whom i send?")
                to = v_input()+"@gmail.com"
                to2= to.replace(" ","")
                sendEmail(to2, content)
                sav("Email has been sent !")
            except Exception as e:
                print(e)
                sav("I am not able to send this email")
        
        #To open shopping website like amazon directly        
        elif 'open amazon' in task:
                webbrowser.open("amazon.in")

        elif "exit"  in task:
            sys.exit()
        
        
        
