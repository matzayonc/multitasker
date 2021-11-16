def get_connection_status(voice_channels, bot_id, user_id):
    for voice_channel in voice_channels:
        if str(bot_id) in str(voice_channel.voice_states.keys()):
            if str(user_id) in str(voice_channel.voice_states.keys()):
                return [2, voice_channel]
            return [1, voice_channel]
    return [0, voice_channel]