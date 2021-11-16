import discord, configparser
from commands.connect import f_connect
from commands.disconnect import f_disconnect
from commands.play import f_play
from commands.prefix import f_change_prefix
# from commands.loop import f_loop
from discord.ext import commands

config = configparser.ConfigParser()
config.read('./helpers/config.env')
prefix = config.get('var','var_prefix')
bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))
    print(f"{bot.user} is now online!")

@bot.command()
async def connect(context):
    await f_connect(context, bot)

@bot.command()
async def disconnect(context):
    await f_disconnect(context, bot)

@bot.command()
async def play(context):
    await f_play(context, bot)

@bot.command()
async def change_prefix(context):
    new_prefix = await f_change_prefix(context, bot)
    if new_prefix:
        bot.command_prefix = new_prefix

# @bot.command()
# async def loop(context):
#     await f_loop(context, bot)

token = config.get('var','var_token')
bot.run(token)