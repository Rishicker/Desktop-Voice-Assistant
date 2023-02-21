import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")
    except:   
        return "None"
    return query.lower()

def TaskExe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        Speak("Good Morning")
    elif hour>12 and hour<18:
        Speak("Good afternoon")
    else:
        Speak("Good evening")
    c_time = datetime.datetime.now().strftime("%I:%M %p")
    Speak(f"Currently it is {c_time}")
    Speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

    GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis","ok jarvis", "are you there"]
    GREETINGS_RES = ["always there for you sir", "i am ready sir","your wish my command", "how can i help you sir?", "i am online and ready sir"]

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("C:\\Users\\shukl\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'telegram' in query:
            os.startfile("C:\\Users\\shukl\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')
        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')
        elif 'discord' in query:
            os.startfile("C:\\Users\\shukl\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord")
        Speak("Your Command Has Been Completed Sir!")

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")
        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")
        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")
        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")
        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")
        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'discord' in query:
            os.system("TASKKILL /F /im discord.exe")
        Speak("Your Command Has Been Succesfully Completed!")

    def Temp():
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} ")
        Speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()
        if 'yes' in next:
            Speak("Tell Me The Name Of tHE Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature} celcius")
        else:
            Speak("no problem sir")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('k')
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('l')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'film mode' in comm:
            keyboard.press('t')
        Speak("Done Sir")

    def Tran():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            Speak("Tell Me The Line!")
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)
            print("Recognizing.....")
            hiquery = command.recognize_google(audio,language='hi')
            print(f"You Said : {hiquery}")
        line = hiquery
        translator = Translator()
        result = translator.translate( line , dest = 'en', src = 'hi')
        Text = result.text
        Speak(Text)

    def ChromeAuto():
        Speak("Chrome Automation started!")
        command = takecommand()
        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

    def screenshot():
        Speak("Ok Boss , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\shukl\\Pictures\\Video Projects\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("")
        Speak("Here Is Your ScreenShot")

    def Music():
        Speak("Tell Me The Name oF The Song!")
        musicName = takecommand()
        pywhatkit.playonyt(musicName)
        Speak("Your Song Has Been Started! , Enjoy Sir!")

    while True:
        query = takecommand()
        if 'hello' in query:
            Speak("Hello Sir , I Am Jarvis .")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")
        elif query in GREETINGS:
                Speak(random.choice(GREETINGS_RES))
        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")
        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            Speak("Just Say Wake Up Jarvis!")
            break
        elif 'youtube search' in query:
            Speak("OK Sir , This Is What I found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")
        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")
        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,1)
            Speak(f"According To Wikipedia : {wiki}")
        elif 'screenshot' in query:
            screenshot()
        elif 'open facebook' in query:
            OpenApps()
        elif 'open instagram' in query:
            OpenApps()
        elif 'open maps' in query:
            OpenApps()
        elif 'open code' in query:
            OpenApps()
        elif 'open youtube' in query:
            OpenApps()
        elif 'open telegram' in query:
            OpenApps()
        elif 'open chrome' in query:
            OpenApps()
        elif 'open discord' in query:
            OpenApps()
        elif 'close chrome' in query:
            CloseAPPS()
        elif 'close discord' in query:
            CloseAPPS()
        elif 'music' in query:
            Music()
        elif 'close telegram' in query:
            CloseAPPS()
        elif 'close instagram' in query:
            CloseAPPS()
        elif 'close facebook' in query:
            CloseAPPS()
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')
        elif 'youtube tool' in query:
            YoutubeAuto()
        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')
        elif 'chrome automation' in query:
            ChromeAuto()
        elif 'tell me a joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")
        elif 'my location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/')
        elif 'alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time : ")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('C:\\Users\\shukl\\Music\\Alarm.mp3')
                    Speak("Alarm Closed!")
                elif now>time:
                    break
        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            Speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste YouTube Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)
            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)
            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)
            root.mainloop()
            Speak("Video Downloaded")
        elif 'translator' in query:
            Tran()
        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That" + remeber.read())
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query,2)
                Speak(result)
            except:
                Speak("No Speakable Data Available!")
        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
        elif 'temperature' in query:
            Temp()
        elif "make a note" in query or "write this down" in query or "remember this" in query:
            import note
            Speak("What would you like me to write down?")
            note_text = takecommand()
            note.note(note_text)
            Speak("I've made a note of that")
        elif "system status" in query:
            import system_stats as ss
            sys_info = ss.system_stats()
            print(sys_info)
            Speak(sys_info)

TaskExe()