import discord, random
from helpers.parameter import get_parameters

async def f_rng(context):
    text_channel = discord.utils.get(context.guild.text_channels, name = "bot")
    parameters = get_parameters(context.message.content, 2)
    if parameters:
        white_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for char in parameters[0]:
            control_flag = False
            for element in white_list:
                if char == str(element):
                    control_flag = True
                    break
            if not control_flag:
                await text_channel.send("Command 'rng' takes only interger values as parameters.")
                return 0
        x = random.randrange(int(parameters[0]), int(parameters[1]) + 1)
        await text_channel.send(f"Your random number: {x}")
    else:
        await text_channel.send("Command 'rng' takes two parameters only.")