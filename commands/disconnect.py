import discord
from helpers.connection import get_connection_status


async def disconnect(context, bot):
    if context.author.voice:
        for client in bot.voice_clients:
            if str(client.user.id) == str(bot.user.id):
                await client.disconnect()
                print(
                    f"{context.author.name} has just banished me from this voice-channel")
                # await text_channel.send(f"{context.author.name} has just banished me from this voice-channel")

    else:
        raise Exception(f"{context.author.name}, I am already disconnected")
