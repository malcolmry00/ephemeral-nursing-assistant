import os
from pathlib import Path

# Create mailbox versions of all agents
agents_code = {
    'coordinator_mailbox.py': '''from uagents import Agent, Context, Protocol, Model

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
''',
    'bubble_analyzer_mailbox.py': '''from uagents import Agent, Context

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
'''
}

for filename, code in agents_code.items():
    with open(f'agents/{filename}', 'w', encoding='utf-8') as f:
        f.write(code)

print("Created mailbox agents!")
print("Run: python agents/coordinator_mailbox.py")