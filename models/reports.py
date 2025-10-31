from uagents import Model

class ComprehensionReport(Model):
    """Report on patient comprehension"""
    patient_id: str
    timestamp: float
    comprehension_score: float
    cognitive_load: float
    alert_triggered: bool
    recommendation: str
