import discord
import random
from random import choice
from discord.ext import commands
client = discord.Client()

words= ('hi', 'HI', 'Hi', 'Hello', 'Yo!!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send(f"{random.choice(words)}")
    if message.content.startswith("hi"):
        await message.channel.send(f"{random.choice(words)}")
    if message.content.startswith("python"):
        await message.channel.send("oh man Yes! I am made By Python Make Sure To Learn it!")
    if message.content.startswith("bye"):
        await message.channel.send("bye!")
    if message.content.startswith("rules"):
        await message.channel.send("There are no rule but Don't spam Or u will be banned. Have a great Time")
    if message.content.startswith("Hi"):
        await message.channel.send(f"{random.choice(words)}")
    if message.content.startswith("lol"):
        await message.channel.send("XD :rofl:")
    if message.content.startswith("XD"):
        await message.channel.send("XD :rofl:")
    if message.content.startswith("bruh"):
        await message.channel.send("oof")
    if message.content.startswith("Hola"):
        await message.channel.send(f"{random.choice(words)}")
    if message.content.startswith("bo!play GameR"):
        activity = discord.Game(name="GameR")
        await client.change_presence(status=discord.Status.idle, activity=activity)
    if message.content.startswith("bo!play help"):
        activity = discord.Game(name="bo!help")
        await client.change_presence(status=discord.Status.online, activity=activity)
    if message.content.startswith("bo!play mind"):
        activity = discord.Game(name="With your mind")
        await client.change_presence(status=discord.Status.online, activity=activity)
    if message.content.startswith("bo!play hi"):
        activity = discord.Game(name="hi")
        await client.change_presence(status=discord.Status.online, activity=activity)


client.run('NzY4NjkzODkwNTQ2Nzk0NTQ2.X5EL-Q.ceUatLY399HmEXYRcE9j_ryt8hk')
