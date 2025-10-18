from core.speaker import speak
from core.listener import listen
from modules.greetings import greet, tell_time,system_start
from modules.system_control import sleep, shutdown, restart, switch_window, switch_to_app, screenshot, increase_volume, decrease_volume, mute_volume,type,open_notepad,close_notepad,save,copy,paste,enter,open_cmd,close_cmd,select_all,backspace,open_anything
from modules.entertainment import spotify
from modules.web_utilities import monkey_type,whatsapp
import time
from modules.pushbullet_actions import lock_phone
#system_start()
#speak("Jarvis 2.0 initialized.")
#greet()

wake_word = "jarvis"
active = False
last_command_time = 0
active_timeout = 20  # seconds Jarvis stays active after last command

while True:
    if not active:
        print("Waiting for wake word...")
        query = listen(timeout=5, phrase_time_limit=4)
        if query and wake_word in query:
            speak("Yes sir, I'm listening.")
            active = True
            last_command_time = time.time()
    else:
        # Check if Jarvis should stay active
        if time.time() - last_command_time > active_timeout:
            speak("Going to sleep mode, sir.")
            active = False
            continue

        command = listen(timeout=5, phrase_time_limit=7)

        if not command:
            # If no command heard, just loop again (don’t deactivate yet)
            continue

        last_command_time = time.time()  # reset timer on valid command

        # --- COMMAND HANDLERS ---
        if "sleep" in command:
            sleep()
        elif "time" in command:
            tell_time()
        elif "spotify" in command:
            speak('What song would you like to play, sir?')
            song = listen()
            if song:
                spotify(song)
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
        elif "increase volume" in command:
            increase_volume()
        elif "decrease volume" in command:
            decrease_volume()
        elif "mute" in command:
            mute_volume()
        elif "type" in command:
            type()
        elif "open notepad" in command:
            open_notepad()
        elif "close notepad" in command:
            close_notepad()
        elif "open cmd" in command:
            open_cmd()
        elif "close cmd" in command:
            close_cmd()
        elif "copy" in command:
            copy()
        elif "paste" in command:
            paste()
        elif "save" in command:
            save()
        elif "enter" in command:
            enter()
        elif "select all" in command:
            select_all()
        elif "backspace" in command:
            backspace()
        elif "monkey" in command:
            monkey_type()
        elif "open" in command:
            open_anything(command)
        elif "whatsapp" in command:
            whatsapp()
            enter()
        elif "lock my phone" in command:
            speak("Locking your phone, sir.")
            lock_phone()    
        else:
            speak(f"You said: {command}")
            