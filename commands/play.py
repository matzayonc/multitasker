import discord
import os
from helpers.connection import get_connection_status


async def play(context, bot, song):
    filename = f"./queue/{song}.webm"
    bot_connection_status = get_connection_status(
        context.guild.voice_channels, bot.user.id, context.author.id)
    if bot_connection_status[0] == 2:
        if os.path.isfile(filename):
            if not context.voice_client.is_playing() and not context.voice_client.is_paused():
                context.voice_client.play(discord.FFmpegPCMAudio(
                    executable="/usr/bin/ffmpeg", source=filename))
                context.voice_client.source = discord.PCMVolumeTransformer(
                    context.voice_client.source, volume=0.03)
            else:
                await context.author.send(f"Music is already playing!")
        else:
            await context.author.send(f"This song is not in queue!")
    elif bot_connection_status[0] == 1:
        print(
            f"{context.author.name}, you have to join my voice channel to use this command")
        await context.author.send(f"{context.author.name}, you have to join my voice channel to use this command")
    elif bot_connection_status[0] == 0:
        print(f"{context.author.name}, you have to summon me to to any voice channel")
        await context.author.send(f"{context.author.name}, you have to summon me to to any voice channel")
