from core.imports import requests,time
from core.speaker import speak
from pushbullet import Pushbullet
# Replace with your Pushbullet API key
API_KEY = ""
pb = Pushbullet(API_KEY)
def lock_phone():
    data = {
        "type": "note",
        "title": "lock_phone",
        "body": "Locking phone via Jarvis"
    }
    response = requests.post(
        "https://api.pushbullet.com/v2/pushes",
        json=data,
        headers={"Access-Token": API_KEY, "Content-Type": "application/json"}
    )
    if response.status_code == 200:
        print("Lock command sent successfully.")
    else:
        print("Failed to send lock command:", response.text)

