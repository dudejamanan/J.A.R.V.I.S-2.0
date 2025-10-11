Jarvis 2.0 – Modular AI Voice Assistant
Jarvis 2.0 is a Python-based modular AI voice assistant that listens, responds, and executes commands. It’s designed for extensibility and provides a real-time letter-by-letter display of spoken text in the terminal.

🚀 Features

Voice commands and speech recognition (online and offline ready)

Letter-by-letter terminal display while speaking

Greet users and tell the current time

Open websites and apps with simple voice commands

Modular design for easy feature expansion

Cross-platform support (Windows/Linux/macOS)

📁 Folder Structure
JARVIS 2.0/
│
├─ main.py                # Main program
├─ core/                  # Core modules
│   ├─ imports.py         # Shared imports and objects
│   ├─ speaker.py         # TTS with letter-by-letter display
│   └─ listener.py        # Speech recognition listener
└─ modules/               # User-defined features
    └─ functions.py       # Custom commands (time, greet, open apps)

⚡ Installation

1. Clone the repository:

git clone https://github.com/yourusername/Jarvis-2.0.git

cd Jarvis-2.0

2. Create a virtual environment:

python -m venv venv

3. Activate the virtual environment:

Windows:

venv\Scripts\activate


Linux/macOS:

source venv/bin/activate

4. Install dependencies:

pip install -r requirements.txt

🏃 Usage

Run Jarvis:

python main.py

Jarvis will initialize and greet the user.

Listens for commands like:

"time" → tells current time

"youtube" → opens YouTube

"stop" → exits Jarvis

Spoken text appears letter-by-letter in the terminal simultaneously.

✨ Adding New Features

1. Open modules/functions.py.

2. Add a new function:

from core.speaker import speak

def tell_joke():
    speak("Why did the programmer quit his job? Because he didn't get arrays!")

3. Import in main.py and call it based on user commands:

from modules.functions import tell_joke

if "joke" in command:
    tell_joke()

🛠 Requirements

Python >= 3.12

Libraries:

pyttsx3

SpeechRecognition

pyaudio (for microphone input)

time, sys, webbrowser (built-in)

💡 Best Practices

Do not push venv to GitHub (use .gitignore).

Keep core functionality in core/ and custom commands in modules/.

Use letter-by-letter speak() for a more interactive experience.

👥 Contributors

Manan Dudeja – Project Creator & Developer

Open for contributions! Submit pull requests or report issues.

📄 License

This project is open-source and free to use under the MIT License.
