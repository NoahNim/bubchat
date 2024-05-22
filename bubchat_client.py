import discord
import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("BOT_KEY")
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    
bot.run(bot_token)