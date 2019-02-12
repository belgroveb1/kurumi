#Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from boto.s3.connection import S3Connection

#Variables
Auth_Token = S3Connection(os.environ['BOT_TOKEN'])

bot_prefix = "#"
bot = command.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
	print("bot is ready")

@bot.event
async def on_message(message):
	if message.author.id != bot.user.id:
		await bot.say("TEST!")

bot.run(Auth_Token)
