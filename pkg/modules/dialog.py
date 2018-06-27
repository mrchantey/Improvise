# imports for testing only
from weather import Weather
from news import News
from activities import Activities
# end test imports
from pkg.modules.dialogflowClient import DialogflowClient
import sys


class Dialog():
    def __init__(self, weather, news, activities, naoSayCallback=None):
        self.dialogflowClient = DialogflowClient()
        self.weather = weather
        self.news = news
        self.activities = activities
        self.naoSayCallback = naoSayCallback

    def OnRequest(self, requestBody):
        queryText = requestBody['queryText'].replace("_", " ")
        response = self.FetchDialog(queryText)
        if self.naoSayCallback != None:
            self.naoSayCallback({'phrase': response['responseText'], 'animate': True})
        return response

    def FetchDialog(self, queryText):
        response = self.dialogflowClient.MakeFormattedRequest(queryText)
        if response['action'] == 'weather.get':
            response['responseText'] = self.weather.RequestWeatherDescription()
        elif response['action'] == 'activities.get':
            response['responseText'] = self.activities.RequestScheduleFromParameters(response['parameters'])['announcement']
        elif response['action'] == 'news.get':
            response['responseText'] = self.news.RequestHeadlinesFromParameters(response['parameters'])['headlines']
        return response


if __name__ == '__main__':
    weather = Weather()
    news = News()
    activities = Activities()
    dialog = Dialog(weather, news, activities)
    response = dialog.OnRequest({'queryText': "what news?"})
    print response
