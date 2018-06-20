# from dialogflow_client import MakeRequest
from modules import weather
from modules import dialogflowClient


def Converse(queryText):
    response = dialogflowClient.MakeFormattedRequest(queryText)
    if response['action'] == 'weather.get':
        response['responseText'] = weather.RequestWeatherDescription()
    return response


if __name__ == '__main__':
    response = Converse('How are you')
    print response['responseText']
    # print str(response['action'])
    # print response['action']
    # print weather.RequestWeatherDescription()
