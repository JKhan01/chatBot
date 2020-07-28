# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

slotList = ["repo_name","project_name","branch_name","user_name","bitbucket_key","duration_keys","bitbucket_action","error_action"]

class BitbucketForm(FormAction):

    def name(self) -> Text:
        return "bitbucket_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        if ("watchers" in tracker.get_slot("bitbucket_action") or "list of watchers" in tracker.get_slot("bitbucket_action")):   
            return ["bitbucket_action","repo_name"]
        elif ("who" or "who all" in tracker.get_slot("search_keys")):
            return ["bitbucket_action","repo_name","duration_keys"]
        else:
            return ["bitbucket_action","repo_name","user_name","branch_name","duration_keys"]



    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class ErrorForm(FormAction):

    def __init__(self):
        self.error_query = ""
    def name(self) -> Text:
        return "error_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["error_action"]
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        self.error_query = tracker.get_slot("error_action")
        print (f"slot value: {self.error_query}")
        return []