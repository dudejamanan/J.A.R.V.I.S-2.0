from core.speaker import speak
from time import strftime
import pygame
import threading
def greet():
    speak(f'''Good Morning Sir, 
Its {strftime('%I:%M %p')} 
You are late for work as usual ''')
    
def tell_time():
    speak(f'''The time is {strftime('%I:%M %p')}''')
def system_start():
    def play():
        pygame.mixer.init()
        pygame.mixer.music.load("assets/jarvis_start.mp3")
        pygame.mixer.music.play()
    threading.Thread(target=play,daemon=True).start()