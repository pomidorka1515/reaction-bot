import discord
import random
import time
from discord.ext import commands
import json

DEBUG = True

try:
    with open("/var/www/bot/config.json", "r", encoding='utf-8') as f:
        T = json.load(f)
except Exception as e:
    print(f"config file load error: {e}")

intents = discord.Intents.all()
intents.message_content = True
intents.messages = True
intents.guilds = True

client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.id in T['blacklist']:
        return
    words = message.content.lower().split()
    for i, v in T['reactions'].items():
        if i in words:
            mojhi = 0
            if isinstance(v, int):
                mohji = v
            elif isinstance(v, list):
                mohji = random.choice(v)
            elif isinstance(v, str):
                mohji = v
            else:
                raise Exception(f"invalid emoji for '{i}', not: int, list or str")
            if not isinstance(v, str):
                emoji = client.get_emoji(mohji)
            await message.add_reaction(emoji if not isinstance(v, str) else mohji)
            if DEBUG: print(f"reacted to keyword {i} from {message.author.name}")

client.run(T['token'])
