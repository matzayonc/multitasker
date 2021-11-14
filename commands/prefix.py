import discord, configparser
from helpers.functions import prefix_change

async def f_change_prefix(context, bot):
    parser = configparser.ConfigParser()
    parser.read("./helpers/config.env")
    prefix = parser.get("VAR","VAR_PREFIX")
    new_prefix = prefix_change(context.message.content, prefix)
    if new_prefix == False:
        await context.channel.send("You have to specify the prefix you want to be using.")
    else:
        parser.set("VAR", "VAR_PREFIX", new_prefix)
        with open("./helpers/config.env", "w") as config:
            parser.write(config)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{new_prefix}help"))
        await context.channel.send(f"{context.author.name} has just changed prefix to '{new_prefix}'.")
        return new_prefix