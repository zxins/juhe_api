# -*- coding:utf-8 -*-
from schemer import Schema
from flask import request
from api import RestResponse
from vo.v1 import vo_format_news
from config.flask_conf import api_app


@api_app.route('/news/category', methods=['GET'])
def news_category(**kwargs):
    """
    top(头条，默认),
    shehui(社会),
    guonei(国内),
    guoji(国际),
    yule(娱乐),
    tiyu(体育),
    junshi(军事),
    keji(科技),
    caijing(财经),
    shishang(时尚)
    """

    from application.news_app import NewsApp

    category = request.values.get('category') or 'top'
    news_app = NewsApp()
    news_list = news_app.retrieve_by_category(category)

    data = []
    for news in news_list:
        data.append(vo_format_news(news))

    response = RestResponse()
    return response.success(data=data)
