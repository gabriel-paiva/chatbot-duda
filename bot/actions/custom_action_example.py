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
class ActionEnviarLocalizacaoBlocoE(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_e"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco E")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude = -15.866730550500023
            longitude = -48.03057020039818
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoF(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_f"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco F")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude = -15.866918891682571
            longitude = -48.03113078209065
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoG(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_g"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco G")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude = -15.867045112251532
            longitude = -48.02809843045367
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoL(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_l"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco L")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude = -15.868033550396934
            longitude = -48.02955231442692
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoS(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_s"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco S")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude =  -15.868791220436874
            longitude = -48.02926837863404
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoM(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_m"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco M")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude =  -15.865674398700659
            longitude = -48.029780635744665
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoN(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_n"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco N")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude =  -15.863852272963632
            longitude = -48.029248943207456
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoK(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_k"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco K")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            latitude =  -15.864691062768392
            longitude = -48.0295616180415
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")

