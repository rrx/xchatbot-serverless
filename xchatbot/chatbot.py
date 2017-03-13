import os
import sys
import telegram
from chatterbot import ChatBot
from telegram import Bot, Update
import simplejson as json
import logging
log = logging.getLogger(__name__)


def train_chatbot(chatbot):
    # Train based on the english corpus
    chatbot.train("chatterbot.corpus.english")

    # Train based on english greetings corpus
    chatbot.train("chatterbot.corpus.english.greetings")

    # Train based on the english conversations corpus
    chatbot.train("chatterbot.corpus.english.conversations")

def get_chatbot(database=None):
    chatbot = ChatBot(
        'Ron Obvious',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
        storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
        database=None
    )
    train_chatbot(chatbot)
    return chatbot


def get_bot(token):
    bot = telegram.Bot(token=token)
    return bot


def handle_incoming_response(chatbot, text):
    return chatbot.get_response(text).text


if __name__ == '__main__':
    def run(token):
        chatbot = get_chatbot()
        # Create bot, update queue and dispatcher instances
        bot = Bot(token)
        event = {
          "message": {
            "date": 1441645532,
            "text": "doing good",
            "from": {
              "username": "Test",
              "first_name": "Test",
              "last_name": "Test Lastname",
              "id": 1111111
            },
            "message_id": 1365,
            "chat": {
              "type": 'test',
              "username": "Test",
              "first_name": "Test",
              "last_name": "Test Lastname",
              "id": 1111111
            }
          },
          "update_id": 10000
        }
        log.info(webhook_lambda_handler(event, {}))

    import sys
    import os
    cmd = sys.argv[1]
    if cmd == 'test':
        chatbot = get_chatbot()
        log.info(chatbot.get_response("Hello"))
    else:
        run(os.environ.get("TELEGRAM_API_KEY",""))
