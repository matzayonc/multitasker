import discord, os
from helpers.connection import get_connection_status

async def f_play(context, bot, song):
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    bot_connection_status = get_connection_status(context.guild.voice_channels, bot.user.id, context.author.id)
    if bot_connection_status[0] == 2:
        if os.path.isfile(f"./queue/{song}"):
            context.voice_client.play(discord.FFmpegPCMAudio(executable = "./ffmpeg.exe", source = f"./queue/{song}"))
            context.voice_client.source = discord.PCMVolumeTransformer(context.voice_client.source, volume=0.03)
        else:
            await context.author.send(f"This song is not in queue!")
    elif bot_connection_status[0] == 1:
        print(f"{context.author.name}, you have to join my voice channel to use this command")
        await text_channel.send(f"{context.author.name}, you have to join my voice channel to use this command")
    elif bot_connection_status[0] == 0:
        print(f"{context.author.name}, you have to summon me to to any voice channel")
        await text_channel.send(f"{context.author.name}, you have to summon me to to any voice channel")