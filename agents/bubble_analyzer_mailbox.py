from uagents import Agent, Context

bubble_analyzer = Agent(
    name="bubble_analyzer",
    seed="bubble_analyzer_seed_2025",
    mailbox=True,
    port=8002
)

@bubble_analyzer.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Bubble Analyzer: {bubble_analyzer.address}")

if __name__ == "__main__":
    bubble_analyzer.run()
