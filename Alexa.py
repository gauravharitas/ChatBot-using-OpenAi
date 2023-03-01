import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from twilio.rest import Client
import pywhatkit as kit
import requests
import json
import time
from wikipedia.wikipedia import languages


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
#1 for david
#0 for zara
engine.setProperty('voice', voices[0].id)

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour >=12 and hour <16:
        speak("Good Afternoon sir")

    elif hour >=16 and hour <19:
        speak("Good Evening sir")

    else:
        speak("Good Night sir")

    speak("I am Alexa with Speed of 1 Terahertz and Memory of 1 Zettabytes. How may i help u sir ?")  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecmd():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 300
        r.pause_threshold = 0.8
        audio = r.listen(source)
        

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language = 'en-in')# hi-In
        print(f"User said: {query}\n")
        

        

    except Exception as e:
        return "none"

    return query

def writefile(loc):
            file = open(f'{loc}','w')
            speak("What do you wanna write sir?")
            write=takecmd()
            file.write(write)
            speak("Sir do wanna write more content ?")
            cont=takecmd().lower()
            if 'no' in cont:
                file.close()
                speak("Data Writing finished....")
            elif 'yes' in cont:
                appendfile(loc)

def appendfile(loc):
            file = open(f'{loc}','a')
            speak("What do you wanna append sir?")
            write=takecmd()
            file.write(f"\n{write}")
            speak("Sir do wanna append more content ?")
            cont=takecmd().lower()
            if 'no' in cont:
                file.close()
                speak("Data Appending finished....")
            else:
                appendfile(loc)

def type(loc):
    speak("sir, do u wanna append or write ?")
    d=takecmd().lower()
    if 'write' in d:
        writefile(loc)

    elif 'append' in d:
        appendfile(loc)

    speak("Sir, typing done....")

def sendemail():

    speak("To whom you want to send the email tell me the name of the person, sir !")
    person=takecmd()

    speak("Sir, please tell me the mail id")
    inputid=takecmd().lower()
    speak("Sir, it is a gmail id , outlook id or yahoo id")
    mailtype=takecmd().lower()
    speak("Sir, Tell me the subject of this mail")
    sub=takecmd()

    if 'outlook' in mailtype:
        outerid='@outlook.in'
    elif 'yahoo' in mailtype:
        outerid='@yahoo.com'
    else:
        outerid='@gmail.com'

    # outerid='@gmail.com'
    compid=inputid+outerid
    id=compid.lower()
    id=id.replace(" ","")
    try:
        speak("what should i say ?")
        body=takecmd()
        to=id
        speak(f"Sir, the mail id is {to} is it correct ?")
        print(f"The mail is {to}")
        idcheck=takecmd().lower()
        if 'yes' in idcheck:
            speak(f"Sending email to {person}")
            kit.send_mail("gauravvirtualassistant@gmail.com", "gaurav@77", sub ,body, to)
            speak(f"Email sent... to Mr.{person}")
        else:
            sendemail()
            

    except Exception as e:

        speak("Sorry Mr. Gaurav I am not able to send this email.")

def search_contact_record():
    ''' This function is used to searches a specific contact record '''

    speak("Sir, Tell me the first name for searching contact record")

    search_name = takecmd().lower()
    rem_name = search_name[1:]
    first_char = search_name[0]
    search_name = first_char.upper() + rem_name
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            speak("Your Required Contact Record is ")
            print (line)
            speak(f"{line}")
            found=True
            break
    if  found == False:
        print("There's no contact Record in Phone Book with name = " + search_name )
        speak(f"sir, There's no contact Record in Phone Book with name {search_name}")

def input_fname():
    ''' Converts first letter of your name  to Upper case '''
    fname = input("Enter First name : ")
    rem_fname = fname[1:]
    first_char = fname[0]
    return first_char.upper() + rem_fname

def input_lname():
    ''' Converts first letter of  last name  to Upper case '''
    lname = input("Enter Last name : ")
    rem_lname = lname[1:]
    first_char = lname[0]
    return first_char.upper() + rem_lname

def enter_contact_record():
    speak("Sir, enter the details of your neew contact")
    first = input_fname()
    last = input_lname()
    phone = input('Enter Phone number : ')
    contact=(f"[ {first} {last} , {phone} ]\n")
    #contact = ("[" + first + " " + last + ", " + phone + "]\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    speak("Contact saved successfully .")
    print("This contact\n " + contact + "has been added successfully!")


#*****************************************************************************************************************
#*****************************************************************************************************************

if __name__ == "__main__":

    wishme()
    while True:
    

        query = takecmd().lower()

        if 'search' in query:
            speak("Searching...")
            query=query.replace("search","")
            kit.search(query)
            speak("Here are some results from the web")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            try:

                query=query.replace("wikipedia"," ")
                result=wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)

            except Exception as e:
                speak("There is no such data available on wikipedia...")

        elif 'open instagram' in query:
            speak("Opening instagram")
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("www.instagram.com")

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
            sendemail()          

        elif 'open youtube' in query:
            speak("Sir, what u wanna search on youtube ?")
            src=takecmd().lower()
            kit.playonyt(src)

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

        elif 'open my notes' in query:
            speak("sir, opening your notes")

            loc=str("C:\\Users\\Gaurav Dev\\Desktop\\Alexa\\alexadocx.txt")
            type(loc)

        elif 'whatsapp message' in query:
            try:
                speak("Sir, On which number u want to send msg")
                num=takecmd().lower()
                speak("What should I type sir ?")
                msg=takecmd().lower()
                
                kit.sendwhatmsg_instantly(f"+91{num}", msg , 25, browser="chrome")
                speak("Message sent successfully !")
                print("Successfully Sent!")
                
                
  
            except:
                speak("An Unexpected Error! occured !")
                print("An Unexpected Error!")

        elif 'to handwriting' in query:
            speak("Sir, what u want to write ?")
            txt=takecmd()
            kit.text_to_handwriting(txt)
            speak("Sir, check my directory .... ")

        elif 'weather' in query:
            speak("Sir, for which place u want weather information ?")
            city=takecmd().lower()
            try:
                if 'none' in city:
                    speak("Sir, there is not city was name None")
                    print("Sir, there is not city was name None")

                else:

                    akey="efa50213ecabbe77b9a4e7de9a5a62d7"
                    url=f"http://api.openweathermap.org/data/2.5/weather?appid={akey}&q={city}"

                    res=requests.get(url)
                    json_data=json.loads(res.text)

                    weather=json_data["weather"][0]["description"]
                    temp=json_data["main"]["temp"]
                    humid=json_data["main"]["humidity"]
                    windspeed=json_data["wind"]["speed"]
                    pressure=json_data["main"]["pressure"]

                    print(f"Todays {city} weather is {weather}")
                    print(f"Temperature is {int(temp-273.15)} degree celcius")
                    print(f"Humidity is {humid} percent")
                    print(f"Pressure is {pressure} hpa")
                    print(f"Wind Speed  is {'{:.2f}'.format(windspeed)}")

                    speak(f"Sir, Todays {city} weather is {weather}")
                    speak(f", Temperature is {int(temp-273.15)} degree celcius")
                    speak(f", Humidity is {humid} percent")
                    speak(f", Pressure is {pressure} hpa")
                    speak(f"and Wind Speed  is {'{:.2f}'.format(windspeed * 3.39)} kilometer per hour")
            except Exception as e:
                speak("Sir, U may be spelled it wrong")

        elif "phone book" in query or "contact" in query or "contacts" in query:
            file_name = "phonebook.txt"
            file1 = open(file_name, "a+")
            file1.close

            speak("Sir, what you wanna do ,  Display contacts , Add a new contact or  search for a contact ?")
            print("")
            print("Display Your Contacts Records")
            print("Add a New Contact Record")
            print("search your contacts")
            print("")
            choice = takecmd().lower()

            if "display" in choice or "show" in choice:
                file1 = open(file_name, "r+")
                file_contents = file1.read()
                if len(file_contents) == 0:
                    speak("Your phone book is empty")
                    print("Phone Book is empty")
                else:
                    speak("sir, Here are some result from your phone book")
                    print (file_contents)
                file1.close
            
            elif "add" in choice or "save" in choice:
                enter_contact_record()
                
            
            elif "search" in choice or "find" in choice:
                search_contact_record()
                
            else:
                speak("No option choosed")
                speak("Exiting from the phonebook")              
        
        elif "wake up" in query:
            speak("I am always there for u sir, what can i do for you ?")

        elif "sleep" in query:
            speak("Ok sir, going to sleep, whenever u need my assist u can call me ...")

        elif "hi" in query or "hello" in query :
            if "how are you" in query:
                speak("I am fine sir, what aboit you")

            else:
                speak("Hi sir !")

        elif 'quit' in query or 'goodbye' in query:
            if 'goodbye' in query :

                speak("Good Bye....")
                speak("Thank you for using me...")
                break
            elif 'quit' in query:
                speak("Quiting....")
                speak("Thank you for using me...")
                break
    
                    
                

            
            

                
            
           

