# from dialogflow_client import MakeRequest
from modules import weather
from modules import activities
from modules import dialogflowClient


def Converse(queryText):
    response = dialogflowClient.MakeFormattedRequest(queryText)
    if response['action'] == 'weather.get':
        response['responseText'] = weather.RequestWeatherDescription()
    elif response['action'] == 'activities.get':
        response['responseText'] = activities.RequestScheduleFromParameters(response['parameters'])
    return response


if __name__ == '__main__':
    response = Converse('What activities are planned for last friday')
    print response['responseText']
    # print str(response['action'])
    # print response['action']
    # print weather.RequestWeatherDescription()
