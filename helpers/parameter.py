from nis import match


def get_parameters(content, amount):
    output = content.split(" ")[1:]

    if len(output) != amount:
        if amount == 0:
            raise Exception('Command takes no parameters!')
        elif amount == 1:
            raise Exception('Command takes a parameter!')
        else:
            raise Exception('Command takes ' +
                            str(amount) + ' parameters!')

    return None if amount == 0 else output


def check_parameter(parameter, type):
    if type == "int":
        white_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for char in parameter:
            control_flag = False
            for element in white_list:
                if char == str(element):
                    control_flag = True
                    break
            if not control_flag:
                return 0
        return 1
