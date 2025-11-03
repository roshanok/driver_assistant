from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

from gps_manager import GPSManager
from audio_manager import AudioManager
from speed_monitor import SpeedMonitor

class DriverAssistantApp(App):
    def build(self):
        self.label = Label(text="Initializing GPS...", font_size='20sp')
        self.audio = AudioManager()
        self.speed_monitor = SpeedMonitor(limit=80, callback=self.audio.speak)
        self.gps_manager = GPSManager(self.on_gps_update)
        Clock.schedule_once(lambda dt: self.gps_manager.start(), 1)
        return self.label

    def on_gps_update(self, lat, lon, speed):
        self.label.text = f"Lat: {lat:.4f}\nLon: {lon:.4f}\nSpeed: {speed:.1f} km/h"
        self.speed_monitor.update_speed(speed)

if __name__ == "__main__":
    DriverAssistantApp().run()
