# coding=utf-8
import datetime
import random
import sched
import time
from threading import Timer

from papirus import PapirusComposite

from Call import Call


def test_callList():
    COST_PER_MINUTE = 1.20
    callList = []
    for i in range(0, random.randrange(0, 5)):
        minutes = random.randrange(1, 20)
        callList.append(Call(time=datetime.datetime.now(), billedMinutes=minutes,
                             cost=minutes * COST_PER_MINUTE))
    return callList


def setText(self, text, x, y, Id, size=20):
    self.RemoveText(Id)
    #
    self.AddText(text, x, y, Id=Id, fontPath="arial.ttf", size=size)


PapirusComposite.SetText = setText


class PapirusController():

    def __init__(self):
        self._screen = PapirusComposite(False, 180)
        # todo: init animation

    def drawGroupName(self, groupName):
        self._screen.SetText(groupName, 10, 10, "groupName", size=18)

    def drawLines(self):
        self._screen.AddImg("pixel.tif", 10, 30, size=(185, 1))
        self._screen.AddImg("pixel.tif", 10, 77, size=(244, 1))
        self._screen.AddImg("pixel.tif", 10, 146, size=(244, 1))

    def drawCeviZeichen(self):
        self._screen.AddImg("cevilogo.tif", 204, 10, size=(50, 50))

    def drawScreen(self, lastUpdated, cost, callList):
        self.drawGroupName("MC NUGGET")
        self.drawCeviZeichen()
        self.drawLastUpdated(lastUpdated)
        self.drawCost(cost)
        self.drawGroupDate(datetime.date(2019, 02, 10), datetime.date(2019, 02, 15))
        self.drawLines()
        self.drawList(callList)
        self._screen.WriteAll()

    def drawLastUpdated(self, lastUpdated):
        self._screen.SetText(lastUpdated.strftime("Zuletzt aktualisiert: %d.%m.%Y %H:%M:%S"), 10, 158, size=12,
                             Id="lastupdated")

    def drawCost(self, cost):
        self._screen.SetText("Fr. " + "%.2f" % cost, 10, 40, size=30, Id="cost")

    def drawList(self, callList):
        for call in callList:
            print(call)
        start_y = 82
        for i in range(0, 4):
            self._screen.RemoveText("date" + str(i))
            self._screen.RemoveText("duration" + str(i))
            self._screen.RemoveText("cost" + str(i))
        if not callList:
            self._screen.SetText("Keine ausgehende Telefonate", 10, start_y, size=12, Id="date0")
        else:
            i = 0
            for call in callList:
                if i < 3 or (i == 3 and callList.__len__() == 4):
                    self._screen.SetText(call.time.strftime("%d.%m.%Y %H:%M"), 10, start_y + i * 15, size=12,
                                         Id="date" + str(i))
                    self._screen.SetText("%02i min" % call.billedMinutes, 133, start_y + i * 15, size=12,
                                         Id="duration" + str(i))
                    self._screen.SetText(str(call.cost) + " CHF", 187, start_y + i * 15, size=12, Id="cost" + str(i))
                elif i < 4:
                    self._screen.SetText("sowie " + str(callList.__len__() - 3) + " weitere", 10, start_y + i * 15,
                                         Id="weitere", size=12)
                else:
                    break
                i += 1
        self.callList = test_callList()

    def drawGroupDate(self, fromDate, toDate):
        dateformat = "%d.%m"
        self._screen.SetText(fromDate.strftime(dateformat) + " - " + toDate.strftime(dateformat), 146, 56, "groupDate",
                             size=12)
        pass
