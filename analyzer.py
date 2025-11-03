from driver_assistant.config import SPEED_LIMIT

def detect_anomaly(speed, last_speed):
    """Return anomaly type if detected."""
    if speed > SPEED_LIMIT:
        return "speeding"
    if last_speed and abs(speed - last_speed) > 25:
        return "harsh_change"
    return None
