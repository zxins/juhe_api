# -*- coding: utf-8 -*-

from config.flask_conf import api_app


@api_app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello World!'
