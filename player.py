from discord.ext import commands
import discord
from commands.queue import get_random_song
import youtube_dl


class Boombox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.stop_after = True
        self.song_after = None

    def stream(self, ctx, filename):
        ctx.voice_client.play(discord.FFmpegPCMAudio(
            executable="/usr/bin/ffmpeg", source=filename), after=lambda _: self.after(ctx))
        ctx.voice_client.source = discord.PCMVolumeTransformer(
            ctx.voice_client.source, volume=0.03)

    def after(self, ctx):
        if self.stop_after:
            return

        name = self.song_after if self.song_after != None else get_random_song()
        filename = f"./queue/{name}.webm"

        self.stream(ctx, filename)

    @commands.command()
    async def play(self, ctx, song):
        filename = f"./queue/{song}.webm"
        self.stream(ctx, filename)
        self.stop_after = True

    @commands.command()
    async def loop(self, ctx, song):
        filename = f"./queue/{song}.webm"
        self.stop_after = False
        self.song_after = song
        self.stream(ctx, filename)

    @commands.command()
    async def random(self, ctx):
        self.stop_after = True
        filename = f"./queue/{get_random_song()}.webm"
        self.stream(ctx, filename)

    @commands.command()
    async def shuffle(self, ctx):
        self.stop_after = False
        self.song_after = None
        filename = f"./queue/{get_random_song()}.webm"
        self.stream(ctx, filename)

    @commands.command()
    async def stop(self, ctx):
        self.stop_after = True
        self.song_after = None
        await self.skip(ctx)

    @commands.command()
    async def skip(self, ctx):

        if not (ctx.voice_client and (ctx.voice_client.is_playing() or ctx.voice_client.is_paused())):
            raise Exception(f"Nothing is playing right now!")

        ctx.voice_client.stop()

    @commands.command()
    async def yt(self, ctx, link, name):
        ydl = youtube_dl.YoutubeDL(
            {'format': '249', 'outtmpl': './queue/' + name + '.%(ext)s'})

        with ydl:
            ydl.download([link])

        await self.play(ctx, name)

    @play.error
    @loop.error
    @random.error
    @shuffle.error
    @stop.error
    @skip.error
    @yt.error
    async def report_error(self, ctx, err):
        print(err.args[0])
        await ctx.author.send(err.args[0])
