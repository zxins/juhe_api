# -*- coding:utf-8 -*-

from flask import jsonify


class RestResponse(object):

    def __init__(self):
        pass

    def fail(self, message="Request fail", code=500):
        d = {'meta': {
            'success': False,
            'status_code': code,
            'message': message
        }}
        json_response = jsonify(d, )
        return json_response

    def success(self, data=None, code=200):
        d = {'meta': {
            'success': True,
            'status_code': code,
            'message': "Requset Success"
        }, 'data': data}
        json_response = jsonify(d)
        return json_response
