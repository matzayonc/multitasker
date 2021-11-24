import discord
from helpers.parameter import get_parameters

async def f_clear(context):
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    parameters = get_parameters(context.message.content, 1)
    if parameters:
        white_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for char in parameters[0]:
            control_flag = False
            for element in white_list:
                if char == str(element):
                    control_flag = True
                    break
            if not control_flag:
                await text_channel.send("Command 'clear' takes only interger values as a parameter.")
                return 0
        await text_channel.purge(limit = int(parameters[0]) + 1)    # context.message.channel
        await text_channel.send(f"Deleted {parameters[0]} messages.")
    else:
        await text_channel.send("Command 'clear' takes one parameter only.")
