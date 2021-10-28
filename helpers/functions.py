def get_connection_status(voice_channels, bot_id, user_id): # function used to check connection of a sperficied member / bot to the voice channels #
    for voice_channel in voice_channels:
        if str(bot_id) in str(voice_channel.voice_states.keys()): # checking if bot is connected to any voice-channel #
            if str(user_id) in str(voice_channel.voice_states.keys()): # checking if aythor of message is connected to bot's voice-channel #
                return [2, voice_channel]
            return [1, voice_channel]
    return [0, voice_channel]

def prefix_change(string, old_prefix):
    begin_point = len(f"{old_prefix}changeprefix ")
    end_point = len(string)
    if begin_point >= end_point:
        prefix = False
        return prefix
    prefix = string[begin_point : end_point]
    return prefix

    # not working yet! #