# speed_monitor.py
class SpeedMonitor:
    def __init__(self, limit=80, callback=None):
        self.limit = limit
        self.callback = callback
        self.over_limit_warned = False

    def update_speed(self, speed):
        if speed > self.limit and not self.over_limit_warned:
            self.over_limit_warned = True
            if self.callback:
                self.callback(f"Speed {int(speed)} km/h — please slow down.")
        elif speed < self.limit - 5:
            self.over_limit_warned = False
