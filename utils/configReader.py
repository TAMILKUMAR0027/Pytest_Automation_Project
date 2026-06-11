from configparser import ConfigParser


def get_config_Data(c, k):
    config = ConfigParser()
    config.read("..\config.ini")
    return config.get(c, k)
