import discord


async def stop(context):
    text_channel = discord.utils.get(context.guild.text_channels, name="bot")
    if context.voice_client and (context.voice_client.is_playing() or context.voice_client.is_paused()):
        context.voice_client.stop()
    else:
        await text_channel.send(f"Nothing is playing right now!")
