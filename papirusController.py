# coding=utf-8
import datetime
import random
import time
from threading import Timer

import papirus
from PIL import Image, ImageDraw
from papirus import PapirusComposite
from papirus.composite import BLACK
from papirus.image import WHITE

from Call import Call

UPDATEINTERVAL = datetime.timedelta(seconds=5)


def test_callList():
    COST_PER_MINUTE = 1.20
    callList = []
    for i in range(0, 5):
        minutes = random.randrange(1, 20)
        callList.append(Call(time=datetime.datetime.now(), duration=datetime.timedelta(minutes=minutes),
                             cost=minutes * COST_PER_MINUTE))
    return callList


def setText(self, text, x, y, Id, size=20):
    self.RemoveText(Id)
    #
    self.AddText(text, x, y, Id=Id, fontPath="arial.ttf", size=size)


PapirusComposite.SetText = setText


class PapirusController():

    def __init__(self):
        self._lastUpdated = datetime.datetime.now()
        self._screen = PapirusComposite(False, 180)
        self.drawScreen()
        self._updateTimer = Timer(UPDATEINTERVAL.seconds, self.update)
        self._updateTimer.start()

    def update(self):
        self.drawScreen()
        self._updateTimer = Timer(UPDATEINTERVAL.seconds, self.update)
        self._lastUpdated = datetime.datetime.now()
        self._updateTimer.start()

    def drawGroupName(self, groupName):
        self._screen.SetText(groupName, 10, 10, "groupName", size=18)

    def drawLines(self):
        self._screen.AddImg("pixel.tif", 10, 30, size=(185, 1))
        self._screen.AddImg("pixel.tif", 10, 77, size=(244, 1))
        self._screen.AddImg("pixel.tif", 10, 146, size=(244, 1))

    def drawCeviZeichen(self):
        self._screen.AddImg("cevilogo.tif", 204, 10, size=(50, 50))

    def drawScreen(self):
        self.drawGroupName("CHRISTOPF VOGEL")
        self.drawCeviZeichen()
        self.drawLastUpdated()
        self.drawCost(53.50)
        self.drawGroupDate(datetime.date(2019, 02, 10), datetime.date(2019, 02, 15))
        self.drawLines()
        self.drawList(test_callList())
        self._screen.WriteAll()

    def drawLastUpdated(self):
        self._screen.SetText(self._lastUpdated.strftime("Zuletzt aktualisiert: %d.%m.%Y %H:%M:%S"), 10, 158, size=12,
                             Id="lastupdated")

    def drawCost(self, cost):
        self._screen.SetText("Fr. " + "%.2f" % cost, 10, 40, size=30, Id="cost")

    def drawList(self, callList):
        start_y = 82
        print(str(callList))
        if not callList:
            # todo: liste löschen
            self._screen.SetText("Keine ausgehende Telefonate")
        else:
            i = 0
            for call in callList:
                if i < 3:
                    self._screen.SetText(call.time.strftime("%d.%m.%Y %H:%M"), 10, start_y + i * 15, size=12,
                                         Id="date" + str(i))
                    self._screen.SetText(str(call.duration) + "min", 133, start_y + i * 15, size=12,
                                         Id="duration" + str(i))
                    self._screen.SetText(str(call.cost) + " CHF", 187, start_y + i * 15, size=12, Id="cost" + str(i))
                elif i < 4:
                    self._screen.SetText("sowie " + str(callList.__len__() - 3) + " weitere", 10, start_y + i * 15,
                                         Id="weitere", size=12)
                else:
                    break
                i += 1

    def drawGroupDate(self, fromDate, toDate):
        dateformat = "%d.%m"
        self._screen.SetText(fromDate.strftime(dateformat) + " - " + toDate.strftime(dateformat), 146, 58, "groupDate",
                             size=12)
        pass
