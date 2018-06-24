# from __future__ import absolute_import
import dialogflow
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToJson
import json
import sys
from pkg.utilservices import utility
import datetime

credentials = service_account.Credentials.from_service_account_file('pkg/keys/Improvise_Communicate-key.json')
language_code = 'en-US'
project_id = 'improvise-communicate'
session_id = 'my-Session'
session_client = dialogflow.SessionsClient(credentials=credentials)
session = session_client.session_path(project_id, session_id)


def MakeFormattedRequest(queryText):
    raw_response = MakeRequest(queryText)
    strResult = MessageToJson(raw_response.query_result)
    jsonResult = json.loads(strResult)
    r = utility.parseType(jsonResult)
    response = {
        'queryText': r['queryText'],
        'responseText': r['fulfillmentMessages'][0]['text']['text'][0],
        'action': r['action'],
        'parameters': r['parameters']
    }
    if 'date' in response['parameters']:
        if response['parameters']['date'] == '':
            return response
        # THIS SHOULD ALL BE PUT INTO UTILITIES!!!!
        # print 'BANG', response['parameters']
        resDateTime = response['parameters']['date']
        resDate = resDateTime.split('T')[0].split('-')
        resDate = utility.parseType(resDate)
        response['parameters']['formattedDate'] = datetime.date(resDate[0], resDate[1], resDate[2])
    return response


def MakeRequest(queryText):
    text_input = dialogflow.types.TextInput(text=queryText, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    # print response.query_result.intent.display_name
    # print response
    # return response.query_result.fulfillment_text
    return response


if __name__ == '__main__':
    if len(sys.argv) > 1:
        query = sys.argv[1]
        parsedResponse = MakeFormattedRequest(query)
        print parsedResponse
        # print 'response received', response

    # try:
    #     while True:
    #         query = raw_input("Enter some text: ")
    #         # response = MakeFormattedRequest(query)
    #         # print 'RAW', raw_response
    #         response = MakeRequest(query)

    #         # print 'PARSED', response
    #         # print 'response received', response.query_result
    # except KeyboardInterrupt:
    #     pass
