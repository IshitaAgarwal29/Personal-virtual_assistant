
import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import psutil
import pyjokes
print("Welcome to the world of AI\n")
print("FUNCTIONS YOU CAN ASK JARVIS TO DO\n")
print("Search on wikipedia\n open youtube\n play music\n open google\n time\n send email\n search on chrome\n shutdown\n "
      "logout\n restart\n remember something\n can tell a joke\n battery percent")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("good evening")
    speak("I am Jarvis madam!! please tell me how may I help u")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")

        return "None"

    return query
def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("2020530810.ishita@ug.sharda.ac.in","Ishita@2910$")
    server.sendmail("2020530810.ishita@ug.sharda.ac.in", to,content)
    server.close()
def screenshoot():
    ing = pyautogui.screenshot()
    ing.save("D:\\screenshot\\photos")
def cpu():
    usage = str(psutil.cpu_percent())
    speak("Cpu is at"+ usage)
    battery = psutil.sensors_battery
    speak("battery is at")

def jokes():
    speak(pyjokes.get_joke())


def screenshot():
    pass


if _name_ == '_main_':
    wishMe()


    while True:
        query = takeCommand().lower()
        print(query)

        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)
            print(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir ='D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "time " in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Madam the time is{strTime} ")
        elif "what is your name" in query:
            speak("My name is jarvis")
        elif "who made you" in query:
            speak("I am made by my coder")
        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = Your email id
                sendmail(to,content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send email")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s"
            search = takeCommand().lower()
            webbrowser.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart " in query:
            os.system("shutdown /r /t 1")
        elif "Remember that" in query:
            speak("what should I remember")
            data = takeCommand()
            speak("you said me to remember"+ data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "what i said to remember" in query:
            remember = open("data.txt", "r")
            speak("you said to remember that "+ remember.read())
        elif "screenshoot" in query:
            screenshot()
            speak("Screenshot taken")
        elif "cpu" in query:
            cpu()

        elif "tell me a joke" in query:
            jokes()
        elif "quit" in query:
            exit()
            speak("signing off")
