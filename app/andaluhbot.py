#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4
###
# Copyleft 2020 Andalugeeks
###

import os

import requests
from discord import Embed, Intents, Interaction, TextChannel, app_commands
from discord.errors import Forbidden
from discord.ext import commands
from dotenv import load_dotenv

# Andaluh API. More info: https://andaluh.es
API_ANDALUH = "https://api.andaluh.es/epa"

# Discord bot instance
bot = commands.Bot(
    command_prefix=commands.when_mentioned, help_command=None, intents=Intents.default()
)

HELP = """
Guenâ! Çoy un bot trâccrîttôh Andalûh EPA. Dîppongo de lô çigientê comandô. Pruébalô:

``/andaluh`` Trâccribe Câtteyano -> Andalûh (EPA) uçando grafía integraora 'ç' o una de çûh bariantê de zezeo, seseo o heheo.

Çi quierê çabêh mâh çobre Andalûh y EPA:

👉 Nuêttra páhina web https://andaluh.es
👉 Trâccrîttôh online https://andaluh.es/transcriptor
👉 Teclao Andalûh EPA https://andaluh.es/teclado-andaluz
"""
EMBED_COLOR = 0x5DBB41


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command(help="Sync bot tree")
@commands.is_owner()
async def sync(ctx: commands.Context):
    await bot.tree.sync()
    await ctx.send("Synced application commands")


@bot.command(help="Bot help")
async def help(ctx: commands.Context):
    await ctx.send(embed=Embed(description=HELP, color=EMBED_COLOR))


# Andaluh slash command
@bot.tree.command(description="Type in Spanish to get Andalûh EPA transliteration")
@app_commands.describe(
    text="Text to transliterate", variant="Transliterate using one of the variants"
)
@app_commands.choices(
    variant=[
        app_commands.Choice(name="Zezeo", value="z"),
        app_commands.Choice(name="Seseo", value="s"),
        app_commands.Choice(name="Heheo", value="h"),
    ]
)
async def andaluh(
    interaction: Interaction, text: str, variant: app_commands.Choice[str] = None
):
    use_webook = (
        isinstance(interaction.channel, TextChannel)
        and interaction.app_permissions.manage_webhooks
    )
    await interaction.response.defer(ephemeral=use_webook)

    params = {"spanish": text, "escapeLinks": True}
    if variant:
        params["vaf"] = variant.value
    result = requests.get(API_ANDALUH, params=params).json()

    if use_webook:
        await send_webhook_message(interaction, result["andaluh"])
    else:
        await interaction.followup.send(result["andaluh"])


async def send_webhook_message(interaction: Interaction, text):
    webhook = await interaction.channel.create_webhook(name=bot.user.name)
    await webhook.send(
        text,
        username=interaction.user.display_name,
        avatar_url=interaction.user.display_avatar.url,
    )
    await webhook.delete()
    await interaction.followup.send("Tradûççión finiquitá!")


def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)


if __name__ == "__main__":
    # Discord secret token storage management
    # More info: https://realpython.com/how-to-make-a-discord-bot-python/
    main()
