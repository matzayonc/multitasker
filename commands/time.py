import discord, configparser
from datetime import datetime

async def f_time(context, parameter):
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    parser = configparser.ConfigParser()
    parser.read("./config.env")
    times = parser.get('time', 'time_alcohol')
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    if parameter == "set":
        name = str(context.author)
        if name in times:
            await context.author.send(f"There already are stats for {context.author}")
        else:
            times += f" {context.author}.{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.{0}"
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
                    time = f"{time[0]}.{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.{int(time[2]) + 1}"
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
            await text_channel.send(f"{context.author} hasn't been drinking since: {time}")
        else:
            await context.author.send(f"No stats for {context.author} (use 'set' option first)")
    elif parameter == "counter":
        name = str(context.author)
        if name in times:
            entries = times.split(" ")
            for m in range(0, len(entries), 1):
                if entries[m].split(".")[0] == name:
                    time = entries[m].split(".")[2]
                    break
            await text_channel.send(f"{context.author} has been drinking {time} times")
        else:
            await context.author.send(f"No stats for {context.author} (use 'set' option first)")
    else:
        await context.author.send(f"Incorrect parameter name")