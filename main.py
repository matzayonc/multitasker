import discord
import commands as cmd
from helpers.parameter import get_parameters
from discord.ext import commands
from utils import get_config, set_config, yt


intents = discord.Intents.default()
intents.members = True

# yt()

config = get_config()
bot = commands.Bot(
    command_prefix=config['prefix'], intents=intents, help_command=None
)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{config['prefix']}help"))
    print(f"{bot.user} is now online!")


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="MEMBER")
    await member.add_roles(role)


@bot.command()
async def ping(context):
    await context.author.send("Hejcia")


@bot.command()
async def help(context):
    await cmd.help(context, bot)


@bot.command()
async def connect(context):
    if get_parameters(context.message.content, 0) != None:
        await cmd.connect(context, bot)
    else:
        await context.author.send("Command 'connect' takes no parameters!")


@bot.command()
async def disconnect(context):
    if get_parameters(context.message.content, 0) != None:
        await cmd.disconnect(context, bot)
    else:
        await context.author.send("Command 'disconnect' takes no parameters!")


@bot.command()
async def rng(context):
    parameters = get_parameters(context.message.content, 2)
    if parameters != None:
        await cmd.rng(context, parameters[0], parameters[1])
    else:
        await context.author.send("Command 'rng' takes two parameters!")


@bot.command()
async def clear(context):
    parameters = get_parameters(context.message.content, 1)
    if parameters != None:
        await cmd.clear(context, parameters[0])
    else:
        await context.author.send("Command 'clear' takes one parameter!")


@bot.command()
async def play(context):
    parameters = get_parameters(context.message.content, 1)
    if parameters != None:
        await cmd.play(context, bot, parameters[0])
    else:
        await context.author.send("Command 'play' takes one parameter!")


@bot.command()
async def stop(context):
    if get_parameters(context.message.content, 0) != None:
        await cmd.stop(context)
    else:
        await context.author.send("Command 'stop' takes no parameters!")


@bot.command()
async def pause(context):
    if get_parameters(context.message.content, 0) != None:
        await cmd.pause(context)
    else:
        await context.author.send("Command 'pause' takes no parameters!")


@bot.command()
async def resume(context):
    if get_parameters(context.message.content, 0) != None:
        await cmd.resume(context)
    else:
        await context.author.send("Command 'resume' takes no parameters!")


@bot.command()
async def queue(context):
    await cmd.f_queue(context)


# @bot.command()
# async def change_prefix(context):
#     new_prefix = await cmd.change_prefix(context, bot)
#     # if new_prefix:
#     #     bot.command_prefix = new_prefix
#     # print('here')
#     # global prefix
#     print(context.message.content)
#     # prefix = context.message.content


@bot.command()
async def time(context):
    parameters = get_parameters(context.message.content, 1)
    if parameters != None:
        await cmd.time(context, parameters[0])
    else:
        await context.author.send("Command 'time' takes one parameters!")

bot.run(config['token'])
