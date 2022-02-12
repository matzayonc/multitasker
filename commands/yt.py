import discord
import youtube_dl


async def yt(context, bot, link, name):

    ydl = youtube_dl.YoutubeDL(
        {'format': '249', 'outtmpl': './queue/' + name + '.%(ext)s'})

    with ydl:
        ydl.download([link])
