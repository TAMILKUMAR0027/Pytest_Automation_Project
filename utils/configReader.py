from configparser import ConfigParser
from pathlib import Path


def get_Config_Data(c, k):
    config = ConfigParser()
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "configuration" / "config.ini"
    config.read(config_path)
    return config.get(c, k)
