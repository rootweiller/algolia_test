from algoliasearch import algoliasearch
from instance.config import API_KEY, APP_ID, INDEX_NAME


def client_connect():

    client = algoliasearch.Client(APP_ID, API_KEY)
    index = client.init_index(INDEX_NAME)
    return index
