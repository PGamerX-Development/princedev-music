import discord
from discord.ext import commands
import os

token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=">")

bot.load_extension("cogs.music")

bot.run(token)