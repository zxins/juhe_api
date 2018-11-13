# -*- coding: utf-8 -*-

from flask import Flask

api_app = Flask('news_api')
api_app.secret_key = 'KLADEHBMGKASAV7NYROACX'

API_HOST = '0.0.0.0'
API_PORT = 9400
