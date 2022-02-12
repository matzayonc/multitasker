import yaml


def get_config():
    with open('config.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader)["config"]


def set_config(config):
    with open('config.yaml', 'w') as f:
        f.write(yaml.dump({'config': config}, Dumper=yaml.Dumper))
