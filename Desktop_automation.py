import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import os
import smtplib
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak('Good morning!!')

    elif 12 <= hour < 18:
        speak('Good afternoon!!')

    else:
        speak('Good evening!!')

    speak('I am your friend and I am here to help. How can I help you')

def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query) 

    except Exception as e:
        #print(e)

        print("Say that again please ....")
        return "None"
    
    return query

def site(url):
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)


if __name__ == '__main__':
    #speak('I am your Desktop helper.   How may I help you.')
    wishMe()
    while True:
        
        query = takeComand().lower()

        if 'google' in query:
            url = 'google.com'
            site(url)

        elif 'youtube' in query:
            url = 'youtube.com'
            site(url)

        elif 'music' in query:
            url = 'https://www.hungama.com/playlists/top-hits-of-arijit-singh/91368/'
            site(url)

        elif 'visual studio' in query:
            code_path = 'C:\\Users\\rajan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(code_path)

        elif 'whatsapp' in query:
            url = 'https://web.whatsapp.com/'
            site(url)

        elif 'close' in query:
            break