# -*- coding: utf-8 -*-

from api.news import *
from config.flask_conf import api_app, API_HOST, API_PORT

if __name__ == '__main__':
    api_app.run(host=API_HOST, port=int(API_PORT))
