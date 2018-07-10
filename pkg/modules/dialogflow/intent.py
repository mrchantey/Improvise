import dialogflow
# REQUIRES GOOGLE AUTHENTICATION


class Intent:
    def __init__(self, credentials, project_id):
        self.project_id = project_id
        self.intents_client = dialogflow.IntentsClient(credentials=credentials)
        self.parent = self.intents_client.project_agent_path(self.project_id)
        self.intents = self.ListIntents()

    # message_text appears to be a response
    def CreateIntent(self, display_name, training_phrases, responses, overwrite=True):
        if overwrite == True:
            self.DeleteIfExists(display_name)

        def CreateDFTrainingPhrase(training_phrase):
            part = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrase)
            return dialogflow.types.Intent.TrainingPhrase(parts=[part])
        df_training_phrases = map(lambda p: CreateDFTrainingPhrase(p), training_phrases)

        df_response_message_text = dialogflow.types.Intent.Message.Text(text=responses)
        df_response_message = dialogflow.types.Intent.Message(text=df_response_message_text)
        intent = dialogflow.types.Intent(
            display_name=display_name,
            training_phrases=df_training_phrases,
            messages=[df_response_message]
        )

        try:
            created_intent = self.intents_client.create_intent(self.parent, intent)
            print 'intent created:\t{0}'.format(created_intent.display_name)
            return created_intent
        except:
            return 'error occured, maybe intent exists and overwrite set to false'

    def ListIntents(self):
        # parentPath = 'projects/{0}/agent'.format(self.project_id)
        intentIterator = self.intents_client.list_intents(self.parent)
        intents = []
        for intent in intentIterator:
            intents.append(intent)
        return intents

    def DeleteIfExists(self, display_name):
        intent = self.GetByDisplayName(display_name)
        if intent != None:
            self.DeleteIntent(intent)
            print 'intent deleted:\t{0}'.format(intent.display_name)
            return True
        return False

    def GetByDisplayName(self, display_name):
        for intent in self.intents:
            if intent.display_name == display_name:
                return intent
        return None

    # def GetId(self, intent):
    #     splitName = intent.name.split('/')
    #     id = splitName[len(splitName)-1]
    #     return id

    def DeleteIntent(self, intent):
        # req = self.intents_client.get_intent(intent_name)
        # print req
        # intent_path = self.intents_client.intent_path(self.project_id, intent_id)
        # print intent_path
        self.intents_client.delete_intent(intent.name)
