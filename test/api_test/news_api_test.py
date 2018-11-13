# -*- coding:utf-8 -*-

import requests
from config.flask_conf import API_HOST, API_PORT


def category():
    import json

    url = 'http://{host}:{port}/news/category'.format(host=API_HOST, port=API_PORT)

    params = {
        # 'category': 'top',
    }

    r = requests.get(url, params=params)
    content = json.loads(r.content)
    data = content.get('data')

    for row in data:
        print row


if __name__ == '__main__':
    category()