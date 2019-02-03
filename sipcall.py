import configparser
import requests
import bb
config =bb.read_config_file(bb.CONFIG_FILE)
class SipCallGetter:
    def __init__(self):
        self.requests=requests
        self.login_url=config.get("sipcall","login_url")
    def _login(self):
        return True
    def get_data(self):
        pass
