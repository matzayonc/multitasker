import commands as cmd


def get_connection_status(voice_channels, bot_id, user_id):
    for voice_channel in voice_channels:

        if str(bot_id) in str(voice_channel.voice_states.keys()):

            if str(user_id) in str(voice_channel.voice_states.keys()):
                return (2, voice_channel)

            return (1, voice_channel)

    return (0, voice_channel)


def is_connected(ctx, bot):
    for channel in ctx.guild.voice_channels:
        if bot.user.id in channel.voice_states:
            return True

    return False


def is_with_user(ctx, bot, user):
    for channel in ctx.guild.voice_channels:
        if bot.user.id in channel.voice_states and user.id in channel.voice_states:
            return True

    return False


def is_alone(ctx, bot):
    for channel in ctx.guild.voice_channels:
        voices = channel.voice_states
        if bot.user.id in voices and len(voices) == 1:
            return True


async def try_here(ctx, bot):
    if not ctx.author.voice:
        raise Exception("You are not on any voice channel")

    if not is_with_user(ctx, bot, ctx.author):
        if not is_connected(ctx, bot):
            await cmd.connect(ctx, bot)
        elif is_alone(ctx, bot):
            await cmd.disconnect(ctx, bot)
            await ctx.author.voice.channel.connect()
        else:
            raise Exception("I'm occupied elsewhere right now")
