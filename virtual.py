import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import webbrowser
import os
import time
import subprocess


import json


print('Powering on')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning, I am Medi-help.")
        print("Hello,Good Morning, I am Medi-help.")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon, I am Medi-help.")
        print("Hello,Good Afternoon, I am Medi-help.")
    else:
        speak("Hello,Good Evening, I am Medi-help.")
        print("Hello,Good Evening, I am Medi-help.")


def introduce():
    speak("I will be evaluating you today to see how your mental health is. I will ask you a few questions and "
          "according to your answers and how you answer them I will make a decision. I will also evaluate using my "
          "inbuilt camera. I will watch your body language. Feel free to tell me everything. Let us get started.")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
            print(statement)

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Powering on")
wishMe()
introduce()


if __name__=='__main__':


    while True:
        speak("What is your name?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        speak("What is your age?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        speak("What is your job?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        speak("Have you felt stressed lately?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        speak("Are you able to sleep properly or is it hard for you to sleep?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        speak("Have you gone through anything that was hard to handle lately?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        speak("I have finished my eveluation and have concluded that you are very stressed and should get psychiatric evaluation.")
        speak("Thank you. Have a good day")
        
time.sleep(1)












