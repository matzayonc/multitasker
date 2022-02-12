import random
from helpers.parameter import check_parameter, get_parameters


async def rng(context, n1, n2):
    parameters = get_parameters(context.message.content, 2)
    if check_parameter(n1, "int") == 1 and check_parameter(n2, "int") == 1:
        if int(parameters[0]) <= int(parameters[1]):
            x = random.randrange(int(parameters[0]), int(parameters[1]) + 1)
        elif int(parameters[0]) > int(parameters[1]):
            x = random.randrange(int(parameters[1]), int(parameters[0]) + 1)
        await context.author.send(f"Your random number: {x}")
    else:
        await context.author.send("Command 'rng' takes only interger values as parameters.")
