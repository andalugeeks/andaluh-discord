#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4
###
# Copyleft 2020 Andalugeeks
###

import os

import requests
from discord import Intents, Interaction, app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Andaluh API. More info: https://andaluh.es
API_ANDALUH = "https://api.andaluh.es/epa"

# Discord bot instance
bot = commands.Bot(
    command_prefix=commands.when_mentioned, help_command=None, intents=Intents.none()
)

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
    print(f"Logged in as {bot.user}")


@bot.command(help="Sync bot tree")
async def sync(ctx: commands.Context):
    await bot.tree.sync()
    await ctx.send("Synced application commands")


@bot.command(help="Bot help")
async def help(ctx: commands.Context):
    await ctx.send(HELP)


# Andaluh slash commands
@bot.tree.command(description="Type in spanish to get Andalûh EPA transliteration.")
@app_commands.describe(text="Text to transliterate")
async def an(interaction: Interaction, text: str):
    result = requests.get(
        API_ANDALUH, params=dict(spanish=text, escapeLinks=True)
    ).json()
    await interaction.response.send_message(result["andaluh"])


@bot.tree.command(description="Type in spanish to get Andalûh EPA Zezeo transliteration.")
@app_commands.describe(text="Text to transliterate")
async def anz(interaction: Interaction, text: str):
    result = requests.get(
        API_ANDALUH, params=dict(spanish=text, escapeLinks=True, vaf="z")
    ).json()
    await interaction.response.send_message(result["andaluh"])


@bot.tree.command(description="Type in spanish to get Andalûh EPA Seseo transliteration.")
@app_commands.describe(text="Text to transliterate")
async def ans(interaction: Interaction, text: str):
    result = requests.get(
        API_ANDALUH, params=dict(spanish=text, escapeLinks=True, vaf="s")
    ).json()
    await interaction.response.send_message(result["andaluh"])


@bot.tree.command(description="Type in spanish to get Andalûh EPA Heheo transliteration.")
@app_commands.describe(text="Text to transliterate")
async def anh(interaction: Interaction, text: str):
    result = requests.get(
        API_ANDALUH, params=dict(spanish=text, escapeLinks=True, vaf="h")
    ).json()
    await interaction.response.send_message(result["andaluh"])


def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)


if __name__ == "__main__":
    # Discord secret token storage management
    # More info: https://realpython.com/how-to-make-a-discord-bot-python/
    main()
