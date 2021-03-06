import requests
import wikipedia
import pywhatkit as browse_kit
from email.message import EmailMessage
import smtplib
from decouple import config
import pyautogui as pg

# Functions this will perform -
# -> Find my IP address
# -> Search on Wikipedia
# -> Play videos on YouTube
# -> Search on Google
# -> Send WhatsApp message
# -> Send Email
# -> Get Latest News Headlines
# -> Get Weather Report
# -> Get Trending Movies
# -> Get Random Jokes
# -> Get Random Advice


def get_my_ip():
    ip_path = 'https://api64.ipify.org?format=json'
    response = requests.get(ip_path)
    ip_add = response.json()
    return ip_add['ip']


def search_wikipedia(command):
    result = wikipedia.summary(command, sentences=2)
    return result


def play_youtube(video):
    browse_kit.playonyt(video)  # used PyAutoGUI under the hood


def search_google(topic):
    browse_kit.search(topic)


def send_messages_whatsapp(number, message):
    browse_kit.sendwhatmsg_instantly(f'+91{number}', message)
    width, height = pg.size()
    pg.click(width / 2, height / 2)


def send_group_whatsapp(G_ID, message):
    browse_kit.sendwhatmsg_to_group_instantly(f'{G_ID}', message, wait_time=32)
    width, height = pg.size()
    pg.click(width / 2, height/2)
    pg.click()


EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')


def send_mails(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        mail_obj = smtplib.SMTP("smtp.gmail.com", 587)
        mail_obj.starttls()
        mail_obj.login(EMAIL, PASSWORD)
        mail_obj.send_message(email)
        mail_obj.close()
        return True
    except Exception as e:
        print(e)
        return False


NEWS_API = config('NEWS_API_KEY')


def get_news_headlines():  # NEWS API
    news_headlines = []
    news_source = []
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API}&category=general")
    value = response.json()
    articles = value['articles']
    for articles in articles:
        news_headlines.append(articles['title'])
        news_source.append(articles['source']['name'])

    return news_headlines[:6], news_source[:6]


WEATHER_API = config('OPEN_WEATHER_APP_ID')


def get_weather(city):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric')
    value = response.json()
    weather = value["weather"][0]["main"]
    temperature = value["main"]["temp"]
    feels_like = value["main"]["feels_like"]
    return weather, f"{temperature}???", f"{feels_like}???"


TREND_MOVIES_API = config('TREND_MOVIES_API_KEY')


def get_movies():
    trending_movies = []
    response = requests.get(f'https://api.themoviedb.org/3/trending/movie/day?api_key={TREND_MOVIES_API}')
    value = response.json()
    result = value['results']
    for results in result:
        trending_movies.append(results['original_title'])
    return trending_movies[:7]


def get_joke():
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get("https://icanhazdadjoke.com/", headers=headers)
    value = response.json()
    return value['joke']


def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    value = response.json()
    return value['slip']['advice']





















