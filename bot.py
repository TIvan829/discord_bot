import json
import os

import discord
from discord.ext import commands

with open("config.json", "r", encoding="UTF-8") as file:
    data = json.load(file)
TOKEN = data["token"]

bot = commands.Bot(help_command=None, intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f">>{bot.user}上線<<")
    while True:
        game = discord.Game("機器人製作中")
        await bot.change_presence(status=discord.Status.online, activity=game)


bot.run(TOKEN)
