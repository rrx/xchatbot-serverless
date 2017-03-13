import pytest
import simplejson as json
from xchatbot.chatbot import handle_incoming_response, get_chatbot
from lambda_handler import handler

def test():
    chatbot = get_chatbot()
    r = handle_incoming_response(chatbot, "Blue")
    assert(r == "Special cases aren't special enough to break the rules.")

# this is a test token that's used in the telegram-bot unittests.
TOKEN="133505823:AAHZFMHno3mzVLErU5b5jJvaeG--qUyLyG0"

EVENT = {
    "update_id":10000,
    "message":{
    "date":1441645532,
    "chat":{
       "type": "test",
       "last_name":"Test Lastname",
       "id":12173560,
       "first_name":"Test",
       "username":"Test"
    },
    "message_id":1365,
    "from":{
       "last_name":"Test Lastname",
       "id":1111111,
       "first_name":"Test",
       "username":"Test"
    },
    "text":"/start"
    }
}


def test_lambda_event():
    assert 'ok' == handler(EVENT, {}, token=TOKEN, respond=False)


def test_proxy():
    assert 'ok' == handler({'body': json.dumps(EVENT)}, {}, token=TOKEN, respond=False)
