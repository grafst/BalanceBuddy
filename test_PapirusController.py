import unittest

import papirusController


class TestPapirusController(unittest.TestCase):
    def test_PapirusController_has_drawWelcomeAnimation_function(self):
        self.assertTrue(callable(papirusController.PapirusController.drawWelcomeAnimation))


"""  def test_PapirusController_has_correct_attributes(self):
      attributes = ["_lastUpdated", "_autoUpdateInterval", "_updateTimer", "_screen"]
      for attribute_name in attributes:
          with self.subTest(attribute_name):
              self.assertTrue(hasattr(papirusController.PapirusController, attribute_name))
"""
