import time
import pyttsx3
import speech_recognition as sr
from decouple import config
import datetime as dt
from random import choices
from Command_Utility import if_Recognize_Text
from Online_Utilities import get_advice, get_joke, get_movies, get_news_headlines, get_weather, get_my_ip, send_mails, \
    send_messages_whatsapp, send_group_whatsapp, search_google, search_wikipedia, play_youtube
from Offline_Utilities import open_Whatsapp, open_cmd, open_camera, open_Brave, open_Teams, open_Discord, open_Notepad, \
    open_Spotify, open_Youtube
import requests

# PART1 - DEFINITION OF BOT - SET UP
USERNAME = config('USER')
BOTNAME = config('BOTNAME')

Engine = pyttsx3.init('sapi5')  # sapi5 - Microsoft Speech API

Engine.setProperty('rate', 175)
Engine.setProperty('volume', 2.0)
Voice_mod = Engine.getProperty('voices')
Engine.setProperty('voice', Voice_mod[0].id)


# PART2 - FUNCTIONALITY OF THE BOT
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
        if 'exit' in command:
            num = 1
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


if __name__ == "__main__":
    greet_user()
    while True:
        Command_Real = taking_user_Input()
        Command = Command_Real.lower()
        # --------------------------------------------------------------------------------------- #
        if 'open camera' in Command:
            open_camera()

        elif 'open notepad' in Command:
            open_Notepad()

        elif 'open microsoft teams' in Command or 'open teams' in Command:
            open_Teams()

        elif 'open brave browser' in Command or 'open brave' in Command:
            open_Brave()

        elif 'open youtube' in Command:
            open_Youtube()

        elif 'open discord' in Command:
            open_Discord()

        elif 'open spotify' in Command or 'play spotify' in Command:
            open_Spotify()

        elif 'open whatsapp' in Command:
            open_Whatsapp()

        elif 'open command prompt' in Command or 'open cmd' in Command:
            open_cmd()

        # ------------------------------------------------------------------------------------------ #
        elif 'what is my ip address' in Command or 'my ip address' in Command:
            answer_ip_add = get_my_ip()
            print(answer_ip_add)
            speak(f"Your IP ADDRESS is {answer_ip_add} ")

        elif 'play youtube' in Command:
            speak("Which video u want to play ?")
            response = taking_user_Input().lower()
            play_youtube(response)

        elif 'enable wikipedia' in Command or 'wikipedia' in Command:
            speak("What do you want to search ? ")
            response = taking_user_Input().lower()
            answer = search_wikipedia(response)
            speak(f"According to wikipedia  {answer}")
            speak("For your convenience result is on the screen")
            print(answer, sep='\n')

        elif 'enable google search' in Command or 'google' in Command:
            speak("What do you want to search ? ")
            response = taking_user_Input().lower()
            speak(f"Searching {response} on google, Here we go vooooooo")
            search_google(response)

        elif 'send a whatsapp message' in Command:
            speak("On group or Private Number ?")
            initial_response = taking_user_Input().lower()

            if 'private number' in initial_response:
                speak("Speech detection is disabled for this operation for the sake of Privacy so "
                      "Enter the Number on to the console ")
                number = input('Enter the Number +91 :')
                speak("And the message would be ?")
                message = taking_user_Input().lower()
                send_messages_whatsapp(number, message)
                speak("Operation Completed, Message delivered")

            else:
                speak("Speech detection is disabled for this operation for the sake of Privacy so "
                      "Enter the Id or Code of the group on to the console ")
                Grp_id = input("Enter the ID: ")
                speak("And the message would be ?")
                message = taking_user_Input().lower()
                send_group_whatsapp(Grp_id, message)
                speak("Operation Completed, Message delivered")

        elif 'send an email' in Command:
            speak("Speech detection is disabled for this operation for the sake of Privacy so, tell me")
            speak("To whom ? Enter the Mail address of the receiver")
            receiver_id = input("Enter the mail id: ")
            speak("Subject Should be ?")
            subject = taking_user_Input().capitalize()
            speak("and the Message Would be ?")
            message = taking_user_Input().capitalize()

            if send_mails(receiver_id, subject, message):
                speak("Execution Completed, Mail delivered")

            else:
                speak(
                    "There was a Problem in sending the mail. Possible errors can be - wrong email id or problem at login. "
                    "Please try again")

        elif 'tell me a joke' in Command:
            speak("Alright, Time to Test Your Level of Humor Because mine is superior all the time")
            joke = get_joke()
            speak(f'The Joke is - {joke}')
            print(joke)

        elif 'any advice for me' in Command or 'can you give me an advice' in Command:
            speak("Alright, as a Virtual Assistant, It is my duty to server you, so Here it goes")
            advice = get_advice()
            speak(advice)
            print(advice)

        elif 'list of trending movies' in Command:
            speak(f"List of Trending movies in world right now {get_movies()}")
            print(get_movies())

        elif 'update me on news' in Command or 'news' in Command:
            head, source = get_news_headlines()
            speak("Today's Headlines are presented by ")

            for i, j in enumerate(head):
                speak(f"{source[i]} and they reports {head[i]} ")
                speak("Next one is")

            print(source, head, sep='-->')

        elif 'weather right now' in Command or 'weather' in Command:
            ip_add = get_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_add}/city/").text
            speak(f"Generating Weather report for your city {city}")
            weather, temp, feels_like = get_weather(city)
            speak(f"The Temperature is {temp} and almost it feels like {feels_like} and uhh Yes")
            speak(f"Weather can be described as {weather}")
            print(f"Temperature -> {temp} \nIt Feels Like -> {feels_like} \nWeather Described as -> {weather}")

        time.sleep(4)
