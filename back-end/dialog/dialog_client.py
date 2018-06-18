import dialogflow
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('dialog/Improvise_Communicate-key.json')
language_code = 'en-US'
project_id = 'improvise-communicate'
session_id = 'my-Session'
session_client = dialogflow.SessionsClient(credentials=credentials)
session = session_client.session_path(project_id, session_id)


def MakeRequest(queryText):
    text_input = dialogflow.types.TextInput(text=queryText, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    # print response.query_result.intent.display_name
    # print response
    return response.query_result.fulfillment_text


if __name__ == '__main__':
    response = MakeRequest('how are you')
    print 'response received', response
