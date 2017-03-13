import pytest

from xchatbot.chatbot import handle_incoming_response, get_chatbot

def test():
    chatbot = get_chatbot()
    r = handle_incoming_response(chatbot, "Blue")
    assert(r == "Special cases aren't special enough to break the rules.")
