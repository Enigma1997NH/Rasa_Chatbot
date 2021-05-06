# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

#from database_connectivity import DataUpdate
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         print("My Self Rasa ChatBot")
         dispatcher.utter_message(text="Hello World!..from first actionhelloworld")

         return []


class ActionName(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "action_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(responses="utter_name")
        return [SlotSet('fname', tracker.latest_message['text'])]


class ActionMobile(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "action_mobile"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_mobile")
        return [SlotSet('mobile', tracker.latest_message['text'])]

class ActionEmail(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "action_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_email")
        return [SlotSet('email', tracker.latest_message['text'])]


class ActionSubmit(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "action_submit"



