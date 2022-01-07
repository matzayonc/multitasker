import configparser
import discord, configparser
from datetime import date

async def f_time(context, parameter):
    parser = configparser.ConfigParser()
    parser.read("./config.env")
    times = parser.get('time', 'time_alcohol')
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    if parameter == "set":
        name = str(context.author)
        if name in times:
            await context.author.send(f"There already are stats for {context.author}")
        else:
            times += f" {context.author}.{date.today()}"
            parser.set("time", "time_alcohol", times)
            with open("./config.env", "w") as config:
                parser.write(config)
    elif parameter == "reset":
        name = str(context.author)
        if name in times:
            entries = times.split(" ")
            for m in range(0, len(entries), 1):
                if entries[m].split(".")[0] == name:
                    time = entries[m].split(".")
                    time = f"{time[0]}.{date.today()}"
                    entries[m] = time
                    break
            times = ""
            for m in range(0, len(entries), 1):
                times += f" {entries[m]}"
            times = times[1:len(times)]
            parser.set("time", "time_alcohol", times)
            with open("./config.env", "w") as config:
                parser.write(config)
        else:
            await context.author.send(f"No stats for {context.author} (use 'set' option first)")
    elif parameter == "check":
        name = str(context.author)
        if name in times:
            entries = times.split(" ")
            for m in range(0, len(entries), 1):
                if entries[m].split(".")[0] == name:
                    time = entries[m].split(".")[1]
                    break
            await context.author.send(f"You haven't been drinking since: {time} (Y-M-D format)")
        else:
            await context.author.send(f"No stats for {context.author} (use 'set' option first)")
    else:
        await context.author.send(f"Incorrect parameter name")