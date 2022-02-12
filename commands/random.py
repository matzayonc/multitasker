import discord
import os
from random import randrange
from helpers.connection import get_connection_status
from commands.queue import get_queue
from commands.play import play


async def random(context, bot):
    queue = get_queue()

    if len(queue) == 0:
        raise Exception('There are no songs in queue')

    song = queue[randrange(len(queue))]

    await play(context, bot, song)
