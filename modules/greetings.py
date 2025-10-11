from core.speaker import speak
from time import strftime

def greet():
    speak(f'''Good Morning Sir, 
Its {strftime('%I:%M %p')} 
You are late for work as usual ''')
    
def tell_time():
    speak(f'''The time is {strftime('%I:%M %p')}''')