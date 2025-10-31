from uagents import Bureau
from agents.coordinator import coordinator
from agents.bubble_analyzer import bubble_analyzer
from agents.verifier import verifier
from agents.alert import alert_agent
from agents.learning import learning_agent
from agents.patient_profile import patient_profile

bureau = Bureau()
bureau.add(coordinator)
bureau.add(bubble_analyzer)
bureau.add(verifier)
bureau.add(alert_agent)
bureau.add(learning_agent)
bureau.add(patient_profile)

if __name__ == "__main__":
    print("=" * 60)
    print("STARTING ALL AGENTS")
    print("=" * 60)
    bureau.run()
