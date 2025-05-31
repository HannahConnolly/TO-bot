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

@tasks.loop(seconds=60)
async def checkTime():
    now = datetime.now()
    if now.weekday() == 6 and 12 <= now.hour < 13:  # Sunday between 12:00 and 13:59
        print("It's Sunday around noon!")
    #     await pingusers()

async def ping_tos_to_post_registration():
    # Replace 'to-role-id' with the actual role ID of the TOs
    to_role_id = 123456789012345678  # TODO: set your TO role ID here
    # Replace 'channel-id' with the actual channel ID where you want to send the message
    channel_id = 123456789012345678  # TODO: set your channel ID here

    channel = bot.get_channel(channel_id)
    if channel:
        mention = f"<@&{to_role_id}>"
        await channel.send(f"{mention} Please post the registration link and info for this week's tournament!")
    else:
        print("Channel not found. Check your channel ID.")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    checkTime.start()

if __name__ == "__main__":
    print("hello world")
    bot.run(TOKEN)