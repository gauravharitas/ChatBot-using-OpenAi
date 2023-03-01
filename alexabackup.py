import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from twilio.rest import Client
import winsound
import pywhatkit as kit
import pyautogui as pag


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#1 for david
#0 for zara
engine.setProperty('voice', voices[0].id)

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")

    elif hour >=12 and hour <16:
        speak("Good Afternoon !")

    elif hour >=16 and hour <19:
        speak("Good Evening !")

    else:
        speak("Good Night !")

    speak("I am Alexa sir, How may I help you ?")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecmd():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language = 'en-in')# hi-In
        print(f"User said: {query}\n")
        

        

    except Exception as e:
        print("Say that again please ...")
        return "none"

    return query

def sendmail(to, body):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("chinuharitas2.0@gmail.com", "Gaurav@77")
    server.sendmail("chinuharitas2.0@gmail.com", to, body)
    server.close()

def type(loc):
    speak("sir, do u wanna append or write ?")
    d=takecmd().lower()
    if 'write' in d:
        file = open(f'{loc}','w')
        speak("What do you wanna write sir?")
        write=takecmd()
        file.write(write)
        file.close()
        speak("Data Writing finished....")

    elif 'append' in d:
        file = open(f'{loc}','a')
        speak("What do you wanna append sir?")
        write=takecmd()
        file.write(f"\n{write}")
        file.close()
        speak("Data Appending finished....")
    speak("Sir, typing done....")




if __name__ == "__main__":
    wishme()
    while True:
    

        query = takecmd().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            try:

                query=query.replace("wikipedia"," ")
                result=wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)

            except Exception as e:
                speak("There is no such data available on wikipedia...")

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'instagram' in query:
            speak("Opening instagram")
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            music_dir = 'F:\\Alexa\\Songs'
            songs=os.listdir(music_dir)
            if len(songs)>0:
                speak("playing music")
                for i in songs:
                    s=random.randint(0,len(songs))
                    os.startfile(os.path.join(music_dir, songs[s]))
                    break
            else:
                speak("There is no song to play in the directory")
        
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'vs code' in query:
            speak("Opening VS Code")
            vspath="C:\\Users\\Gaurav Dev\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)

        elif 'send email' in query:
            speak("To whom you want to send the email")
            person=takecmd()
            
            speak("Sir, please tell me the mail id")
            inputid=takecmd().lower()
            outerid='@gmail.com'
            compid=inputid+outerid
            id=compid.lower()
            id=id.replace(" ","")
            try:
                speak("what should i say ?")
                body=takecmd()
                to=id
                speak("Are u sure to send email")
                print(f"The mail is {to}")
                
                speak("Say 1 for yes and 0 for no.")
                ch=takecmd().lower()
                
                
                if ch=='one' or ch == 'One' or ch == '1':
                    sendmail(to, body)
                    speak(f"Email sent... to Mr.{person}")

                else:
                    
                    speak("Email sending procedure aborted...")

            except Exception as e:

                speak("Sorry Mr. Gaurav I am not able to send this email.")

        elif 'open browser' in query:
            speak("what do you want to search in chrome ?")
            srch=takecmd()
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(str(f'{srch}'))
            
        elif 'search' in query:
            speak("Searching...")
            query=query.replace("search","")
            kit.search(query)

        elif 'close' in query:
            q=query
            q=q.lower()
            q=q.replace("close","")
            q=q.replace(" ","")
            pre=q
            suf='.exe'
            comp=pre+suf
            os.system(f"taskkill /im {comp} /f")
            speak(f"{pre} closed...")

        elif 'open notepad' in query:
            speak("opening notepad")

            os.startfile('C://WINDOWS//system32//notepad.exe')
            loc=str("C:\\Users\\Gaurav Dev\\Desktop\\Alexa\\alexadocx.txt")
            pag.hotkey('ctrl', 'o')
            pag.write(loc)
            pag.press('enter')
            type(loc)
            pag.hotkey('ctrl', 's')
            pag.click(661, 359, button='left')
            





        # elif 'type' in query:
        #     speak("sir, do u wanna append or write")
        #     d=takecmd().lower()
        #     if 'write' in d:
        #         file = open('alexadocx.txt','w')
        #         speak("What do you wanna append sir?")
        #         write=takecmd()
        #         file.write(write)
        #         file.close()

        #     elif 'append' in d:
        #         file = open('alexadocx.txt','a')
        #         speak("What do you wanna write sir?")
        #         write=takecmd()
        #         file.write(write)
        #         file.close()

            
        elif 'quit' in query:
            speak("Quiting....")
            speak("Thank you for using me...")
            break
    
                    
                

            
            

                
            
           

