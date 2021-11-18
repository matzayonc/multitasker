def get_parameters(content, parameters):
    message = content.split(" ")
    output = []
    if len(message) == parameters + 1:
        for m in range(1, parameters + 1, 1):
            output.append(message[m])    
        return output
    else:
        return None