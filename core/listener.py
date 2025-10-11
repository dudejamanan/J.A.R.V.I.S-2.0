# core/listener.py
from core.imports import recognizer
from core.speaker import speak
import speech_recognition as sr

def listen(timeout=3, phrase_time_limit=5):
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return None

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return None
    except sr.RequestError:
        speak("Network error. Please check your internet.")
        return None
