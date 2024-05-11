import discord
import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("BOT_KEY")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(bot_token)