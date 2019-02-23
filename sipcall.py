import configparser
from logging import error

import requests
import balancebuddy

config = balancebuddy.read_config_file(balancebuddy.CONFIG_FILE)


class SipCallGetter:
    def __init__(self):
        self.requests = requests
        self.login_url = config.get("sipcall", "login_url")
        self.username = config.get("sipcall", "username")
        self.password = config.get("sipcall", "password")

    def _login(self):
        try:
            sipcall_session = requests.session()
            response = sipcall_session.get(self.login_url)
            response.raise_for_status()
        except:
            error("cannot connect to '%s'.Internet Connection? DNS? Correct URL in config file?", self.login_url)
            return None
        login = {
            "user": self.username,
            "password": self.password
        }
        login_headers = {
            'referer': "https://my.sipcall.ch/",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
        response_login = sipcall_session.post(self.login_url, data=login, headers=login_headers)
        print(response_login)
        return sipcall_session


if __name__ == '__main__':
    sipcallGetter = SipCallGetter()
    sipcallGetter._login()  # todo: remove when app is finished
