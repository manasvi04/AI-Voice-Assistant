import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyjokes
import psutil
import random
import json




print('Initializing your AI companion - Zia')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Zia")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Zia is shutting down,Good bye')
            print('your personal assistant Zia is shutting down,Good bye')
            break

        
    
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="02661c4a92ffa115fa8856e21ef0ecd4"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")    


        elif 'who are you' in statement or 'what can you do' in statement:
            speak('Hi, I’m Zia, your personal assistant, version 1 point 0!'
                  'I’m here to simplify your day by handling tasks like opening YouTube, Gmail, or Google Chrome, telling the'
                  'current time, or snapping a photo. I can also search Wikipedia, provide weather updates, and share the latest Times of India headlines. '
                  'Whether you need quick info or assistance, just ask, and I’m here to help! ')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by AI voice assistant Team")
            print("I was built by  AI voice assistant Team")


        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")   


        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is stackoverflow")


        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)  


        elif "joke" in statement:
             joke = pyjokes.get_joke()
             speak(joke)
             print(f"Zia: {joke}")


        elif "open notepad" in statement or "open calculator" in statement or "open vlc" in statement:
            if "notepad" in statement:
                os.system("notepad.exe")
                speak("Opening Notepad")
            elif "calculator" in statement:
                os.system("calc.exe")
                speak("Opening Calculator")
            elif "vlc" in statement:
                os.system("start vlc")
                speak("Opening VLC Player")


        elif "battery status" in statement or "cpu status" in statement:
            battery = psutil.sensors_battery()
            percent = battery.percent
            cpu_usage = psutil.cpu_percent()
            speak(f"Your system battery is at {percent} percent.")
            speak(f"Current CPU usage is {cpu_usage} percent.")


        elif "count words" in statement:
            speak("Please say the sentence.")
            sentence = takeCommand()
            words = sentence.split()
            word_count = len(words)
            speak(f"Your sentence has {word_count} words.") 


        elif "start Countdown" in statement:
            speak("For how many seconds?")
            try:
                seconds = int(input("Enter seconds: "))
                while seconds:
                    mins, secs = divmod(seconds, 60)
                    timeformat = f"{mins:02}:{secs:02}"
                    print(timeformat, end="\r")
                    time.sleep(1)
                    seconds -= 1
                speak("Time's up!")
            except ValueError:
                speak("Invalid input. Please enter a number.")


        elif "suggest an idea" in statement or "give me ideas" in statement:
              try:
                  with open("ideas.json", "r") as file:
                       ideas = json.load(file)

                  speak("Sure! What type of ideas are you looking for? You can ask for birthday decor, party themes, date night ideas, DIY gifts, festival decorations, surprise gifts, outdoor adventures, workplace celebrations, or home makeovers.")
                  print("Choose a category: birthday decor, party themes, date night ideas, DIY gifts, festival decorations, surprise gifts, outdoor adventures, workplace celebrations, or home makeovers.")
        
                  idea_category = takeCommand().lower()

                  if idea_category in ideas:
                     suggestion = random.choice(ideas[idea_category])
                     speak(f"Here's an idea for {idea_category}: {suggestion}")
                     print(f"Idea for {idea_category}: {suggestion}")
                  else:
                      speak("Sorry, I don't have ideas for that. But I can suggest birthday decor, party themes, date night ideas, DIY gifts, festival decorations, surprise gifts, outdoor adventures, workplace celebrations, or home makeovers.")
                      print("Sorry, I don't have ideas for that.")

              except Exception as e:
                           speak("Oops! I couldn't load the ideas. Please check the file.")
                           print(f"Error: {e}")      


        elif "typing test" in statement:
            test_sentence = "The quick brown fox jumps over the lazy dog."
            speak("Type the following sentence as fast as you can:")
            print(test_sentence)

            input("Press Enter when ready...")
            start_time = time.time()
            user_input = input("Type here: ")
            end_time = time.time()

            time_taken = end_time - start_time
            word_count = len(user_input.split())
            speed = round(word_count / (time_taken / 60), 2)

            speak(f"You typed {word_count} words in {round(time_taken, 2)} seconds. Your speed is {speed} words per minute!")
            print(f"You typed {word_count} words in {round(time_taken, 2)} seconds. Your speed is {speed} words per minute!")


        elif "roll a dice" in statement or "roll dice" in statement:
            dice_roll = random.randint(1, 6)
            speak(f"The dice rolled a {dice_roll}")
            print(f"The dice rolled a {dice_roll}")
       

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="8X6V6Q-7R9WXQ28PH"
            client = wolframalpha.Client('8X6V6Q-7R9WXQ28PH')
            res = client.query(question)
            answer = next(res.results).text
            print(answer) 
            speak(answer)
             

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
    

   
        else:
            speak("Sorry I can't help you")
            print("Sorry I can't help you")
time.sleep(3)












