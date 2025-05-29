import discord, os
from datetime import datetime
from discord.ext import commands, tasks
# from replit import db
from random import choice
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@tasks.loop(seconds=1)
async def checkTime():
    print("Checking time...")
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # if current_time == db["time"]:
    #     await pingusers()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    checkTime.start()

if __name__ == "__main__":
    print("hello world")
    bot.run(TOKEN)