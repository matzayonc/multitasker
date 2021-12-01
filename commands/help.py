import discord

async def f_help(context, bot):
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    bot_commands = []
    for command in bot.commands:
        bot_commands.append(command.name)
    await text_channel.send(f"List of all avalaible commands: {bot_commands}\nExample of the syntax: [prefix][command name] [optional parameters]\nCurrent prefix is: {bot.command_prefix}")