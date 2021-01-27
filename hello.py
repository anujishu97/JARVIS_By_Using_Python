import pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
from datetime import date
from datetime import datetime
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #intall by pip install pyautogui
import uuid
import psutil #pip install psutill 
import pyjokes
query=""
list1=["Hi, I am anuj","How may can I help you"]
myself=["tell me your name"]
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def gen_table():
    engine.say("Please enter the number to generate the table")
    engine.runAndWait()
    
    num=int(input(""))
    for i in range(1,11):
        table=num*i
        speak(table)

def greet():
   for i in range(len(myself)):
       speak(myself[i])
   user_name=takecommand()
   name="Hi " + user_name 
   speak(name)
   speak("How are you?")

def start():
    for i in range(len(list1)):
        speak(list1[i])
    input_user()

def cur_date():
    today = date.today()
    speak(today)

def cur_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(current_time)


def wiki(user_input1):
    speak("searching.....")
    user_input1=user_input1.replace("wikipedia","")
    result=wikipedia.summary(user_input1,sentences=2)
    print(result)
    speak(result)

def send_email(to,content):
    speak("Sending...")
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kanuj8840@gmail.com','alwaysbehappy')
    server.sendmail('kanuj8840@gmail.com',to,content)
    server.close()

def chrome_search():
    speak("What do you want to search")
    chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    user_query=takecommand().lower()
    wb.get(chromepath).open_new_tab(user_query)

def screenshots():
    img=pyautogui.screenshot()
    current_time = datetime.now()  
    val=str(current_time.second*10+100)
    img.save("E:\\Python Chatbot\\Screenshots\\"+val+".png")

def cpu():
    cpu_usage=str(psutil.cpu_percent())
    speak("CPU is at "+cpu_usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    joke=pyjokes.get_joke()
    print(joke)
    speak(joke)

def input_user():
    user_input=takecommand().lower()
    if 'table' in user_input:
        gen_table()
    elif 'greeting' in user_input:
        greet()
    elif 'date' in user_input:
        cur_date()
    elif ('time' in user_input or 'current time' in user_input):
        cur_time()
    elif ('stop' in user_input or 'go offline' in user_input):
        speak("hmm...... okay")
        speak("Thanks,Nice to meet you")
        exit()
    elif ('search' in user_input or 'wikipedia' in user_input or 'what do you know' in user_input or 'what is' in user_input or 'which is' in user_input or 'what are the ' in user_input or 'who is ' in user_input):
        wiki(user_input)
    elif('send email' in user_input or 'send mail' in user_input):
        try:
            speak("Enter your recipient's e-mail-id")
            to=input("to send:")
            speak("What do you want to send? Please enter your message")
            content=input("Message:")
            send_email(to,content)
            speak("E-mail has been send successfully")
        except Exception as e:
            print(e)
            speak("Unable to send mail.")
    elif 'logout' in user_input:
        os.system("shutdown -1")
    elif 'shutdown' in user_input:
        os.system("shutdown /s /t 1")
    elif 'restart' in user_input:
        os.system("shutdown /r /t 1")
    elif('remember that' in user_input or 'remember' in user_input):
        speak("What shouldI remember")
        data=takecommand()
        speak("You said me to remember" +data)
        remember=open('data.txt','w')
        remember.write(data)
        remember.close()
    elif('remember anything' in user_input or 'you know' in user_input):
        remember=open('data.txt','r')
        speak("You said me to remember that "+remember.read())
        remember.close()  
    elif 'screenshot' in user_input:
        screenshots()
        speak("Done!")
    elif 'cpu' in user_input:
        cpu()
    elif 'joke' in user_input:
        jokes()
    else:
        engine.say("Sorry I did not understand")
        engine.runAndWait()


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recoginizning...")
        query=r.recognize_google(audio,language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Please try again")
        return "None"
    return query
if __name__=="__main__":
    while True:
        start()
#input_user()