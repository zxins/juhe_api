# -*- coding:utf-8 -*-
import shortuuid
from schemer import Schema, Array


class News(object):
    """ 新闻实体类 """

    def __init__(self, **kwargs):

        # 先对参数做校验,校验不通过不生成News对象
        params_schema = Schema({
            'no': {'type': basestring, 'required': False, 'default': shortuuid.uuid().upper()},
            'title': {'type': basestring, 'required': True},
            'author_name': {'type': basestring, 'required': True},
            'url': {'type': basestring, 'required': True},
            'date': {'type': basestring, 'required': False},
            'pictures': {'type': dict, 'required': False},
            'category': {'type': basestring, 'required': False, 'default': 'default'},  # 这里要限制类型吗？
        })

        params_schema.validate(kwargs)
        params_schema.apply_defaults(kwargs)

        self.no = kwargs.get('no')
        self.title = kwargs.get('title')
        self.author_name = kwargs.get('author_name')
        self.url = kwargs.get('url')
        self.date = kwargs.get('date')
        self.pictures = kwargs.get('pictures')
        self.category = kwargs.get('category')

    @property
    def is_default(self):
        return self.category.lower() == 'default'

    @property
    def is_top(self):
        return self.category.lower() == 'top'
