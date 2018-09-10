from pkg.utilities import utility
from pkg.utilities import datetimeUtils
from datetime import date, time


class Activities():
    def __init__(self):
        activityData = utility.OpenJson("pkg/data/activities.json")
        self.plannedDays = activityData['plannedDays']
        self.activities = activityData['activities']
        self.locations = activityData['locations']
        self.neighbourhoods = activityData['neighbourhoods']

        for plannedDay in self.plannedDays:
            plannedDay["date"] = date(2018, plannedDay["month"], plannedDay["day"])

    def OnRequest(self, requestBody):
        return self.RequestSchedule()

    def RequestScheduleFromParameters(self, params):
        if 'date' in params:
            reqDate = datetimeUtils.ParseDateFromString(params['date'])
            return self.RequestSchedule(reqDate)
        else:
            return self.RequestSchedule()

    def RequestSchedule(self, reqDate=date.today()):
        plannedDay = self.GetRequestedDay(reqDate)
        if plannedDay == None:
            reqDatePhrase = datetimeUtils.GetDateWords(reqDate, False)
            return {"announcement": ["There are no activities planned for {0}".format(reqDatePhrase)]}

        self.FillEvents(plannedDay)
        self.CreateAnnouncement(plannedDay)

        return plannedDay

    def GetRequestedDay(self, reqDate):
        matchingPlannedDays = filter(lambda day: day["date"] == reqDate, self.plannedDays)
        if len(matchingPlannedDays) == 0:
            return None
        else:
            return matchingPlannedDays[0]

    def FillEvents(self, plannedDay):
        for event in plannedDay["events"]:
            # NO ERROR CHECKING
            if 'activity' in event:
                event["activityObject"] = filter(lambda a: a["activity"] == event["activity"], self.activities)[0]
            if 'location' in event:
                event["locationObject"] = filter(lambda l: l["location"] == event["location"], self.locations)[0]
            event["time"] = time(event["hour"], event["minute"])
            event["timeWords"] = datetimeUtils.GetTimeWords(event["time"])
            event["timePhrase"] = "At {0} we have {1}.".format(event["timeWords"], event["activity"])

    def CreateAnnouncement(self, plannedDay):
        plannedDatePhrase = datetimeUtils.GetDateWords(plannedDay["date"])
        plannedDay["announcement"] = ["The activities for {0} are as follows.".format(plannedDatePhrase)]
        plannedDay["announcement"].extend(map(lambda e: e["timePhrase"], plannedDay["events"]))


if __name__ == "__main__":
    activities = Activities()
    plannedDay = activities.RequestScheduleFromParameters({"date": "2018-06-27T12:00:00+10:00"})
    # print plannedDay
    for ann in plannedDay['announcement']:
        print ann
        # day = RequestSchedule(date(2017, 3, 12))
        # for ann in day["announcement"]:
        # print ann
