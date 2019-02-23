"""
represents a call
"""
import time


class Call:
    """
    :param time when the call started
    :param duration the duration of the call in minutes
    :param cost  cost of call as double in CHF
    """

    def __init__(self, time, billedMinutes, cost):
        self.time = time
        self.billedMinutes = billedMinutes
        self.cost = cost

    def __str__(self):
        return self.time.strftime("%d.%m.%Y %H:%M") + str(self.billedMinutes) + "min" + str(self.cost) + " CHF"
