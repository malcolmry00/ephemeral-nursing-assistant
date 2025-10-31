from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

patient_profile = Agent(
    name="patient_profile",
    port=8006,
    seed="patient_profile_seed_2025",
    endpoint=["http://localhost:8006/submit"]
)

fund_agent_if_low(patient_profile.wallet.address())

@patient_profile.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Patient Profile Agent started: {patient_profile.address}")
    ctx.logger.info("Storing patient preferences and learning patterns")

if __name__ == "__main__":
    patient_profile.run()