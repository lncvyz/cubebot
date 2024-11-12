import discord
from discord.ext import commands
import random
from tinydb import TinyDB, Query
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)
client = commands.Bot(intents = intents, command_prefix = '$', case_insensitive = True)

query = Query()

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    for i in message.mentions:
        if i.id == client.user.id:
            await message.channel.send("can i help you")
            await message.channel.send("cunt")
    if message.content.startswith("kys"):
        await message.channel.send("no because it doesn't take being alive to love life")
    if message.content.startswith("kms"):
        await message.channel.send("nooo don't kill yourself your so sexy aha")
    if "ai art" in message.content:
        await message.channel.send("close enough welcome back plagiarism")

    await client.process_commands(message)

########

# HELP
@client.command()
async def help(ctx):
    pass

@client.command()
async def tell_my_fortune(ctx):
    future_adjective = ["good", "bad", "neutral"]
    future_thing = ["job", "partner", "parent", "sibling", "friend", "sky"]
    future_action = ["fail", "succeed", "go fucking crazy", "be okay"]
    result = f"Your future looks {random.choice(future_adjective)} because your {random.choice(future_thing)} will {random.choice(future_action)}!"
    await ctx.send(result)

########

# TAROT

tarot_majorArcana = ["fool", "magician", "high priestess", "empress", "emperor", "hierophant", "lovers", "chariot", "strength", "hermit", "wheel of fortune", "justice", "hanged man", "death", "temperance", "devil", "tower", "star", "moon", "sun", "judgment", "world"]
tarot_suits = ["cups", "pentacles", "swords", "wands"]
tarot_faces = ["king", "queen", "page", "knight"]

@client.command()
async def tarot(ctx):
    digit = random.choice(range(1, 40))

    # major arcana
    if digit < 12:
        card = random.choice(tarot_majorArcana)
        await ctx.send(f"your card is the {card}")

    # minor arcana
    else:
        suit = random.choice(tarot_suits)
        number = random.choice(range(1, 14))
        if digit == 1:
            await ctx.send(f"your card is the ace of {suit}")
        elif digit <= 10 and digit > 1:
            await ctx.send(f"your card is the {number} of {suit}")
        else:
            face = random.choice(tarot_faces)
            await ctx.send(f"your card is the {face} of {suit}")

client.run("thing")