# core/speaker.py
from core.imports import engine,time

def speak(text,delay=0.05):
    
    engine.say(text)
    engine.startLoop(False) # Non-blocking loop

    
    # Print text letter by letter in terminal
    for char in text:
        print(char, end='', flush=True)  # flush=True ensures immediate display
        time.sleep(delay)
        engine.iterate()
    print()
    engine.endLoop() # finish speaking

    