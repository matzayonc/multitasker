import discord

async def f_help(context, bot):
    bot_commands = []
    for command in bot.commands:
        bot_commands.append(command.name)
    await context.author.send(f"List of all avalaible commands: {bot_commands}\nSyntax: [prefix][command name] [optional parameter 1] [optional parameter 2] ... (example: !rng 0 9)\nCurrent prefix is: {bot.command_prefix}")