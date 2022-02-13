from timeit import repeat
import discord
import os
from commands.queue import get_random
from helpers.connection import get_connection_status
from commands.connect import connect


async def play(context, bot, song, repeat):

    filename = f"./queue/{song if song != None else get_random()}.webm"

    bot_connection_status = get_connection_status(
        context.guild.voice_channels, bot.user.id, context.author.id)

    if bot_connection_status[0] == 0:
        await connect(context, bot)

    if bot_connection_status[0] == 1:
        print(
            f"{context.author.name}, you have to join my voice channel to use this command")
        await context.author.send(f"{context.author.name}, you have to join my voice channel to use this command")
    else:
        if os.path.isfile(filename):
            if not context.voice_client.is_playing() and not context.voice_client.is_paused():

                continue_playing = True

                def loop(_):

                    nonlocal continue_playing
                    nonlocal filename

                    if not continue_playing:
                        return

                    context.voice_client.play(discord.FFmpegPCMAudio(
                        executable="/usr/bin/ffmpeg", source=filename), after=loop)
                    context.voice_client.source = discord.PCMVolumeTransformer(
                        context.voice_client.source, volume=0.03)

                    continue_playing = repeat
                    filename = f"./queue/{song if song != None else get_random()}.webm"
                    loop(None)

            else:
                await context.author.send(f"Music is already playing!")
        else:
            await context.author.send(f"This song is not in queue!")

    loop(None)
