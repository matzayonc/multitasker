def prefix_change(string, old_prefix):
    black_list = [34, 35, 37, 39, 64, 92, 96, 126]
    begin_point = len(f"{old_prefix}change_prefix ")
    end_point = len(string)
    if begin_point >= end_point:
        return 0
    prefix = string[begin_point : end_point]
    if old_prefix == prefix:
        return 1
    for char in prefix:
        if (ord(char) > 32) and (ord(char) < 127):
            for element in black_list:
                if element == ord(char):
                    return 1
        else:
            return 1
    return prefix