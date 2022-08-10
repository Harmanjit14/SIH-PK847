import numpy as np
from inltk.inltk import tokenize
from setup import language
from queries import *
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

USERNAME = None
LOGGEDIN = False
TOKEN = None


def token(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return tokenize(sentence, language)


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [word for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag


async def case_selector(id, client):

    # Server Connection
    transport = AIOHTTPTransport(url="http://localhost:8000/graphql")
    server_client = Client(transport=transport,
                           fetch_schema_from_transport=True)

    if id == -1:
        uname = input("Enter Username")
        upass = input("Enter Password")
        await login(uname, upass, client)


# print(token('ਸਤ ਸ੍ਰੀ ਅਕਾਲ,  ਮੈਂ ਹੇਜ਼ਲ ਹਾਂ |'))
