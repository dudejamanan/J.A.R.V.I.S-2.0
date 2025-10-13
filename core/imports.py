# core/imports.py
import speech_recognition as sr
import pyttsx3
import sys
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import os
import pyautogui
import pygetwindow as gw
from time import strftime
import pywhatkit
import datetime

engine = pyttsx3.init('sapi5')

# Set voice properties
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)          # Speed of speech
engine.setProperty('voice', voices[0].id) # 0 = male, 1 = female

# Initialize recognizer once
recognizer = sr.Recognizer()

# Optional: print voice info
print(f"Using voice: {voices[0].id}")

# Expose commonly used objects
__all__ = ['sr', 'pyttsx3', 'sys', 'engine', 'recognizer']
