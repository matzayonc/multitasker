import discord


async def get_help(context, bot):
    bot_commands = [i.name for i in bot.commands]
    await context.author.send(f"List of all avalaible commands: {bot_commands}\nSyntax: [prefix][command name] [optional parameter 1] [optional parameter 2] ... (example: !rng 0 9)\nCurrent prefix is: {bot.command_prefix}")
