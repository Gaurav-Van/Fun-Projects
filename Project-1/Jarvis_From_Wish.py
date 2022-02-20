import pyttsx3
import speech_recognition as sr
from decouple import config
import datetime as dt
from random import choices
from Command_Utility import if_Recognize_Text
import os
import subprocess as sp

# PART1 - DEFINITION OF BOT - SET UP
USERNAME = config('USER')
BOTNAME = config('BOTNAME')

Engine = pyttsx3.init('sapi5')  # sapi5 - Microsoft Speech API

Engine.setProperty('rate', 175)
Engine.setProperty('volume', 2.0)
Voice_mod = Engine.getProperty('voices')
Engine.setProperty('voice', Voice_mod[0].id)


def speak(text):
    Engine.say(text)
    Engine.runAndWait()


def greet_user():
    hour = dt.datetime.today().hour

    if (hour >= 4) and (hour < 12):
        speak(f'Good Morning {USERNAME}')
    elif (hour >= 12) and (hour < 17):
        speak(f'Good Afternoon {USERNAME}')
    elif (hour >= 17) and (hour <= 20):
        speak(f'Good Evening {USERNAME}')

    speak(f'I am {BOTNAME}, How may I Assist You')


def taking_user_Input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am Listening")
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing .... ")
        command = r.recognize_google(audio, language='en-in')
        if 'Terminate' in command:
            hour = dt.datetime.today().hour
            if (hour >= 21) and (hour < 4):
                speak(f"Good Night {USERNAME}, Take care and Sweet Dreams")
            elif (hour >= 17) and (hour < 21):
                speak(f"Alright,  Have a Good Evening {USERNAME}")
            else:
                speak(f"Alright,  Have a Good Day {USERNAME}")

            exit()

        else:
            speak(choices(if_Recognize_Text))

    except Exception as e:
        print(e)
        speak("Sincere Apologies, I was not able to Recognize what you said, Can you Repeat it again ? ")
        Recursive_command = taking_user_Input()
        command = Recursive_command

    return command
