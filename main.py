import webbrowser
import speech_recognition as sr
import pyttsx3
import musiclibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi='0087babe674f46ef9250e08419977f57'

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def processCommand(c):
    if 'open google' in c.lower():
        webbrowser.open('https://www.google.com')
    elif 'open youtube' in c.lower():
        webbrowser.open('https://www.youtube.com') 
    elif 'open facebook' in c.lower():
        webbrowser.open('https://www.facebook.com')
    elif 'open twitter' in c.lower():
        webbrowser.open('https://www.twitter.com')          
    elif 'open instagram' in c.lower():     
        webbrowser.open('https://www.instagram.com')
    elif 'open whatsapp' in c.lower():
        webbrowser.open('https://web.whatsapp.com')
    elif 'linkedin' in c.lower():
        webbrowser.open('https://www.linkedin.com')
    elif c.lower().startswith('play'):
        song=c.lower().split(' ')[1] 
        link=musiclibrary.music[song]
        webbrowser.open(link)
        
    
    elif'news'in c.lower():
        r= requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}')
        
    if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])    
            for article in articles[:5]:
                speak(article['title'])
            
    else :
        #let open ai handle the req
           pass    
        

if __name__ == '__main__':
    speak('Initializing Apex......')
    while True:
        # Listen for the word "Apex"
        #obtaining audio from the microphone2
        r= sr.Recognizer()
        
        print('recognizing....')
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if(word.lower() == "Apex"):
                speak('yes boss')
                # Listen for the command
                with sr.Microphone() as source:
                    print("Apex activated...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print('error; {0}'.format(e)) 
            
            
            