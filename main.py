import discord, configparser
from commands.connect import f_connect
from commands.disconnect import f_disconnect
from commands.play import f_play
from commands.stop import f_stop
from commands.pause import f_pause
from commands.resume import f_resume
from commands.queue import f_queue
from commands.prefix import f_change_prefix
from commands.clear import f_clear
from commands.rng import f_rng
from commands.help import f_help
from commands.time import f_time
from helpers.parameter import get_parameters
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

config = configparser.ConfigParser()
config.read('./config.env')
prefix = config.get('var','var_prefix')
bot = commands.Bot(command_prefix = prefix, intents = intents, help_command = None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))
    print(f"{bot.user} is now online!")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="MEMBER")
    await member.add_roles(role)

@bot.command()
async def help(context):
    await f_help(context, bot)

@bot.command()
async def connect(context):
    if get_parameters(context.message.content, 0) != None:
        await f_connect(context, bot)
    else:
        await context.author.send("Command 'connect' takes no parameters!")

@bot.command()
async def disconnect(context):
    if get_parameters(context.message.content, 0) != None:
        await f_disconnect(context, bot)
    else:
        await context.author.send("Command 'disconnect' takes no parameters!")

@bot.command()
async def rng(context):
    parameters = get_parameters(context.message.content, 2)
    if parameters != None:
        await f_rng(context, parameters[0], parameters[1])
    else:
        await context.author.send("Command 'rng' takes two parameters!")

@bot.command()
async def clear(context):
    parameters = get_parameters(context.message.content, 1)
    if parameters != None:
        await f_clear(context, parameters[0])
    else:
        await context.author.send("Command 'clear' takes one parameter!")

@bot.command()
async def play(context):
    parameters = get_parameters(context.message.content, 1)
    if parameters != None:
        await f_play(context, bot, parameters[0])
    else:
        await context.author.send("Command 'play' takes one parameter!")

@bot.command()
async def stop(context):
    if get_parameters(context.message.content, 0) != None:
        await f_stop(context)
    else:
        await context.author.send("Command 'stop' takes no parameters!")

@bot.command()
async def pause(context):
    if get_parameters(context.message.content, 0) != None:
        await f_pause(context)
    else:
        await context.author.send("Command 'pause' takes no parameters!")
   
@bot.command()
async def resume(context):
    if get_parameters(context.message.content, 0) != None:
        await f_resume(context)
    else:
        await context.author.send("Command 'resume' takes no parameters!")

@bot.command()
async def queue(context):
    await f_queue(context)

@bot.command()
async def change_prefix(context):
    new_prefix = await f_change_prefix(context, bot)
    if new_prefix:
        bot.command_prefix = new_prefix

@bot.command()
async def time(context):
    parameters = get_parameters(context.message.content, 1)
    if parameters != None:
        await f_time(context, parameters[0])
    else:
        await context.author.send("Command 'time' takes one parameters!")

token = config.get('var','var_token')
bot.run(token)