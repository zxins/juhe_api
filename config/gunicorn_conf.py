# -*- coding: utf-8 -*-
from config.flask_conf import API_HOST, API_PORT

bind = "0.0.0.0:{0}".format(API_PORT)
workers = 1
worker_class = "gevent"
