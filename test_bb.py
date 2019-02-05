import configparser
import unittest

import bb


class TestConfigFile(unittest.TestCase):
    def test_read_non_existent_tag(self):
        #todo: mayby create temporary config file and after delete it
        config = bb.read_config_file("fail_config.ini")
        self.assertRaises(configparser.NoOptionError, config.get, "sipcall", "login_url")

    def test_load_config_file(self):
        self.assertRaises(FileNotFoundError, bb.read_config_file, "")

    def test_raise_exception_on_empty_config_file(self):
        self.assertRaises(bb.FileEmptyError, bb.read_config_file, "config_empty.ini")
