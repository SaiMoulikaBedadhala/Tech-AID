import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import speedtest
import PyPDF2
from requests import get

engine = pyttsx3.init()

#To spell out 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! MASTER")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! MASTER")   

    else:
        speak("Good Evening! MASTER")  

    speak("You are talking to TechAid!!!! How may i help you??")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"MASTER said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def pdf_reader():
    book = open('VA.pdf',"rb")
    pdfReader = PyPDF2.PdfReader(book)

    page = pdfReader.pages[0]
    text = page.extract_text()
    speak(text)
    book.close()

wishMe()


d = '/Applications'
apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))

while True:
    q=takeCommand()
    #to open an app
    if 'open' in q:
        q = q[5: ]
        q=q.replace(" ","")
        q=q[0].upper() + q[1:]
        #print(q)
        #if app is present in System
        if q in apps:
            os.system(('open ' +d+'/{}.app').format(q))
        #Searches from browser
        else:
            webbrowser.open("https://www.{}.com".format(q))

    #to close any app
    if 'close' in q:
        q = q[6: ]
        q=q.replace(" ","")
        print(q)
        os.system(('pkill {}').format(q))
    
    if 'convergence 2023' in q:
        webbrowser.open("https://convergence2k23.netlify.app/?fbclid=PAAabqazhm6azrfk1eJRm_Gjp1QTCmeRafEbCytLUiRzz-qmpiDDXxXeEeJdU")

    if 'time' in q:
        hr = int(datetime.datetime.now().hour)
        min = int(datetime.datetime.now().minute)
        if not (hr >= 0 and hr < 12):
            hr = hr - 12
        print("The time is {} hours and {} minutes".format(hr, min))
        speak("The time is {} hours and {} minutes".format(hr, min))

    if 'Wikipedia' in q:
        q = q.lower()
        speak("Searching on wikipedia")
        q = q.replace("wikipedia", "")
        results = wikipedia.summary(q, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    if 'read PDF' in q:
        pdf_reader()
    
    if 'speed' in q:
        wifi = speedtest.Speedtest()
        print("Download Speed:",(wifi.download()))
        print("upload speed",(wifi.upload()))

    if "ip address" in q:
        ip = get('https://api.ipify.org').text
        speak(f"Your IP address is {ip}")
    
    if 'bye' in q:
        speak("Hope I helped You Meet you soon")
        break




