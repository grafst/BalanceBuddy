import json
import time
from datetime import datetime
from logging import error

import requests

from Call import Call
from configGetter import config

DATEFORMAT = "%Y-%m-%d %H:%M:%S"


class SipCallGetter:
    def __init__(self):
        self.requests = requests
        self.login_url = config.get("sipcall", "login_url")
        self.account_data_url = config.get("sipcall", "account_data_url")
        self.call_list_url = config.get("sipcall", "call_list_url")
        self.logout_url = config.get("sipcall", "logout_url")
        self.account_id = config.get("sipcall", "account_id")
        self.username = config.get("sipcall", "username")
        self.password = config.get("sipcall", "password")

    def _login(self):
        login = {
            "user": self.username,
            "password": self.password
        }
        login_headers = {
            'referer': "https://my.sipcall.ch/",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

        sipcall_session = requests.session()
        response_login = sipcall_session.post(self.login_url, data=login, headers=login_headers)
        response_login.raise_for_status()
        return sipcall_session

    def logout(self, sipcall_session):
        response_account_page = sipcall_session.get(self.logout_url)

    def getData(self, from_date, to_date):
        try:
            sipcall_session = self._login()
            sipcall_account_data_headers = ""
            response_account_data = sipcall_session.post(self.account_data_url, data="",
                                                         headers=sipcall_account_data_headers)
            response_account_data_dictionary = json.loads(response_account_data.text)
            sip_balance = abs(float(response_account_data_dictionary['account_info']['balance']))
            sip_balance_formatted = "{0:.2f}".format(round(sip_balance, 1))

            connection_data = {
                "i_service": 3,
                "get_total": 1,
                "limit": 1800,
                "from_date": from_date.strftime(DATEFORMAT),
                "to_date": to_date.strftime(DATEFORMAT),
                "i_account": self.account_id
            }
            response_connection_data = sipcall_session.post(self.call_list_url, data=connection_data,
                                                            headers=sipcall_account_data_headers)
            response_connection_data_dictionary = json.loads(response_connection_data.text)
            i = 0
            cost = 0.0
            callList = []
            for entry in response_connection_data_dictionary['xdr_list']:
                connection_start_time = response_connection_data_dictionary['xdr_list'][i]['connect_time']
                connection_target_number = response_connection_data_dictionary['xdr_list'][i]['CLD']
                connection_charged_time = response_connection_data_dictionary['xdr_list'][i]['charged_quantity']
                connection_charged_money = response_connection_data_dictionary['xdr_list'][i]['charged_amount']
                if float(connection_charged_money) > 0.0:
                    start_time = datetime.strptime(connection_start_time, DATEFORMAT)
                    callList.append(Call(time=start_time, billedMinutes=connection_charged_time // 60,
                                         cost=connection_charged_money))
                    cost = cost + float(connection_charged_money)
                i = i + 1
            self.logout(sipcall_session)

            return (callList, sip_balance, cost)
        except:
            error("cannot login to '%s'.Internet Connection? DNS? Correct URL in config file?", self.login_url)
            return (None, 0, 0)
