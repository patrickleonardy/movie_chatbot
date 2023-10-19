# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import omdb
from dotenv import load_dotenv, find_dotenv
import os
import json
_ = load_dotenv(find_dotenv())


omdb.set_default('apikey', os.environ["OMDB_API_KEY"])


class ActionSearchMovieOmdb(Action):
    def name(self) -> Text:
        return "action_search_movie_omdb"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        current_movie = next(tracker.get_latest_entity_values("movie"), None)

        omdb_api_response = omdb.request(t=current_movie)
        omdb_api_response_json_content = json.loads(omdb_api_response.content)
        dispatcher.utter_message(json_message=omdb_api_response_json_content)
        return []
