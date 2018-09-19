import dialogflow
from google.protobuf.json_format import MessageToJson
import json
from pkg.utilities import utility


language_code = 'en-US'

class Session():
    def __init__(self,credentials,project_id):
        session_id = 'my-Session'
        self.session_client = dialogflow.SessionsClient(credentials=credentials)
        #maybe session is only one needs to persist
        self.session = self.session_client.session_path(project_id, session_id)

    def MakeFormattedRequest(self, queryText):
        raw_response = self.MakeRequest(queryText)
        strResult = MessageToJson(raw_response.query_result)
        jsonResult = json.loads(strResult)
        r = utility.parseType(jsonResult)
        response = {
            'queryText': r['queryText'],
            'responseText': r['fulfillmentMessages'][0]['text']['text'][0],
            'action': r['action'],
            'parameters': r['parameters']
        }
        return response

    def MakeRequest(self, queryText):
        text_input = dialogflow.types.TextInput(text=queryText, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = self.session_client.detect_intent(session=self.session, query_input=query_input)
        # print response.query_result.intent.display_name
        # print response
        # return response.query_result.fulfillment_text
        return response