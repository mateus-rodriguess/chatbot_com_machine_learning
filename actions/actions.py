# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from analysistext.analysis import message_user


class ActionSentiment(Action):
    """
    main action 
    """
    def name(self):
        return 'action_sentiment'

    def run(self, dispatcher, Tracker, domain):


        message = Tracker.latest_message['text']
        result_text = message_user(message)
        dispatcher.utter_message(text=result_text)
        return []
