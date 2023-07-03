import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import smtplib
import ctypes
import time
import requests
import shutil
import os
import wolframalpha
import requests
from bs4 import BeautifulSoup


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening .......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing......")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Can't access.....")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    sender_email = "ghosharchisman58@gmail.com"
    password = input(str("please enter your password"))

    # Enable low security in gmail
    server.login(sender_email, password)
    server.sendmail("ghosharchisman58@gmail.com", to, content)
    server.close()


def mylocation():
    ip_add = requests.get("https://api.ipyify.org").text
    url = "https://get/.geojs.io/v1/ip/geo" + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speechtx(f" sir, now you are in {state, country}.")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 100)
    engine.say(x)
    engine.runAndWait()


def get_temperature(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == "404":
        return None
    else:
        temperature = data["main"]["temp"]
        return temperature


if __name__ == '__main__':

    # if sptext().lower() == "hey peter":
    data1 = sptext().lower()
    assert isinstance(data1, object)

    if "your name" in data1:
        name = "my name is peter "
        speechtx(name)

    elif " old are you" in data1:
        age = "i was born in kolkata, now i am two years old "
        speechtx(age)

    elif " time " in data1:
        time_now = datetime.datetime.now().strftime("%I%M%p")
        speechtx(time_now)

    elif " google " in data1:
        webbrowser.open_new_tab("http://google.com/")

    elif " youtube " in data1:
        speechtx(" opening youtube..")
        webbrowser.open_new_tab("http://youtube.com/")
    elif 'email to me' in data1:
        try:
            speechtx("What should I say?")
            content = sptext()
            # speechtx("whom should i send")
            to = " cse2021026@rcciit.org.in "
            sendEmail(to, content)
            speechtx("Email has been sent !")
        except Exception as e:
            print(e)
            speechtx("I am not able to send this email")

    elif 'how are you' in data1:
        speechtx("I am fine, Thank you")
        speechtx("How are you, Sir")
    elif 'fine' in data1 or "good" in data1:
        speechtx("It's good to know that your fine")
    elif 'joke' in data1:
        speechtx(pyjokes.get_joke(category="neutral"))
    elif "calculate" in data1:

        app_id = "736G6P-AW3KAJJ5RW"
        client = wolframalpha.Client(app_id)
        while True:
            query = str(input('qry: '))
            res = client.query(query)
            output = next(res.results).text
            print(output)
            speechtx(output)

    elif " location " in data1:
        speechtx("finding your location")
        # mylocation()

    elif " powerpoint " in data1:
        speechtx("opening powerpoint ")
        power = r"C:\Users\ADMIN\Downloads\INTERCONNECTION NETWORKS (1).pptx"
        os.startfile(power)
    elif " play song " in data1:
        add = r"C:\Users\ADMIN\Videos\Captures"
        listsong = os.listdir(add)
        print(listsong)
        os.startfile(os.path.join(add, listsong[3]))
    elif "will you be my gf" in data1 or "will you be my bf" in data1:
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in data1:
        speak("I'm fine, glad you me that")

    elif "i love you" in data1:
        speechtx("It's hard to understand")
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Love")

    elif "what is" in data1 or "who is" in data1:

        # Use the same API key
        # that we have generated earlier
        client = wolframalpha.Client("736G6P-AW3KAJJ5RW")
        res = client.query(data1)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("No results")
    elif " temperature " in data1:
        api_key = "c45e7d6bd7073c9f6919543998a832ae"
        city_name = "kolkata"
        temperature = get_temperature(city_name, api_key)
        if temperature:
            print(f"The temperature in {city_name} is {temperature}°C.")
        else:
            print("Sorry, I could not retrieve the temperature.")

# else:
# print("thanks")
