# Import  all the required Libraries
import speech_recognition as sr
import pyttsx3
import datetime
#import wikipedia
#import webbrowser
import os
import time
import subprocess
#import wolframalpha
import json
import requests
import nltk
from geotext import GeoText
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import datetime
import time
from playsound import  playsound


# Function to enquire about the weather and speak:
def weat(sent):
	places = GeoText(sent)
	city = places.cities[0]
	base_url = "https://api.openweathermap.org/data/2.5/weather?"
	api_key = # Your API key here
	url = base_url + "q=" + city + "&appid=" + api_key
	response = requests.get(url)
	if response.status_code == 200:
	   data = response.json()
	   main = data['main']
	   temperature = '%.1f'%(main['temp']-273)
	   humidity = main['humidity']
	   pressure = main['pressure']
	   report = data['weather']
	   speak(f"{city:-^30}")
	   speak(f"Temperature: {temperature}")
	   speak(f"Humidity: {humidity}")
	   speak(f"Weather Report is: {report[0]['description']}")

	   print(f"{city:-^30}")
	   print(f"Temperature: {temperature}")
	   print(f"Humidity: {humidity}")
	   print(f"Weather Report is: {report[0]['description']}")
	else:
	   speak("I'm sorry, couldn't get that for you.")


# Function to play any song from youtube
def play(sent):
	sent = sent[1:]
	sent = ' '.join(sent)
	music_name = sent
	query_string = urllib.parse.urlencode({"search_query": music_name})
	formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
	search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
	clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
	clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
	inspect = BeautifulSoup(clip.content, "html.parser")
	yt_title = inspect.find_all("meta", property="og:title")
	import pafy
	# url of video 
	url = clip2
	video = pafy.new(url) 
	value = video.length
	for concatMusic1 in yt_title:
	    pass
	print(concatMusic1['content'])
	#print(clip2)
	subprocess.Popen("start /b "+ clip2 + " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",shell=True)
	import time,keyboard
	time.sleep(value)
	keyboard.press_and_release('ctrl+w')


def alarm():
	speak('For when should I set an alarm for?')
	set_alarm = takeCommand()
	#12 15 in a string
	set_alarm = set_alarm.split()
	set_alarm = ':'.join(set_alarm)
	# For example: set_alarm = "12:15"
	speak('Alarm set for {}'.format(set_alarm))
	while(True):
		time.sleep(1)
		current_time = datetime.datetime.now().strftime("%H:%M")
		if current_time == set_alarm:
			playsound("13767_morning_alarm.mp3")
			break


def news():
	url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=')
	api_key = # Your API key here
	url+=api_key
		try:
			response = requests.get(url)
		except:
			speak("couldn't retrieve information, please check your internet.")

		news = json.loads(response.text)

		for new in news['articles']:
			speak(str(new['title']))
			time.sleep(2)


# pyttsx is the python text to speech library,initialise and set values for voice characteristics.
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('rate',150)
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen for user input
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("I didn't quite catch that.")
            return "None"
        return statement


#Greet
greet = 'Hi, My name is Mara and I am your personal assistant!'
speak(greet)


#Initial starting command
speak("How can I help you?")
statement = takeCommand()
# Example: statement = 'how is the weather in Seoul?'



while(1):
	# To split the list and remove the stopwords
	sentence = nltk.word_tokenize(statement)
	from nltk.corpus import stopwords
	stop = stopwords.words('english')
	sentence = [w for w in sentence if not w.lower() in stop]


	# If user asks for the weather
	if 'weather' in sentence:
		weat(statement)


	# If user wants to play any song
	if 'play' in sentence:
		play(sentence)


	# User wants current date
	if 'today\'s' and 'date' in sentence:
		speak(datetime.time(datetime.now()))


	# User wants current time
	if 'time' or 'right now' in sentence:
	t = time.localtime()
	current_time = time.strftime("%H %M", t)
	speak(current_time)


	# For setting an alarm
	if 'set' and 'alarm' in sentence:
		alarm()

	if 'news' and 'India' in sentence:
		news()


	# Any Other Commands
	speak("Anything else I can help you with?")


	## Voice input or sentence
	statement = takeCommand()
	#statement = 'play hello by adele'


	if('bye' in statement or 'shut down' in statement or 'talk to you later' in statement):
		break


# For shutting down the assistant.
speak('Your assistant is logging off!')
