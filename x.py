import speech_recognition as sr
import pyttsx3
import pywhatkit 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your alexa')
engine.say('what can i do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play' , '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

run_alexa()