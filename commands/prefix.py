import discord
import configparser
from helpers.prefix import prefix_change


async def change_prefix(context, bot):
    text_channel = discord.utils.get(context.guild.text_channels, name="bot")
    parser = configparser.ConfigParser()
    parser.read("./config.env")
    prefix = parser.get("var", "var_prefix")
    new_prefix = prefix_change(context.message.content, prefix)
    if new_prefix == 0:
        await text_channel.send(f"You have to specify the prefix you want to be using.")
        return None
    elif new_prefix == 1:
        await text_channel.send(f"You have to use different prefix.")
        return None
    else:
        parser.set("var", "var_prefix", new_prefix)
        with open("./config.env", "w") as config:
            parser.write(config)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{new_prefix}help"))
        await text_channel.send(f"{context.author.name} has just changed prefix to '{new_prefix}'.")
        return new_prefix
