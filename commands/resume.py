import discord

async def f_resume(context):
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    if context.voice_client and context.voice_client.is_paused():
        context.voice_client.resume()
    else:
        await text_channel.send(f"Nothing is paused right now!")