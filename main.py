import pyttsx3  #text to speech engine pip
import speech_recognition as sr
import datetime 
import os
import smtplib
import random
import pandas as pd  #allows importing data of various file formats
import numpy as np  #multidimensional array used to store values of same type

engine = pyttsx3.init()
voices = engine.getProperty('voices')#initializing voices


engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  #it will not speak until it encounters runAndwait()


def wishMe():  #just for fun
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening !")     

    speak("i am exenor, what can i do for you ? ")  #named it exenor you can name anything you wish   

def gooffline():
    speak('thank you')
    speak('until next time')
    quit()      

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:  #taking voice input
        print("callibrating the speaker ")
        r.adjust_for_ambient_noise(source,duration=2) #avoids surrounding noise of lower threshold value
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #google engine to recognize input voice in english
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

"""
def writeExcel(to, content):
   
"""


excel_file = 'C:\\Users\\SUBHASMITA\\Desktop\\Python Projects\\automating excel sheets by voice\\Workbook1.xlsx'
df = pd.read_excel(excel_file)
print(df)


if __name__ == "__main__":
    wishMe()
    while True:
        #if 1:
        query = takeCommand().lower()

        if 'search excel' in query:
            speak('what do you want me to search?')   


        elif 'programmer' in query:
            speak('searching excel file for programmer..')
            query = query.replace("excel_files", "")


            excel_files = ['C:\\Users\\SUBHASMITA\\Desktop\\Python Projects\\automating excel sheets by voice\\Workbook1.xlsx']


            for individual_excel_file in excel_files:
    
                df = pd.read_excel(individual_excel_file)
                programmers = df['Name'].where(df['Occupation'] == 'Programmer').dropna()
                print("File Name\t" + individual_excel_file)
                print(programmers)
           
            speak(excel_files)
            speak(programmers)




        elif 'write excel' in query:
            speak("which excel file do you want to edit")
                
                
                
        elif 'sheet 1' in query:
            speak('opening excel file named workbook1')
            book1Path = "C:\\Users\\SUBHASMITA\\Desktop\\automating excel sheets by voice"
            os.startfile(book1Path)

        elif 'sheet 2' in query:
            speak('opening workbook2')
            book2Path ="C:\\Users\\SUBHASMITA\\Desktop\\automating excel sheets by voice"
            os.startfile(book2Path)
        

            
        #general query part

        elif 'introduce yourself' in query:
            strintro = ('i am exenor and i am here to help you') 
            speak(f"sir, {strintro}")  

        elif 'quit' in query:
            gooffline()  

    
        else:
            speak('i could not understand , please try again ')    
                   

        