from uagents import Model
from typing import List

class EphemeralBubble(Model):
    """Ephemeral bubble - exists 5-30 seconds"""
    bubble_id: str
    timestamp: float
    duration: float  # seconds
    cognitive_load: float  # 0-1
    comprehension_score: float  # 0-1
    attention_level: float  # 0-1
    num_readings: int
