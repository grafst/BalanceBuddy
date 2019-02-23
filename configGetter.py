import os

import configparser

CONFIG_FILE = "config.ini"


class FileEmptyError(Exception):
    pass


if not os.path.exists(CONFIG_FILE):
    # print("config file %s not found",config_file)
    raise FileNotFoundError
elif os.stat(CONFIG_FILE).st_size == 0:
    raise FileEmptyError
else:
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
