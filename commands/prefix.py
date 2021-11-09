import discord
from helpers.functions import prefix_change
from helpers.config import bot, prefix

@bot.command()
async def changeprefix(context):
    new_prefix = prefix_change(context.message.content, prefix)
    if new_prefix == False:
        await context.channel.send("You have to specify the prefix you want to be using.")
    else:
        config_file = open("./helpers/config.py", "w")
        config_file.write(f"from discord.ext import commands\n\n")
        config_file.write(f'prefix = "{new_prefix}"\n')
        config_file.write(f"bot = commands.Bot(command_prefix = prefix)\n")
        config_file.close()
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{new_prefix}help"))
        await context.channel.send(f"{context.author.name} has just changed prefix to '{new_prefix}'.")
