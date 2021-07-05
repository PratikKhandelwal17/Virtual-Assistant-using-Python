# Virtual-Assistant-using-Python

Virtual Assistant named Mara has been created using Python. Created using multiple libraries including:
1. pyttsx3: Python speech to text library
2. BeatifulSoup: Library for web parsing and extracting html elements
3. nltk: Python library for natural language processing 
4. requests,url,datetime,json,subprocess

- It has multiple features and new features are being added.

1. Weather conditions: It returns and speaks out the weather conditions in any city for which the user asks, it returns the temperature, the humidity and the weather report or short summary. API used: 'OpenWeatherMap.org'

2. Youtube songs: It opens a new browser tab and plays the song of user choice. After the song has been finished, the tab closes automatically and asks for the next command of the user.

3. Alarm Clock: Sets an Alarm clock for the time the user wants and will play the track "13767_morning_alarm.mp3" included in the repository. It takes in string input and within a while loop checks for the equality.

4. Date and time: Returns the current date and time of the system upon user command

5. News: Reads out the top 5 news of the region in which you are in, even the description can be included within the code, API used: 'NewsApi.org'. Currently the code has been programmed to run and provide news only for 'India'.

# Future Changes:
1. Currently the software will accept only 1 input and cannot simaltaneously work at 2 commands at the same time.
2. Include more features and tasks to expand the domain of work.
3. To improve the accuracy of speech to text and reduce inability to hear during noise.
4. Feature for the user to stop any command at any point in time.
