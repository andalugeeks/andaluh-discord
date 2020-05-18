import requests
import json
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='/')



@bot.command()
async def an(ctx,p):
    str = requests.get('https://api.andaluh.es/epa?spanish=' + p + '&vaf=%C3%A7&vvf=h&escapeLinks=true')
    x = str.text
    await ctx.send(x)

#prueba de commando
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)
    print(arg)
    print(type(arg))

bot.run(SECRET TOKEN)
