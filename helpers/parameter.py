def get_parameters(content, parameters):
    message = content.split(" ")
    output = []
    if len(message) == parameters + 1:
        for m in range(1, parameters + 1, 1):
            output.append(message[m])
        return output
    else:
        return None


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
