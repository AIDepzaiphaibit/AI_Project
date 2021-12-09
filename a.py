import pyttsx3
import datetime
import speech_recognition

AImouth = pyttsx3.init()
voice = AImouth.getProperty('voices')
AImouth.setProperty('voice',voice[0].id) # pyttsx3 has three voices. [1,2,3]

def speak(audio):
    print("Robot: " + str(audio))
    AImouth.say(audio)
    AImouth.runAndWait()

def listen():
    AIear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        audio = AIear.listen(mic)
    try:
        you = AIear.recognize_google(audio,language='en')
        print("You: " + str(you))
    except:
        speak("I can't hear you, try again!")

def time():
    Time = datime.datime.now().strftime('%H:%M:%S %p') # %H: hour | %M: minute | %S: second %p: PM or AM
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if (hour >= 4) and (hour < 12):
        speak("Good Morning")
    if (hour >= 12) and (hour < 18):
        speak("Good Affternoon")
    if (hour >= 18) and (hour < 24):
        speak("Good Night")
    else:
        speak("!!!"

if __name__=='__main__':
    
