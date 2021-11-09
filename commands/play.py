import discord, os

from discord import voice_client; from helpers.config import bot; from helpers.functions import get_connection_status;

@bot.command()
async def play(context):
    text_channel = discord.utils.get(context.guild.text_channels, name = "multitasker")
    voice_channel = context.channel.guild
    current_song = os.path.isfile("./data/song.flac")
    bot_connection_status = get_connection_status(context.guild.voice_channels, bot.user.id, context.author.id)
    if bot_connection_status[0] == 2:
        if current_song:
            voice_channel.voice_client.play(discord.FFmpegPCMAudio(executable = "./ffmpeg.exe", source = "./data/song.flac"))
    elif bot_connection_status[0] == 1:
        print(f"{context.author.name}, you have to join my voice channel to use this command")
        await text_channel.send(f"{context.author.name}, you have to join my voice channel to use this command")
    else:
        print(f"{context.author.name}, you have to summon me to to any voice channel")
        await text_channel.send(f"{context.author.name}, you have to summon me to to any voice channel")