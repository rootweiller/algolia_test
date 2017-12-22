import os


class BaseConfig:

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Debug True
    DEBUG = False

    # Algolia KEY
    APP_ID = "7UHV2993DH"
    API_KEY = "40645e7932ca76222885dcd8f1cf0f53"
    INDEX_NAME = "SDN"

    # CSV URL DOWNLOAD
    XML_URL = "https://www.treasury.gov/ofac/downloads/add.csv"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False