# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import telegram


class ActionExemplo(Action):
    def name(self) -> Text:
        return "action_exemplo"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Esta mensagem esta sendo enviada do RASA SDK!!!")

        return []

class ActionEnviarDocEstatuto(Action):
    def name(self):
        return "action_enviar_doc_estatuto"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento do Estatuto da UCB")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2019/12/ESTATUTO-UCB-2019-1.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")

class ActionEnviarLocalizacaoBlocoABCD(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_abcd"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização dos blocos A, B, C e D")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude = -15.867332217513887
            longitude = -48.03043820754369
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
