import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pocketsphinx 



#ACTIVATING VOICE ENGINE
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Intro
def Wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" how do we get started ?..")

#voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("CALLIBRATING THE SPEAKER, PLEASE WAIT")
        #speak("CALLIBRATING THE SPEAKER, PLEASE WAIT")

        r.adjust_for_ambient_noise(source, duration=5)
        print("LISTENING..")
        speak("LISTENING..")
        r.pause_threshold = 1
        audio = r.listen(source)

    #google engine to recognize input voice in english
    try:
        print("RECOGNIZING...")
        query = r.recognize_sphinx(audio)
        print(f"User Said: {query}\n")

    except sr.UnknownValueError:
        print("I'M SORRY, PLEASE SAY THAT AGAIN.")
        return "None"

    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))    
        
    return query



def openExcel():
    speak("which excel file do you want to edit")
    if 'file one' in query:
        speak('opening excel file one')
        os.startfile(file1)

    elif 'file two' in query:
        speak('opening file two')
        os.startfile(file2)

    elif 'file three' in query:
        speak('opening file three')
        os.startfile(file3)

    else:
        speak("Please say it clear")    


#switchoff voice
def Exit():
    speak(" Thank You.... See you next time. ")
    quit()


if __name__ == "__main__":

    Wish()
    while True:
        query = takeCommand()
        wrd = "{query}"

        if 'search excel' in query:
            speak("Please Specify the search criteria")

        elif wrd in query:
            speak("SEARCHING FILE")
            txt = df_comb[wrd]
            print(txt)
            speak(txt)



        #combine all files into one dataframe for easier searching
        elif 'combine' in query:
            speak("combining all excel files")
            df_comb = pd.concat([df_customers, df_wrkbk1, df_wrkbk2]).dropna()
        

        #create a new combined file
        elif 'create' in query:
            speak("creating a new combined csv file")
            df_comb.to_csv("combined.csv")
            print(df_comb)



        #write to exixting file
        #if 'write excel' or 'edit' in query:
            #openExcel()

        elif 'show specific' in query:
            speak("Which file do you want to search specifically") 
            #if ''  : 


        elif 'exit' in query:
            Exit()   

   

    

#excel section
file1 = 'Test Assests\Data Files\customers.csv'
file2 = 'Test Assests\Data Files\Workbook1.xlsx'
file3 = 'Test Assests\Data Files\Workbook2.xlsx'


df_customers = pd.read_csv(file1)
df_wrkbk1 = pd.read_excel(file2)
df_wrkbk2 = pd.read_excel(file3)



"""
pivot = df_comb.groupby(['Age']).mean()
prod = pivot.loc[::]  # new pandas fnct to takw multiple rpws of data

print(prod)

prod.plot(kind='bar')
plt.show()
"""
