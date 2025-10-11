from core.speaker import speak
from core.listener import listen
from modules.greetings import greet,tell_time

speak("Jarvis 2.0 initialized.")
greet() 

while True:
    command = listen()
    if command:
        if "stop" in command:
            speak("Goodbye Manan sir.")
            break
        elif "time" in command:
            tell_time()
        else:
            speak(f"You said: {command}")
