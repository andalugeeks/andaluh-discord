#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4
###
# Copyleft 2020 Andalugeeks
###

import os

import requests
from discord.ext import commands
from dotenv import load_dotenv

# Andaluh API. More info: https://andaluh.es
API_ANDALUH = "https://api.andaluh.es/epa"

# Discord bot instance
bot = commands.Bot(command_prefix=commands.when_mentioned)

HELP = """
🇳🇬 Guenâ! Çoy un bot trâccrîttôh Andalûh EPA. Dîppongo de lô çigientê comandô. Pruébalô:

/an   Trâccribe Câtteyano - Andalûh (EPA) uçando grafía integraora 'ç'
/anz  Iguâh pero zezeando
/ans  Iguâh pero seseando
/anh  Iguâh pero heheando

Çi quierê çabêh mâh çobre Andalûh y EPA:

👉 Nuêttra páhina web https://andaluh.es
👉 Trâccrîttôh online https://andaluh.es/transcriptor
👉 Teclao Andalûh EPA https://andaluh.es/teclado-andaluz
"""


@bot.event
async def on_ready():
    print(f"Logged in as {bot}")


# Remove default help and add ours
bot.remove_command("help")


@bot.command(name="help", help="Bot help")
async def an(ctx, *args):
    await ctx.send(HELP)


# Andaluh commands
@bot.command(name="an", help="Type in spanish to get Andalûh EPA transliteration.")
async def an(ctx, *args):
    result = requests.get(
        API_ANDALUH, params=dict(spanish=" ".join(args), escapeLinks=True)
    ).json()
    await ctx.send(result["andaluh"])


@bot.command(
    name="anz", help="Type in spanish to get Andalûh EPA Zezeo transliteration."
)
async def anz(ctx, *args):
    result = requests.get(
        API_ANDALUH, params=dict(spanish=" ".join(args), escapeLinks=True, vaf="z")
    ).json()
    await ctx.send(result["andaluh"])


@bot.command(
    name="ans", help="Type in spanish to get Andalûh EPA Seseo transliteration."
)
async def ans(ctx, *args):
    result = requests.get(
        API_ANDALUH, params=dict(spanish=" ".join(args), escapeLinks=True, vaf="s")
    ).json()
    await ctx.send(result["andaluh"])


@bot.command(
    name="anh", help="Type in spanish to get Andalûh EPA Heheo transliteration."
)
async def anh(ctx, *args):
    result = requests.get(
        API_ANDALUH, params=dict(spanish=" ".join(args), escapeLinks=True, vaf="h")
    ).json()
    await ctx.send(result["andaluh"])


def main():
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)


if __name__ == "__main__":
    # Discord secret token storage management
    # More info: https://realpython.com/how-to-make-a-discord-bot-python/

    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)
