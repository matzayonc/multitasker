import discord; from helpers.config import bot; from helpers.functions import get_connection_status;

@bot.command()
async def disconnect(context):
    text_channel = discord.utils.get(context.guild.text_channels, name = "multitasker")
    if context.author.voice:
        bot_connection_status = get_connection_status(context.guild.voice_channels, bot.user.id, context.author.id)
        if bot_connection_status[0] == 2:
            for client in bot.voice_clients:
                if str(client.user.id) == str(bot.user.id):
                    await client.disconnect()
                    print(f"{context.author.name} has just banished me from this voice-channel")
                    await text_channel.send(f"{context.author.name} has just banished me from this voice-channel")
        elif bot_connection_status[0] == 1:
            print(f"{context.author.name}, you cannot access me from there")
            await text_channel.send(f"{context.author.name}, you cannot access me from there")
        else:
            print(f"{context.author.name}, I am already disconnected")
            await text_channel.send(f"{context.author.name}, I am already disconnected")
    else:
        print(f"{context.author.name}, I am already disconnected")
        await text_channel.send(f"{context.author.name}, I am already disconnected")
