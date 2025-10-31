from utils.mock_biosignals import MockBiosignalGenerator
from utils.bubble_processor import BubbleProcessor

def test_bubble_creation():
    """Test creating bubbles from mock biosignals"""
    
    print("=" * 60)
    print("EPHEMERAL BUBBLE DEMO")
    print("=" * 60)
    
    generator = MockBiosignalGenerator()
    processor = BubbleProcessor()
    
    # Scenario 1: Confused patient
    print("\nScenario 1: Patient confused about medication")
    print("-" * 60)
    confused_readings = generator.generate_batch("confused", count=15)
    confused_bubble = processor.create_bubble(confused_readings)
    
    print(f"Created bubble from {confused_bubble.num_readings} readings")
    print(f"Cognitive Load: {confused_bubble.cognitive_load}")
    print(f"Comprehension Score: {confused_bubble.comprehension_score}")
    
    if confused_bubble.comprehension_score < 0.5:
        print("ALERT: Patient confused! Nurse intervention needed.")
    
    # Scenario 2: Understanding patient
    print("\nScenario 2: After nurse provides visual aid")
    print("-" * 60)
    understanding_readings = generator.generate_batch("understanding", count=15)
    understanding_bubble = processor.create_bubble(understanding_readings)
    
    print(f"Created bubble from {understanding_bubble.num_readings} readings")
    print(f"Cognitive Load: {understanding_bubble.cognitive_load}")
    print(f"Comprehension Score: {understanding_bubble.comprehension_score}")
    
    if understanding_bubble.comprehension_score >= 0.7:
        print("SUCCESS: Patient understanding verified!")
    
    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)

if __name__ == "__main__":
    test_bubble_creation()
