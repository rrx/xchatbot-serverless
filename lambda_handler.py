"""
This is an entry handler for AWS Lambda

The lambda function must have HOME environment variable set to /tmp, since
/tmp is the only directory that has write access.  NLTK needs to download
some files to make this work.
"""
from __future__ import print_function
import os
import sys


def setup_vendored_libraries():
    """
    We tell python to get all of it's libraries from here
    The vendored directory get's zipped up as part of the serverless deploy
    """
    # import vendored application
    here = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(here, "vendored"))

    cwd = os.getcwd()
    print("CWD: %s" % cwd)

    # change to /tmp
    os.chdir(os.environ.get("HOME", '/tmp'))

    cwd = os.getcwd()
    print("CWD: %s" % cwd)


setup_vendored_libraries()


from xchatbot.chatbot import get_bot, get_chatbot, handle_incoming_response
from telegram import Update


def webhook_lambda_handler(event, context):
    print("Message %s" % event)

    bot = get_bot()
    here = os.path.dirname(os.path.realpath(__file__))
    chatbot = get_chatbot()
    # if the event is malformed, then just return ok
    if event.get('message') is None:
        return 'ok'


    update = Update.de_json(event, bot)
    chat_id = update.message.chat.id
    response = handle_incoming_response(chatbot, update.message.text)

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = response.encode('utf-8')
    print("Got /%s/, sending /%s/" % (update.message.text, text))
    # repeat the same message back (echo)
    bot.sendMessage(chat_id=chat_id, text=text)
    return 'ok'


if __name__ == '__main__':
    # send a test event just for testing
    # it will return an error from telegram because the chat_id doesn't exist
    event = {
        "update_id":10000,
        "message":{
        "date":1441645532,
        "chat":{
           "type": "test",
           "last_name":"Test Lastname",
           "id":1111111,
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
    webhook_lambda_handler(event, {})
