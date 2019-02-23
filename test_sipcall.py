import logging
import sys
import unittest
import requests
from httpretty import httpretty
import balancebuddy
import sipcall


class TestSipCall(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG
        stream_handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(stream_handler)
        self.sipCallGetter = sipcall.SipCallGetter()

    def test_sipcallgetter_has_login_function(self):
        self.assertTrue(callable(sipcall.SipCallGetter._login))

    """ def test_cannot_login_if_url_not_reachable(self):
         httpretty.register_uri(httpretty.GET, self.sipCallGetter.login_url, body="", status=404)
         self.assertRaises(requests.RequestException, self.sipCallGetter._login)
    """

    def test_if_login_logs_error_on_http404(self):
        httpretty.register_uri(httpretty.GET, self.sipCallGetter.login_url, body="", status=404)
        with self.assertLogs(self.logger, level='ERROR'):
            self.sipCallGetter._login()

    def test_sucessful_login_returns_a_session_object(self):
        httpretty.register_uri(httpretty.POST, self.sipCallGetter.login_url, body="", status=200)
        sipCallGetter = sipcall.SipCallGetter()
        self.assertIsInstance(sipCallGetter._login(), requests.Session)

    def test_configfile_sipcall_section(self):
        self.assertTrue(balancebuddy.config.has_section("sipcall"))
        missing_subtests = (
            # A tuple of (option_name, subtest_description)
            ('username', 'Missing the first_name field'),
            ('login_url', 'Missing the last_name field'),
            ('password', 'Missing the address field'),
        )
        for option_name, subtest_description in missing_subtests:
            with self.subTest(subtest_description):
                self.assertTrue(balancebuddy.config.has_option("sipcall", option_name))
