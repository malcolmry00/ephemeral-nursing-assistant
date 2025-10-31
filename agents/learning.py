from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

learning_agent = Agent(
    name="learning_agent",
    port=8005,
    seed="learning_agent_seed_2025",
    endpoint=["http://localhost:8005/submit"]
)

fund_agent_if_low(learning_agent.wallet.address())

@learning_agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Learning Agent started: {learning_agent.address}")

if __name__ == "__main__":
    learning_agent.run()
