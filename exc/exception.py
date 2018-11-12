# -*- coding:utf-8 -*-


class BizError(Exception):
    """ 业务错误,需要将错误内容暴露出来 """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
