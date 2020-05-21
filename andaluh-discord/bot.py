import requests
import json
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='/')




@bot.command()
async def an(ctx,p):
    str = requests.get('https://api.andaluh.es/epa', params=dict(spanish= p , escapeLinks=True, vaf=u'z')).json()

    await ctx.send(str)

#prueba de commando
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)
    print(arg)
    print(type(arg))

bot.run(Token secreto)
