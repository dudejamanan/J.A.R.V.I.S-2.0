from core.speaker import speak
from core.imports import sys,os,time,pyautogui,gw,strftime
from core.listener import listen

def sleep():
    speak("Alright baby i am going bye. muahhh")
    sys.exit()

def shutdown():
    speak("System will shut down in 10 seconds. Say 'cancel' to stop.")
    for i in range(10, 0, -1):
        command = listen()
        print(f"Shutting down in {i} seconds...")
        time.sleep(1)
        try:
            
            if "cancel" in command:
                speak("Shutdown Terminated.")
                break
            else:
                os.system("shutdown /s /t 5")
                
        except Exception as e:
                os.system("shutdown /s /t 5")
                #/s shuts down the system
                #/t 5 delays the shutdown by 5 seconds
def restart():
    speak("System will restart in 10 seconds. Say 'cancel' to stop.")
    for i in range(10, 0, -1):
        command = listen()
        print(f"Restarting in {i} seconds...")
        time.sleep(1)
        try:
            
            if "cancel" in command:
                speak("Restart Terminated.")
                break
            else:
                os.system("shutdown /r /t 5")
        
        except Exception as e:
                os.system("shutdown /r /t 5")
def switch_window():
    pyautogui.keyDown("alt") #alt dbaya
    pyautogui.press("tab") #tab press kra
    pyautogui.keyUp("alt") #alt chorda
    # you can directly use pyautogui.hotkey("alt","tab")
def switch_to_app(app_name):
    windows = gw.getWindowsWithTitle(app_name) #returns a list of all windows whose title contains the string app_name.
    if windows:
        try:
            win = windows[0] #picks the most relevant one
            if win.isMinimized:
                win.restore()
                time.sleep(0.5)
            win.activate() #brings the window to the foreground (focuses it).
            speak(f"Switched to {app_name}")
        except Exception as e:
            speak(f"Couldn't directly switch to {app_name}. Trying alt tab method.")
            pyautogui.hotkey("alt","tab") #used to press two keys simultaneously

    else:
        speak(f"I couldn’t find any window named {app_name}, sir.")

def screenshot():
    speak("Screenshot will be taken in next 5 seconds")
    time.sleep(5)
    img=pyautogui.screenshot()
    filename= f"Screenshot {strftime('%Y-%m-%d %H-%M-%S')}.png" #save as (Screenshot year/month/date hours:minutes:seconds)
    desktop_path = os.path.join(os.path.expanduser("~"),"Desktop") #os.path.expanduser("~") → gives your home directory (e.g., C:\Users\Manan)
    #os.path.join joins my home directory and desktop 
    full_path = os.path.join(desktop_path,filename)
    #os.path.join joins my desktop path and file like - C:\Users\Manan\Desktop\Screenshot 2025-10-12 18-05-32.png
    img.save(full_path)
    speak(f"Screenshot saved on Desktop:{full_path}")

def increase_volume():
        for i in range(15):
            pyautogui.press("volumeup")
            time.sleep(0.1)

        speak("volume increased sir")
def decrease_volume():
        for i in range(15):
            pyautogui.press("volumedown")
            time.sleep(0.2)

        speak("volume decreased sir")
def mute_volume():
    pyautogui.press("volumemute")
    speak("muted volume sir")
def type():
     speak("Voice mode activated. Say 'stop typing' to exit.")
     while True:
          query=listen(timeout=6,phrase_time_limit=10)
          if query:
               if 'stop typing' in query:
                    speak("Voice mode deactivated.")
                    break
               else:
                    pyautogui.typewrite(query+" ")
          else :
               continue #if silent for some time , continue waiting
def open_notepad():
     notepad_path = "C:\\Windows\\system32\\notepad.exe"
     os.startfile(notepad_path)
def close_notepad():
     speak("okay sir closing notepad")
     os.system("taskkill /f /im notepad.exe")
     #taskkill is a windows command used to terminate tasks
     #/f flag forces the termination of tasks
     #/im specifies the image name (in this case notepad.exe)
def save():
     pyautogui.hotkey('ctrl','s')
def copy():
     pyautogui.hotkey('ctrl','c')
def paste():
     pyautogui.hotkey('ctrl','v')
def enter():
     pyautogui.press('enter')
def open_cmd():
     os.system("start cmd")
def close_cmd():
     os.system("taskkill /f /im cmd.exe")