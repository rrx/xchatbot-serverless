"""
This is an entry handler for AWS Lambda

The lambda function must have HOME environment variable set to /tmp, since
/tmp is the only directory that has write access.  NLTK needs to download
some files to make this work.
"""
from __future__ import print_function
import os
import sys
__here__ = os.path.dirname(os.path.realpath(__file__))


def setup_vendored_libraries():
    """
    We tell python to get all of it's libraries from here
    The vendored directory get's zipped up as part of the serverless deploy
    """
    # import vendored application
    sys.path.append(os.path.join(__here__, "vendored"))

    cwd = os.getcwd()
    print("CWD: %s" % cwd)

    # change to /tmp
    os.chdir(os.environ.get("HOME", '/tmp'))

    cwd = os.getcwd()
    print("CWD: %s" % cwd)

# call this before importing
setup_vendored_libraries()

from xchatbot.chatbot import get_bot, get_chatbot, handle_incoming_response
from telegram import Update
import simplejson as json
import copy
import traceback
import logging
log = logging.getLogger(__name__)

from lambda_utils import setup_nltk_on_lambda
setup_nltk_on_lambda()


def webhook_lambda_handler(event, context):
    logger.setLevel(logging.INFO)
    try:
        handler(event, context, respond=True)
    except:
        logging.exception("handler")

    # return to API gateways
    return {
        "statusCode": 200,
        "body": "ok"
    }


def handler(_event, context, respond=True, database='/tmp/database.db'):
    # don't modify the event object, we do a deep copy
    event = copy.deepcopy(_event)
    log.debug("Event %s", event)

    bot = get_bot()
    chatbot = get_chatbot(database=database)
    # if the event is malformed, then just return ok

    if not event:
        return 'ok'

    if 'message' in event:
        update = Update.de_json(event, bot)
    elif 'body' in event:
        body = json.loads(event.get('body', ''))
        update = Update.de_json(body, bot)
    else:
        return 'ok'

    chat_id = update.message.chat.id
    response = handle_incoming_response(chatbot, update.message.text)

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = response.encode('utf-8')
    log.info("Got /%s/, sending /%s/", update.message.text, text)
    # repeat the same message back (echo)
    if respond:
        bot.sendMessage(chat_id=chat_id, text=text)
    return 'ok'


if __name__ == '__main__':
    # send a test event just for testing
    #os.chdir(__here__)
    from tests.test_chatbot import EVENT
    handler(EVENT, {}, respond=False)
    handler({'body': json.dumps(EVENT)}, {}, respond=False)
