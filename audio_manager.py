# audio_manager.py
import pyttsx3

class AudioManager:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.last_alert = None

    def speak(self, text):
        print(f"[Audio Alert]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
