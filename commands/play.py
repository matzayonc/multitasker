import discord, os
from helpers.connection import get_connection_status

async def f_play(context, bot):
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    voice_channel = context.channel.guild
    current_song = os.path.isfile("./data/song.mp3")
    bot_connection_status = get_connection_status(context.guild.voice_channels, bot.user.id, context.author.id)
    if bot_connection_status[0] == 2:
        if current_song:
            voice_channel.voice_client.play(discord.FFmpegPCMAudio(executable = "./helpers/ffmpeg.exe", source = "./data/song.mp3"))
    elif bot_connection_status[0] == 1:
        print(f"{context.author.name}, you have to join my voice channel to use this command")
        await text_channel.send(f"{context.author.name}, you have to join my voice channel to use this command")
    elif bot_connection_status[0] == 0:
        print(f"{context.author.name}, you have to summon me to to any voice channel")
        await text_channel.send(f"{context.author.name}, you have to summon me to to any voice channel")