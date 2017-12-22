from algoliasearch import algoliasearch
from instance.config import DevelopmentConfig


def client_connect():

    client = algoliasearch.Client(DevelopmentConfig.APP_ID,
                                  DevelopmentConfig.API_KEY)
    index = client.init_index(DevelopmentConfig.INDEX_NAME)
    return index
