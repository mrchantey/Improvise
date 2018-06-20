from pkg.utilservices import utility
from pkg.utilservices import datetimeUtils
from datetime import date, time


def RequestScheduleFromParameters(parameters):
    if 'formattedDate' in parameters:
        return RequestSchedule(parameters['formattedDate'])['announcement']
    else:
        return RequestSchedule()['announcement']


def RequestSchedule(reqDate=date.today()):
    activityData = utility.OpenJson("pkg/data/activities.json")
    for plannedDay in activityData['plannedDays']:
        plannedDay["date"] = date(2018, plannedDay["month"], plannedDay["day"])

    matchingPlannedDays = filter(lambda day: day["date"] == reqDate, activityData["plannedDays"])
    if len(matchingPlannedDays) == 0:
        reqDatePhrase = datetimeUtils.GetDateWords(reqDate, False)
        return {"announcement": ["There are no activities planned for {0}".format(reqDatePhrase)]}

    plannedDay = matchingPlannedDays[0]
    plannedDatePhrase = datetimeUtils.GetDateWords(plannedDay["date"])
    plannedDay["announcement"] = ["The activities for {0} are as follows.".format(plannedDatePhrase)]
    FillEvents(activityData["activities"], plannedDay)
    plannedDay["announcement"].extend(map(lambda e: e["timePhrase"], plannedDay["events"]))
    return plannedDay


def FillEvents(activities, plannedDay):
    for event in plannedDay["events"]:
        event["activity"] = filter(lambda a: a["id"] == event["id"], activities)[0]
        event["time"] = time(event["hour"], event["minute"])
        event["timeWords"] = datetimeUtils.GetTimeWords(event["time"])
        event["timePhrase"] = "At {0} we have {1}.".format(event["timeWords"], event["activity"]["name"])


if __name__ == "__main__":
    day = RequestSchedule(date(2017, 3, 12))
    for ann in day["announcement"]:
        print ann
