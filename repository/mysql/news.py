# -*- coding:utf-8 -*-
import json
import when
from entity.news import News
from toolkit.args import accepts
from repository.mysql import get_session, NewsModel


class NewsRepository(object):

    def __init__(self, session=None):
        self.session = session or get_session()

        # 决定是否自己销毁session, 而不是依赖上层回收
        if session is None:
            self.is_local_session = True
        else:
            self.is_local_session = False

    def __del__(self):
        """ 析构函数里面注销掉自己new出来的session """
        try:
            if self.is_local_session:
                self.session.close()
        except:
            pass

    def __commit__(self):
        """ 如果是自己new出来的session, 自己可以commit, 否则自己不要commit """
        try:
            if self.is_local_session:
                self.session.commit()
        except:
            pass

    def __create__(self, model):
        """ 为了统一, 写一个这个wrapper函数 """
        self.session.add(model)

    def entity_to_model(self, news):
        model = NewsModel()
        model.no = news.no
        model.title = news.title
        model.author_name = news.author_name
        model.url = news.url
        model.date = news.date
        model.pictures = json.dumps(news.pictures)
        model.category = news.category
        model.created = when.now()
        model.modified = when.now()
        return model

    def model_to_entity(self, model):

        params = {
            'no': model.no,
            'title': model.title,
            'author_name': model.author_name,
            'url': model.url,
            'date': model.date,
            'pictures': model.pictures,
            'category': model.category,
        }

        return News(**params)

    def find_by_category(self, category):
        models = self.session.query(NewsModel).filter(NewsModel.category == category).all()

        news = []
        for model in models:
            new = self.model_to_entity(model)
            news.append(new)
        return news

    @accepts(object, News)
    def save(self, news):
        """ 保存 """
        model = self.entity_to_model(news)
        self.__create__(model)
        self.__commit__()

    def batch_save(self, news):
        """ 批量保存 """

        models = []
        for entity in news:
            model = self.entity_to_model(entity)
            models.append(model)

        self.session.bulk_save_objects(models)
        self.__commit__()
