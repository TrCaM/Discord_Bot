import os

import discord

import settings

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello'):
        await message.channel.send(f'Hello, {message.author.name}!')

client.run(settings.TOKEN)
