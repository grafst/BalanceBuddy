"""
represents a call
"""


class Call:
    """
    :param time when the call started
    :param duration the duration of the call in minutes
    :param cost  cost of call as double in CHF
    """

    def __init__(self, time, duration, cost):
        self.time = time
        self.duration = duration
        self.cost = cost

    def __str__(self):
        return self.time.strftime("%d.%m.%Y %H:%M") + str(self.duration) + "min" + str(self.cost) + " CHF"
