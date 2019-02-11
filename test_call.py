import datetime
import unittest
import Call


class TestCall(unittest.TestCase):
    def setUp(self):
        self.time = datetime.datetime.now()
        self.duration = 4
        self.cost = 3.5
        self.myCall = Call.Call(self.time, self.duration, self.cost)

    def test_call(self):
        self.assertEqual(
            str(self.myCall),
            self.time.strftime("%d.%m.%Y %H:%M") + str(self.duration) + "min" + str(self.cost) + " CHF")

    def test_call_has_relevant_attributes(self):
        self.assertTrue(hasattr(self.myCall, "time"))
        self.assertTrue(hasattr(self.myCall, "duration"))
        self.assertTrue(hasattr(self.myCall, "cost"))
