import unittest
import sipcall
class TestSipCall(unittest.TestCase):
    def test_login(self):
        sipCallGetter=sipcall.SipCallGetter()
        self.assertEqual(sipCallGetter._login(),True)
"""
    @httpretty.activate
    def can_load_a_site():
        # define your patch:
        httpretty.register_uri(httpretty.GET, "http://yipit.com/", body="mueter", status=200)
        # use!
        sipCallGetter=sipcall.SipCallGetter()
        assert sipCallGetter._login() == True
"""