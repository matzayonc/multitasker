import discord
from helpers.parameter import check_parameter

async def f_clear(context, n1):
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    if check_parameter(n1, "int") == 1:
        await text_channel.purge(limit = int(n1) + 1)         # context.message.channel
        await text_channel.send(f"Deleted {n1} messages.")
    else:
        await context.author.send("Command 'clear' takes only interger values as a parameter.")
