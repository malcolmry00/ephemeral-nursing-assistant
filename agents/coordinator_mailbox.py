from uagents import Agent, Context, Protocol, Model

class ChatMessage(Model):
    message: str

coordinator = Agent(
    name="coordinator",
    seed="coordinator_seed_phrase_2025",
    mailbox=True,
    port=8000
)

chat_protocol = Protocol("Chat")

@chat_protocol.on_message(model=ChatMessage)
async def handle_chat(ctx: Context, sender: str, msg: ChatMessage):
    ctx.logger.info(f"Chat query: {msg.message}")
    response = ChatMessage(message="Ephemeral Bubble Nursing Assistant ready!")
    await ctx.send(sender, response)

coordinator.include(chat_protocol)

@coordinator.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Coordinator: {coordinator.address}")

if __name__ == "__main__":
    coordinator.run()
