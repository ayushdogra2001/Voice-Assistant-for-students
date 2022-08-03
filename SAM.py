# import subprocess
from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import numpy
from numpy import *
import re 
import pyttsx3
# import tkinter
import json
# import random
# import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import googlemaps
import os
# import winshell
import pyjokes
# import feedparser
import smtplib
import ctypes
import time
import requests
# import shutil
from twilio.rest import Client
# from client.textui import progress
# from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import wolframalpha
import pywhatkit
import datetime
import pickle
import os.path



engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[0].id)
engine.setProperty('voice',voice[1].id)

rate = engine.getProperty('rate')   
engine.setProperty('rate', 145)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()


  



def wishMe():
     hour= int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morning")

     elif hour>=12 and hour<18:
           speak("Good Afternoon")        
     else:
          speak("Good Evening")     

     speak("Sam here, how may I help you")     

def takeCommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio= r.listen(source)
   try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')    
        print(f"User Said:{query}\n")
          
   except Exception as e:
       # print(e)
        print("Say That Again Please...")
        return "None"      
   return query 
if __name__=="__main__":
  wishMe()
  while(True):
          
        query = takeCommand().lower()
        if "wikipedia" in query:
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query)
          speak(results)

        elif 'youtube' in query:
             webbrowser.open("youtube.com")

        elif 'google' in query:
             webbrowser.open("google.com")  
        elif 'stack overflow' in query:
             webbrowser.open("stackoverflow.com")    
  
        elif 'podcast' in query:
            webbrowser.open("podcasts.google.com")
       
        elif 'translate' in query:
             webbrowser.open("translate.google.co.in")    
  
        elif 'search' in query or 'play' in query:             
          #   query = query.replace("search", "")
          #   query = query.replace("play", "")         
          #   webbrowser.open(query)
          query = query.replace("play","")
          song = query.replace("play","")
          pywhatkit.playonyt(song)

          #pywhatkit.playonyt(song)

        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"The Time {strTime}")  

        elif "calculate" in query:             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client('K2GH2J-E8QPH2758Y')
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)  

        # elif 'doubt' or 'problems' in query:
        #     speak("Is it releated to Mathematics Or Science")
        #     db=takeCommand()
        #     if 'maths'in db:
        #         speak("here is some website that might help you")
        #         webbrowser.open("https://www.mathdoubts.com/")    
        #         webbrowser.open("https://www.doubtnut.com/")
        #         break
        #     elif 'science' in db:
        #         speak("here is some website that might help you")
        #         webbrowser.open("https://www.doubtnut.com/")
        #         webbrowser.open("https://www.quora.com/What-are-some-of-the-most-interesting-science-questions-how-why-what-to-know")
        #         break 
        #     break   
           
     
        elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you")
        elif 'joke' in query:
                speak(pyjokes.get_joke()) 
                print(pyjokes.get_joke())     

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")    

   

        elif "note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            query = takeCommand()
            if 'yes' in query or 'sure' in query:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
 
   
        elif "wikipedia" in query:
                webbrowser.open("wikipedia.com") 

        elif "i love you" in query:
            speak("It's hard to understand, love is complicated these days")

       

      
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")  

        elif 'lock window' in query:
                speak("doing it right way")
                ctypes.windll.user32.LockWorkStation()

        elif "what is" in query or "who is" in query or "how to" in query or "what does" in query:             
            client = wolframalpha.Client("K2GH2J-E8QPH2758Y")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

                
        elif "attendance" in query:
            speak("login using your mail id and go to the attendance page")
            webbrowser.open("https://academia.srmist.edu.in/#Page:My_Attendance")


        elif 'exit'in query or 'thanks' in query or 'thank you' in query:
            speak("Thanks for giving me your time")
            exit()    
        # else:
        #     speak("Couldn't get you please say that agian")          


 
     #    elif 'shutdown system' in query:
     #            speak("Give me few seconds")
     #            subprocess.call('shutdown / p /f')4
      
      
  # def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
     
#     server.login('your email id', 'your email password')
#     server.sendmail('your email id', to, content)
# def speak(text):
#     engine=pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     rate = engine.getProperty('rate')
#
#     engine.setProperty('rate', rate-20)
#
#     engine.say(text)
#     engine.runAndWait()
#
# speak("Welcome to mail service")
# SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
# def authenticate_gmail():
#     """Shows basic usage of the Gmail API.
#     Lists the user's Gmail labels.
#     """
#     creds = None
#
#     # The file token.pickle stores the user's
#     # access and refresh tokens, and is
#     # created automatically when the authorization
#     # flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#
#     # If there are no (valid) credentials available,
#     # let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port = 0)
#
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
# def check_mails(service):
#
#     # fetching emails of today's date
#     today = (date.today())
#
#     today_main = today.strftime('%Y/%m/%d')
#
#     # Call the Gmail API
#     results = service.users().messages().list(userId = 'me',labelIds=["INBOX","UNREAD"],q="after:{0} and category:Primary".format(today_main)).execute()
#     # The above code will get emails from primary
#     # inbox which are unread
#     messages = results.get('messages',[])
#
#
#     if not messages:
#
#         # if no new emails
#         print('No messages found.')
#         speak('No messages found.')
#     else:
#         m=""
#
#         # if email found
#         speak("{} new emails found".format(len(messages)))
#
#         speak("if you want to read any particular email just type read ")
#         speak("and for not reading type leave ")
#         for message in messages:
#
#             msg=service.users().messages().get(userId='me',
#                                                id = message['id'], format = 'metadata').execute()
#
#             for add in msg['payload']['headers']:
#                 if add['name']=="From":
#
#                     # fetching sender's email name
#                     a=str(add['value'].split("<")[0])
#                     print(a)
#
#                     speak("email from"+a)
#                     text=input()
#
#                     if text == "read":
#
#                         print(msg['snippet'])
#
#                         # speak up the mail
#                         speak(msg['snippet'])
#
#                     else:
#                         speak("email passed")          


        

        # elif 'send a mail' in query:
        #    try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         speak("whome should i send")
        #         to = input()   
        #         sendEmail(to, content)
        #         speak("Email has been sent !")
        #    except Exception as e:
        #         print(e)
        #         speak("I am not able to send this email")     


 #    elif "weather" in query:
                 
     #        # Google Open weather website
     #        # to get API of Open weather
     #        api_key = "Api key"
     #        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
     #        speak(" City name ")
     #        print("City name : ")
     #        city_name = takeCommand()
     #        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
     #        response = requests.get(complete_url)
     #        x = response.json()
             
     #        if x["cod"] != "404":
     #            y = x["main"]
     #            current_temperature = y["temp"]
     #            current_pressure = y["pressure"]
     #            current_humidiy = y["humidity"]
     #            z = x["weather"]
     #            weather_description = z[0]["description"]
     #            print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
     #        else:
     #            speak(" City Not Found ")   
     # 
     #      

     #    elif 'news' in query:
             
     #        try:
     #            jsonObj = urlopen('''https://www.indiatoday.in/''')
     #            data = json.load(jsonObj)
     #            i = 1
                 
     #            speak('here are some top news')
                                 
     #            for item in data['articles']:
                     
     #                print(str(i) + '. ' + item['title'] + '\n')
     #                print(item['description'] + '\n')
     #                speak(str(i) + '. ' + item['title'] + '\n')
     #                i += 1
     #        except Exception as e:
                 
     #            print(str(e))    

  #    elif "weather" in query:
                 
     #        # Google Open weather website
     #        # to get API of Open weather
     #        api_key = "Api key"
     #        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
     #        speak(" City name ")
     #        print("City name : ")
     #        city_name = takeCommand()
     #        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
     #        response = requests.get(complete_url)
     #        x = response.json()
             
     #        if x["cod"] != "404":
     #            y = x["main"]
     #            current_temperature = y["temp"]
     #            current_pressure = y["pressure"]
     #            current_humidiy = y["humidity"]
     #            z = x["weather"]
     #            weather_description = z[0]["description"]
     #            print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
     #        else:
     #            speak(" City Not Found ")    


  # elif "don't listen" in query or "stop listening" in query:
        #     speak("for how much time you want to stop me from listening commands")
        #     a = int(takeCommand())
        #     time.sleep(a)
        #     print(a)
