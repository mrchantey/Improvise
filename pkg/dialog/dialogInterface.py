from modules import weather
from modules import news
from modules import activities
from modules import dialogflowClient
import sys


def Converse(queryText):
    response = dialogflowClient.MakeFormattedRequest(queryText)
    if response['action'] == 'weather.get':
        response['responseText'] = weather.RequestWeatherDescription()
    elif response['action'] == 'activities.get':
        response['responseText'] = activities.RequestScheduleFromParameters(response['parameters'])
    elif response['action'] == 'news.get':
        response['responseText'] = news.RequestHeadlinesFromParameters(response['parameters'])
    return response


if __name__ == '__main__':
    response = -1
    if len(sys.argv) > 1:
        response = Converse(sys.argv[1])
    else:
        response = Converse('What activities are planned for last friday')
    print response['responseText']
    # print str(response['action'])
    # print response['action']
    # print weather.RequestWeatherDescription()
