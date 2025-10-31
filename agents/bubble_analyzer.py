from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

bubble_analyzer = Agent(
    name="bubble_analyzer",
    port=8002,
    seed="bubble_analyzer_seed_2025",
    endpoint=["http://localhost:8002/submit"]
)

fund_agent_if_low(bubble_analyzer.wallet.address())

@bubble_analyzer.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Bubble Analyzer started: {bubble_analyzer.address}")

if __name__ == "__main__":
    bubble_analyzer.run()
