import discord
from helpers.connection import get_connection_status


async def disconnect(context, bot):
    text_channel = discord.utils.get(context.guild.text_channels, name="bot")
    if context.author.voice:
        bot_connection_status = get_connection_status(
            context.guild.voice_channels, bot.user.id, context.author.id)
        if bot_connection_status[0] == 2:
            for client in bot.voice_clients:
                if str(client.user.id) == str(bot.user.id):
                    await client.disconnect()
                    print(
                        f"{context.author.name} has just banished me from this voice-channel")
                    # await text_channel.send(f"{context.author.name} has just banished me from this voice-channel")
        elif bot_connection_status[0] == 1:
            raise Exception(
                f"{context.author.name}, you cannot access me from there")
        elif bot_connection_status[0] == 0:
            raise Exception(
                f"{context.author.name}, I am already disconnected")
    else:
        raise Exception(f"{context.author.name}, I am already disconnected")
