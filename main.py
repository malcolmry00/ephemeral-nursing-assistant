from uagents import Bureau
from agents.coordinator import coordinator
from agents.bubble_analyzer import bubble_analyzer
from agents.verifier import verifier
from agents.alert import alert_agent
from agents.learning import learning_agent

bureau = Bureau()
bureau.add(coordinator)
bureau.add(bubble_analyzer)
bureau.add(verifier)
bureau.add(alert_agent)
bureau.add(learning_agent)

if __name__ == "__main__":
    print("=" * 60)
    print("STARTING ALL AGENTS")
    print("=" * 60)
    bureau.run()
