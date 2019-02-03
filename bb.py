import configparser
import os

CONFIG_FILE="config.ini"

def read_config_file(config_file):
    if not os.path.exists(config_file):
        #print("config file %s not found",config_file)
        raise FileNotFoundError
    else:
        config=configparser.ConfigParser()
        config.read(config_file)
        return config

#config=read_config_file(CONFIG_FILE)