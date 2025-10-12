from core.speaker import speak
from core.listener import listen
from modules.greetings import greet,tell_time
from modules.system_control import sleep,shutdown,restart,switch_window,switch_to_app,screenshot
from modules.entertainment import spotify

speak("Jarvis 2.0 initialized.")
#greet() 

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
        elif "shutdown" in command:
            shutdown()
        elif "restart" in command:
            restart()
        elif "switch window" in command:
            switch_window()
        elif "switch to" in command:
            app_name = command.replace("switch to", "").strip()
            switch_to_app(app_name)
        elif "screenshot" in command:
            screenshot()
        else:
            speak(f"You said: {command}")
