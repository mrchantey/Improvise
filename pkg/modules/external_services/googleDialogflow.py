

API_KEY = open("pkg/keys/improvise-communicate-api-key.txt").read()
PROJECT_ID = "improvise-communicate"
SESSION_ID = 0
GOOGLE_SPEECH_URL = "https://dialogflow.googleapis.com/v2/projects/*/agent/sessions/*}:detectIntent?key={0}".format(API_KEY)
