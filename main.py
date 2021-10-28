import discord, commands.connect, commands.disconnect; from helpers.config import prefix, bot

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))
    print(f"{bot.user} is now online!")
bot.run("ODk3OTY4NjUzNzQyNTE4MzMy.YWdYeg.qq7uGUAkobaz2J2NciFbLgqdpxA")
