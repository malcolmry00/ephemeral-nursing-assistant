from uagents import Model
from typing import Optional

class BiosignalReading(Model):
    """Single biosignal reading from patient device"""
    timestamp: float
    pupil_diameter: float  # mm, 2-8 range
    heart_rate_variability: float  # ms, RMSSD
    galvanic_skin_response: float  # microsiemens
    facial_tension: Optional[float] = None  # 0-1 scale
