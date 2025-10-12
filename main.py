from core.speaker import speak
from core.listener import listen
from modules.greetings import greet,tell_time
from modules.system_control import sleep
#from core.imports import spotipy,SpotifyOAuth
from modules.entertainment import spotify

speak("Jarvis 2.0 initialized.")
greet() 

while True:
    command = listen()
    if command:
        if "sleep" in command:
            sleep()
        elif "time" in command:
            tell_time()
        elif "spotify" in command:
            speak('What song would you like to play, sir?')
            command = listen()
            spotify(command)
        else:
            speak(f"You said: {command}")
