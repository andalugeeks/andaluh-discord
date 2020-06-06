#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4
###

import json

import requests
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.command()
async def an(ctx, *args):
    str = requests.get('https://api.andaluh.es/epa', params=dict(spanish=' '.join(args), escapeLinks=True, vaf=u'z')).json()
    await ctx.send(str['andaluh'])

if __name__ == '__main__':
    # Secret token storage as per https://realpython.com/how-to-make-a-discord-bot-python/
    import os
    from dotenv import load_dotenv

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)