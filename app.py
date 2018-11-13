# -*- coding: utf-8 -*-

from views.index import *
from config.flask_conf import api_app, API_HOST, API_PORT

if __name__ == '__main__':
    api_app.run(host=API_HOST, port=int(API_PORT))
