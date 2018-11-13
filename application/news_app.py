# -*- coding: utf-8 -*-
from repository.mysql.news import NewsRepository


class NewsApp(object):

    def __init__(self):
        pass

    def retrieve_by_category(self, category):
        nr = NewsRepository()
        news_list = nr.find_by_category(category)
        return news_list
