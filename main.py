import discord
import commands as cmd
from helpers.parameter import get_parameters
from discord.ext import commands
from utils import get_config, set_config, yt


intents = discord.Intents.default()
intents.members = True

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
async def yt(context):
    try:
        props = get_parameters(context.message.content, 2)
        await cmd.yt(context, bot, props[0], props[1])
        print('playing', props[1])
        await cmd.play(context, bot, props[1])
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def help(context):
    await cmd.get_help(context, bot)


@bot.command()
async def connect(context):
    try:
        get_parameters(context.message.content, 0)
        await cmd.connect(context, bot)
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def disconnect(context):
    try:
        get_parameters(context.message.content, 0)
        await cmd.disconnect(context, bot)
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def rng(context):
    try:
        parameters = get_parameters(context.message.content, 2)
        await cmd.rng(context, parameters[0], parameters[1])
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def clear(context):
    try:
        parameters = get_parameters(context.message.content, 1)
        await cmd.clear(context, parameters[0])
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def play(context):
    try:
        parameters = get_parameters(context.message.content, 1)
        await cmd.play(context, bot, parameters[0])
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def stop(context):
    try:
        get_parameters(context.message.content, 0)
        await cmd.stop(context)
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def pause(context):
    try:
        get_parameters(context.message.content, 0)
        await cmd.pause(context)
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def resume(context):
    try:
        get_parameters(context.message.content, 0)
        await cmd.resume(context)
    except Exception as e:
        print(e.args[0])
        await context.author.send(e.args[0])


@bot.command()
async def queue(context):
    await cmd.queue(context)


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
