import random
import time
from models.biosignals import BiosignalReading

class MockBiosignalGenerator:
    """Generate mock biosignals for demo"""
    
    def generate_confused_reading(self) -> BiosignalReading:
        """Simulate confused patient - high cognitive load"""
        return BiosignalReading(
            timestamp=time.time(),
            pupil_diameter=random.uniform(6.5, 7.8),  # Dilated (stressed)
            heart_rate_variability=random.uniform(20, 35),  # Low HRV (stressed)
            galvanic_skin_response=random.uniform(8, 12),  # High GSR (anxious)
            facial_tension=random.uniform(0.7, 0.9)
        )
    
    def generate_understanding_reading(self) -> BiosignalReading:
        """Simulate understanding patient - low cognitive load"""
        return BiosignalReading(
            timestamp=time.time(),
            pupil_diameter=random.uniform(3.5, 4.5),  # Normal
            heart_rate_variability=random.uniform(60, 80),  # High HRV (calm)
            galvanic_skin_response=random.uniform(2, 4),  # Low GSR (relaxed)
            facial_tension=random.uniform(0.1, 0.3)
        )
    
    def generate_batch(self, state: str, count: int = 15):
        """Generate batch of readings"""
        readings = []
        for _ in range(count):
            if state == "confused":
                readings.append(self.generate_confused_reading())
            else:
                readings.append(self.generate_understanding_reading())
            time.sleep(0.1)  # Small delay
        return readings
