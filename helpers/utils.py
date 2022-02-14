import yaml
import youtube_dl
import os


def get_config():
    with open('config.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader)["config"]


def set_config(config):
    with open('config.yaml', 'w') as f:
        f.write(yaml.dump({'config': config}, Dumper=yaml.Dumper))


def yt():
    ydl = youtube_dl.YoutubeDL(
        {'format': '249', 'outtmpl': './queue/%(title)s.%(ext)s'})

    with ydl:
        ydl.download(['https://www.youtube.com/watch?v=Q5As_wiR4DE'])


def get_file(name):
    filename = f"./queue/{name}.webm"
    if not os.path.isfile(filename):
        raise Exception("Sorry, I can't find this song")

    return filename
