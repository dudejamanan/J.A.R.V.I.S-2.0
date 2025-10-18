from core.speaker import speak
from core.imports import webbrowser,datetime,pywhatkit,genai
from core.listener import listen
import requests

def monkey_type():
    webbrowser.open("www.monkeytype.com")

def whatsapp():
    speak("who would you like to message. Sir?")
    name = listen()
    contacts = {
        "myself":"+918595115309",
        "manav":"+919667787672",
        "mamma":"+919211331615"
    }
    if name not in contacts:
        speak(f"I dont have any {name} saved in my memory")
        return 
    speak(f"what should i say to {name}?")
    message = listen()
    if not message:
        speak("I didnt not hear properly")
        return
    #get current time
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute+1
    try:
        speak(f"sending your message to {name} in a few seconds.")
        pywhatkit.sendwhatmsg(contacts[name],message,hour,minute)
        speak("message has been sent successfully.")
    except Exception as e:
        speak("Sorry, i coundn't send the message")
        print(e)

