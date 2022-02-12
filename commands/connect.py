import discord
from helpers.connection import get_connection_status


async def connect(context, bot):

    text_channel = discord.utils.get(context.guild.text_channels, name="bot")
    if context.author.voice:
        bot_connection_status = get_connection_status(
            context.guild.voice_channels, bot.user.id, context.author.id)
        if bot_connection_status[0] == 0:
            user_voice_channel = discord.utils.get(
                context.guild.voice_channels, id=context.author.voice.channel.id)
            await user_voice_channel.connect()
            print(f"{context.author.name} has just summoned me to this voice-channel")
            # await text_channel.send(f"{context.author.name} has just summoned me to this voice-channel")

        elif bot_connection_status[0] == 1:
            raise Exception(
                f"{context.author.name}, I am occupied in another channel")
        elif bot_connection_status[0] == 2:
            raise Exception(f"{context.author.name}, I am already here")

    else:
        raise Exception(
            f"{context.author.name}, you are not connected to any voice-channels")
