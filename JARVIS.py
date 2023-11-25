import  pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Wait for Few Moment...")
        query=r.recognize_google(audio, language='en-in')
        print(f"You just said:  {query}\n") 
    except Exception as e:
        print(e)
        speak("Please Tell me again")
        query="none"
    return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning BOSS")
        speak("Good Morning BOSS  ")
    elif hour>=12 and hour<17:
        print("Good Afternoon BOSS")
        speak("Good Afternoon BOSS  ")
    elif hour>=17 and hour<21:
        print("Good Evening BOSS")
        speak("Good Evening BOSS  ")
    else:
        print("Good Night BOSS")
        speak("Good Night BOSS  ")


if __name__ == "__main__":
    wishings()
    query=commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir,the time is {strTime}")

    elif 'open chrome' in query:
        speak("Opening chrome Application sir....")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'wikipedia' in query:
        speak("searching in Wikipedia...")
        try:
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia,")
            speak(results)
            speak(results)
        except:
            speak("No results found..")
            print("No results found.")                




