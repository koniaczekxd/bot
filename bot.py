import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
Client=discord.Client
client=commands.Bot(command_prefix="!")

@client.event
async def on_ready():
	print('Ready boy')
@client.event
async def on_message(message):
  if message.content.startswith('!bait'):
   channel = message.channel
   await channel.send(time.strftime('Hello World'))

		
client.run(str(os.environ.get('BOT_TOKEN')))
