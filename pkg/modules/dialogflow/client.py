# import dialogflow
from google.oauth2 import service_account
from pkg.modules.dialogflow.session import Session
from pkg.modules.dialogflow.intent import Intent

credentials = service_account.Credentials.from_service_account_file('pkg/keys/improvise-communicate-admin.json')
# credentials = service_account.Credentials.from_service_account_file('pkg/keys/Improvise_Communicate-admin-key.json')
# en-au is untested

project_id = 'improvise-communicate'


class DialogflowClient():
    def __init__(self):
        self.Session = Session(credentials, project_id)
        self.Intent = Intent(credentials, project_id)
        pass


if __name__ == "__main__":
    client = DialogflowClient()
    trainingPhrases = ['hey there', 'whats goin on', 'greetings', 'hello', 'hi']
    responseText = 'hello!'
    displayName = 'Test Greetings'
    intent = client.Intent.CreateIntent("Test Greetings", trainingPhrases, [responseText])
    # print intent
