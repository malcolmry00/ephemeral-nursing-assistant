from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

verifier = Agent(
    name="verifier",
    port=8003,
    seed="verifier_seed_2025",
    endpoint=["http://localhost:8003/submit"]
)

fund_agent_if_low(verifier.wallet.address())

@verifier.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Verifier started: {verifier.address}")
    ctx.logger.info("Comprehension threshold: 0.7")

if __name__ == "__main__":
    verifier.run()
