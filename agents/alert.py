from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

alert_agent = Agent(
    name="alert_agent",
    port=8004,
    seed="alert_agent_seed_2025",
    endpoint=["http://localhost:8004/submit"]
)

fund_agent_if_low(alert_agent.wallet.address())

@alert_agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Alert Agent started: {alert_agent.address}")

if __name__ == "__main__":
    alert_agent.run()
