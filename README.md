# J.A.R.V.I.S 2.0 — Your Personal AI Desktop Assistant

J.A.R.V.I.S 2.0 (Just A Rather Very Intelligent System) is a Python-based AI assistant designed to perform a variety of desktop tasks using voice commands.
From controlling system operations and playing music to sending WhatsApp messages and switching between apps — JARVIS is your own Iron Man-inspired productivity partner ⚙️💬

## 🚀 Features
1) 🎙️ Voice Interaction

2) Always-on voice assistant powered by speech_recognition and pyttsx3

3) Listens to your commands and responds naturally

4) Smart error handling — Jarvis politely asks you to repeat if it doesn’t hear clearly

## 💻 System Control

1) Shutdown / Restart / Sleep your PC with a single voice command

2) Switch windows or apps (e.g. “Switch to Chrome”)

3) Take screenshots (automatically saved to Desktop)

4) Change volume (increase, decrease, mute, unmute)

### 🧩 Example Commands:

Jarvis, shutdown the system  
Jarvis, switch to Notepad  
Jarvis, take a screenshot  
Jarvis, increase the volume  

## 🎵 Entertainment (Spotify Integration)

1) Search and play any song on Spotify using your voice

2) Uses the official Spotify Web API and opens the song in your browser

### Example:

Jarvis, play Shape of You on Spotify
## 💬 Messaging (WhatsApp Integration)

1) Send WhatsApp messages using pywhatkit

2) Supports scheduled or instant sending

3) Detects contact names and asks for message content

### Example:

Jarvis, send a message to Ivan  
Jarvis, message Mom saying I’ll call later

## ⏰ Time & Greetings

1) Greets you according to the time of day

2) Tells the current time

### Example:

Jarvis, what’s the time?  
Jarvis, good morning

## 🧩 Project Structure
JARVIS 2.0/
│
├── core/

│   ├── imports.py          # All common imports and initializations

│   ├── listener.py         # Handles microphone input and speech recognition

│   └── speaker.py          # Text-to-speech module
│
├── modules/

│   ├── greetings.py        # Greet and tell_time functions

│   ├── system_control.py   # System actions: shutdown, restart, screenshot, volume

│   ├── entertainment.py    # Spotify song playback

│   └── messaging.py        # WhatsApp messaging with pywhatkit
│
├── main.py                 # The core brain of Jarvis

└── README.md               # Project documentation

## How It Works

1) Jarvis starts with:

Jarvis 2.0 initialized.


2) It greets based on the current time.

3) It listens for your voice command → processes → performs the action.

4) After each command, it keeps listening for more until you tell it to sleep.

## ⚙️ Installation

### Clone this repository:

git clone https://github.com/<your-username>/JARVIS-2.0.git
cd JARVIS-2.0


### Install dependencies:

pip install -r requirements.txt


### Or manually:

pip install pyttsx3 speechrecognition spotipy pyautogui pygetwindow pywhatkit pillow


### Spotify Setup:

1) Go to Spotify Developer Dashboard

2) Create an app and note down your Client ID and Client Secret

3) Set redirect URI: http://127.0.0.1:8888/callback

4) Add them to your entertainment.py config

5) Run JARVIS:

6) python main.py

## 🧩 Example Conversation

🧠 You: Jarvis, what’s the time?
💻 JARVIS: It’s 5:42 PM, sir.

🧠 You: Jarvis, play Believer on Spotify.
💻 JARVIS: Playing Believer on Spotify.

🧠 You: Jarvis, take a screenshot.
💻 JARVIS: Screenshot will be taken in next 5 seconds.

🧠 You: Jarvis, send a message to Mom.
💻 JARVIS: What should I say to Mom?

## 🛠️ Technologies Used
Feature	Library
Speech Recognition	speech_recognition
Text-to-Speech	pyttsx3
Spotify Playback	spotipy
GUI Automation	pyautogui
WhatsApp Messaging	pywhatkit
Window Management	pygetwindow
Screenshot Handling	Pillow
## ⚡ Future Improvements


🤖 ChatGPT Integration for general Q&A

🧱 GUI Dashboard for manual control

🌐 Browser automation (Google search, YouTube control)

🏠 Smart home control via IoT

👨‍💻 Author

## 🤝 Open Source Contributions

This project is open to pull requests and contributions.
I’m actively maintaining and expanding J.A.R.V.I.S — and I’d love to see your ideas!

### If you’d like to contribute:

1) Fork this repository

2) Create a new branch for your feature or fix

3) Submit a pull request — I’ll review it personally!

💡 All meaningful and creative contributions are welcome — from code improvements to new features.

# 🧑‍💻 Developer

## 👤 Manan Dudeja
B.Tech CSE Core @ VIT Chennai
Building JARVIS 2.0 — a modular AI assistant integrated with Smart Desk automation.


## 🏁 License

This project is open-source under the MIT License.
