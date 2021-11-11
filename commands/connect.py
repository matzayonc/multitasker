import discord
from helpers.functions import get_connection_status

async def f_connect(context, bot):
    text_channel = discord.utils.get(context.guild.text_channels, name = "multitasker")
    if context.author.voice:
        bot_connection_status = get_connection_status(context.guild.voice_channels, bot.user.id, context.author.id)
        if bot_connection_status[0] == 0:
            user_voice_channel = discord.utils.get(context.guild.voice_channels, id = context.author.voice.channel.id)
            await user_voice_channel.connect()
            print(f"{context.author.name} has just summoned me to this voice-channel")
            await text_channel.send(f"{context.author.name} has just summoned me to this voice-channel")
        elif bot_connection_status[0] == 1:
            print(f"{context.author.name}, I am occupied in another channel")
            await text_channel.send(f"{context.author.name}, I am occupied in another channel")
        elif bot_connection_status[0] == 2:
            print(f"{context.author.name}, I am already here")
            await text_channel.send(f"{context.author.name}, I am already here")
    elif not context.author.voice:
        print(f"{context.author.name}, you are not connected to any voice-channels")
        await text_channel.send(f"{context.author.name}, you are not connected to any voice-channels")
