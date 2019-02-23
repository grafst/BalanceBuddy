import datetime
import sched
import time

from datetime import datetime
import papirusController
import sipcall
from configGetter import config


class BalanceBuddy():
    def __init__(self):
        self.scheduler = None
        self.papirusController = papirusController.PapirusController()
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def run(self):
        from_date = datetime(year=2017, month=1, day=1, hour=0, minute=0, second=0)
        to_date = datetime(year=2019, month=2, day=21, hour=0, minute=0, second=0)
        sipCallGetter = sipcall.SipCallGetter()
        (callList, sip_balance, cost) = sipCallGetter.getData(from_date, to_date)
        lastUpdated = datetime.now()
        self.papirusController.drawScreen(lastUpdated, cost, callList)

        # run again in x time
        self.scheduler.enter(int(config.get("balancebuddy", "update_frequency")), 1, self.run, "")
        self.scheduler.run()


if __name__ == '__main__':
    balancebuddy = BalanceBuddy()
    balancebuddy.run()
