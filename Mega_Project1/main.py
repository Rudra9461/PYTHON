import speech_recognition as sr  
import webbrowser       #to use browser dierectly to work for 
import pyttsx3         #covert text to speech 
import music_library
import requests

recognizer = sr.Recognizer()  #we make a class for speech recognizer to recognize the speech we provide 
engine = pyttsx3.init()         # we initialize the coverter   # take refrence from google for pyttsx3 website 
newsapi = "886cd467dee34524918ade8a22eefc2d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")    
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")   
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")  
    elif "open github" in c.lower():
        webbrowser.open("http://github.com")  
    elif c.lowe().statwith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song] 
        webbrowser.open(link)  

    elif "news" in c.lower():  
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=886cd467dee34524918ade8a22eefc2d")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            #Print the Headlines
            for article in articles:
                speak(article['title'])    


if __name__=="__main__":
    speak("Initiallizing Jarvis....")
    while True:
    # listen for the wake word Jarvis .
    # obtain audio from the microphone
        r = sr.Recognizer()        # recognize speech using Sphinx
        
        print("recogizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source , timeout=2 , phrase_time_limit=1)
            Word = r.recognize_google(audio)
            if(Word.lower()=="jarvis"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))
