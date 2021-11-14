def get_connection_status(voice_channels, bot_id, user_id):
    for voice_channel in voice_channels:
        if str(bot_id) in str(voice_channel.voice_states.keys()):
            if str(user_id) in str(voice_channel.voice_states.keys()):
                return [2, voice_channel]
            return [1, voice_channel]
    return [0, voice_channel]

def prefix_change(string, old_prefix):
    begin_point = len(f"{old_prefix}change_prefix ")
    end_point = len(string)
    if begin_point >= end_point:
        prefix = False
        return prefix
    prefix = string[begin_point : end_point]
    return prefix

# def f_set_bot(prefix):
#     config = configparser.ConfigParser()
#     config.read('./helpers/config.env')
#     prefix = config.get('VAR','VAR_PREFIX')
#     bot = commands.Bot(command_prefix = prefix)