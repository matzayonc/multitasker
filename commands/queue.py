import discord
import os


async def f_queue(context):
    text_channel = discord.utils.get(context.guild.text_channels, name="bot")
    temp = os.listdir("./queue/")
    queue = []
    for m in range(0, len(temp), 1):
        if ".mp3" in temp[m]:
            queue.append(temp[m])
        if ".webm" in temp[m]:
            queue.append(temp[m])
    await text_channel.send(f"Queue: {queue}")
