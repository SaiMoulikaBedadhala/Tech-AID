import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import PyPDF2
from requests import get
import pyautogui
import time
import numpy

engine = pyttsx3.init()
# # voice= engine.getProperty('voice') #getting details of current voice
# # print(voice)
# # engine.setProperty('voice', voice[19])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# # speak("Moulika is good girl")

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")   

#     else:
#         speak("Good Evening!")  

#     speak("I am Akash Sir. Please tell me how may I help you")       


# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query

# def virtualAssistant():
#     # wishMe()
#     d = '/Applications'
#     apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
#     # print("Terminal" in apps)
#     while True:
#         q=takeCommand()
#         # speak(q)
#         if 'open' in q:
#             q = q[5: ]
#             q=q.replace(" ","")
#             q=q[0].upper() + q[1:]
#             print(q)
#             if q in apps:
#                 os.system(('open ' +d+'/{}.app').format(q))
#             else:
#                 webbrowser.open("https://www.{}.com".format(q))
#         if 'close' in q:
#             q = q[6: ]
#             q=q.replace(" ","")
#             print(q)
#             os.system(('pkill {}').format(q))



#     #     if 'open youtube' in q:
#     #         webbrowser.open("https://www.youtube.com/")
#     #     if 'open github' in q:
#     #         webbrowser.open("https://github.com/")
#     #     if 'open linkedin' in q:
#     #         webbrowser.open("https://www.linkedin.com/feed/")
#     #     if 'open hackerank' in q:
#     #         webbrowser.open("https://www.hackerrank.com/auth/signup")
#         if 'convergence 2023' in q:
#             webbrowser.open("https://convergence2k23.netlify.app/?fbclid=PAAabqazhm6azrfk1eJRm_Gjp1QTCmeRafEbCytLUiRzz-qmpiDDXxXeEeJdU")
#         if 'time' in q:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             # strTime = datetime.datetime.now().strftime("%H")    
#             print("The time is {}".format(strTime))    
#             speak("The time is {} hours".format(strTime))
#             # speak(f"Sir, the time is {strTime}")
#         if 'wikipedia' in q:
#             speak("Searching on wikipedia")
#             q = q.replace("wikipedia", "")
#             results = wikipedia.summary(q, sentences = 2)
#             speak("According to wikipedia")
#             print(results)
#             speak(results)
#         if 'bye' in q:
#             speak("Bye Akash sir")
#             break
#         # print(q)

# # os.system("open /Applications/WhatsApp.app")

# # os.system("pkill WhatsApp")

# # output = os.popen("find /Applications/Netflix.app").read()
# # output = os.popen("find /Applications/WhatsApp.app").read()

# # if not len(output) == 0:
# #     # print(output)
# # else:
# #     print("Empty string")

# # d = '/Applications'
# # apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
# # # print(apps)
# # q = 'open whatsapp'
# # q = q[5:]
# # os.system(('open ' +d+'/{}.app').format(q))

# # q = takeCommand().lower()
# # if 'open' in q:
#     # q = q[5: ]
#     # print(q)
# # virtualAssistant()
# h = int(datetime.datetime.now().hour)
# m = int(datetime.datetime.now().minute)
# print(h, m)

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
# engine.say('Hello World')
# engine.runAndWait()

# def pdf_reader():
#     book = open('VA.pdf',"rb")
#     pdfReader = PyPDF2.PdfReader(book)
#     # pages = pdfReader.numPages
#     # speak(f"Total number of pages in this book {pages}")
#     # speak("Sir please enter the page number i have to read")
#     # pg = int(input("Please enter the page number:"))
    
#     page = pdfReader.pages[0]
#     text = page.extract_text()
#     speak(text)
#     book.close()



# pdf_reader()
# if "ip address" in query:
# ip = get('https://api.ipify.org').text
# speak(f"Your IP address is {ip}")

# if "where i am" in q or "where are we" in q:
# speak("wait sir let me check")
# try:
#     ipAdd = get('https://api.ipify.org').text
#     print(ipAdd)
#     url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
#     geo_requests = get(url)
#     geo_data = geo_requests.json()
#     # print(geo_data)
#     city = geo_data['city']
#     state = geo_data['state']
#     country = geo_data['country']
#     speak(f"Sir im not sure, but we are in {city} city {state} state of {country} country")
# except Exception as e:
#     speak("Sorry Sir, Due to network issue i am not able to find where we are.")
#     pass

# os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")


# import subprocess
# cmd = "gnome-terminal --working-directory=/home/USERNAME/Documents/Scripts/"
# subprocess.Popen(cmd, shell=True)

# elif "take screenshot" in query:


# speak("Sir, Please tell me the name for the screenshot file")
# name = takeCommand().lower()
# speak("Taking Screenshot...!")
# time.sleep(2)
img = pyautogui.screenshot('/Users/SaiMoulikaBedadhala/Desktop/Screenshots/pic.png')
img.save('/Users/SaiMoulikaBedadhala/Desktop/Screenshots/pic.png')
speak("ScreenShot Saved...!")