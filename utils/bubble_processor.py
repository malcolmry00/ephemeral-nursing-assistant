import time
import hashlib
from typing import List
from models.biosignals import BiosignalReading
from models.bubbles import EphemeralBubble

class BubbleProcessor:
    """Process biosignals into ephemeral bubbles"""
    
    def create_bubble(self, readings: List[BiosignalReading]) -> EphemeralBubble:
        """Create bubble from biosignal batch"""
        
        if not readings:
            raise ValueError("Need readings to create bubble")
        
        # Calculate averages
        avg_pupil = sum(r.pupil_diameter for r in readings) / len(readings)
        avg_hrv = sum(r.heart_rate_variability for r in readings) / len(readings)
        avg_gsr = sum(r.galvanic_skin_response for r in readings) / len(readings)
        
        # Normalize to 0-1 scale
        pupil_norm = (avg_pupil - 2.0) / 6.0  # 2-8mm range
        hrv_norm = 1.0 - (avg_hrv / 100.0)  # Inverse: low HRV = high load
        gsr_norm = avg_gsr / 15.0  # 0-15 microsiemens range
        
        # Calculate cognitive load (weighted average)
        cognitive_load = (
            pupil_norm * 0.4 +
            hrv_norm * 0.3 +
            gsr_norm * 0.3
        )
        
        # Calculate comprehension score
        # High cognitive load = low comprehension
        base_comprehension = 1.0 - cognitive_load
        
        # Attention level (simplified)
        attention = 1.0 - (pupil_norm * 0.5)
        
        # Final comprehension score
        comprehension = (base_comprehension * 0.7) + (attention * 0.3)
        comprehension = max(0.0, min(1.0, comprehension))
        
        # Generate bubble ID
        bubble_id = hashlib.md5(
            f"{readings[0].timestamp}".encode()
        ).hexdigest()[:8]
        
        return EphemeralBubble(
            bubble_id=bubble_id,
            timestamp=readings[0].timestamp,
            duration=readings[-1].timestamp - readings[0].timestamp,
            cognitive_load=round(cognitive_load, 2),
            comprehension_score=round(comprehension, 2),
            attention_level=round(attention, 2),
            num_readings=len(readings)
        )
