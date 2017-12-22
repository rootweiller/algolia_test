#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests
import xmltodict as xmltodict
from flask import Flask, g

from client import client_connect
from instance.config import DEBUG, XML_URL

app = Flask(__name__)


@app.route('/')
def welcome_page():
    message = 'Welcome to Clinton List'
    return message


@app.route('/API/V1/q/<search_code>/')
def search_in_api(search_code):

    g.search_code = search_code
    connect = client_connect()

    search = connect.search(search_code)
    result = json.dumps(search)

    return result


@app.route('/API/V1/a/add_list/')
def update_list():

    with requests.Session() as s:
        download = s.get(XML_URL)

        output = xmltodict.parse(download)

        o_output = json.dumps(output)

        print(o_output)

        return 'Done'


@app.route('/API/V1/l/list_indexes')
def list_index():

    connect = client_connect()

    list_index = connect.client.list_indexes()

    return str(list_index['items'][0]['name'])


if __name__ == '__main__':
    app.run(debug=DEBUG)