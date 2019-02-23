import datetime
import random

import configparser
import papirusController
import os

CONFIG_FILE = "config.ini"


class FileEmptyError(Exception):
    pass


def read_config_file(config_file):
    if not os.path.exists(config_file):
        # print("config file %s not found",config_file)
        raise FileNotFoundError
    elif os.stat(config_file).st_size == 0:
        raise FileEmptyError
    else:
        config = configparser.ConfigParser()
        config.read(config_file)
        return config

        # papirusController.drawScreen()


config = read_config_file(CONFIG_FILE)
papirusController = papirusController.PapirusController()
