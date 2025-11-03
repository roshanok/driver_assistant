# gps_manager.py
from kivy.app import App
from kivy.clock import Clock
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission
    from plyer import gps

class GPSManager:
    def __init__(self, callback):
        self.callback = callback
        self.gps_started = False

    def start(self):
        if platform == 'android':
            request_permissions([
                Permission.ACCESS_FINE_LOCATION,
                Permission.ACCESS_COARSE_LOCATION
            ])
            gps.configure(on_location=self.on_location)
            gps.start(minTime=1000, minDistance=1)
            self.gps_started = True
        else:
            print("GPS simulation started for non-Android platform.")
            Clock.schedule_interval(self.mock_location, 2)

    def on_location(self, **kwargs):
        # Extract GPS data
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        speed = kwargs.get('speed', 0)  # Speed in m/s
        if speed is not None:
            speed_kmh = speed * 3.6
            self.callback(lat, lon, speed_kmh)

    def mock_location(self, dt):
        """Simulate location for testing on desktop."""
        from random import random
        lat, lon = 37.7749 + random()/100, -122.4194 + random()/100
        speed = 40 + random()*10
        self.callback(lat, lon, speed)
