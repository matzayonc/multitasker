import discord
import os
from random import randrange


def get_queue():
    queue = []

    for f in os.listdir("./queue/"):
        if ".mp3" in f or ".webm" in f:
            queue.append(f.split('.')[0])

    return queue


def get_random():
    queue = get_queue()

    if len(queue) == 0:
        raise Exception('There are no songs in queue')

    return queue[randrange(len(queue))]


async def queue(context):
    text_channel = discord.utils.get(context.guild.text_channels, name="bot")
    queue = get_queue()

    await text_channel.send(f"Queue: {queue}")
