import discord


async def pause(context):
    text_channel = discord.utils.get(context.guild.text_channels, name="bot")
    if context.voice_client and context.voice_client.is_playing():
        context.voice_client.pause()
    else:
        await text_channel.send(f"Nothing is playing right now!")
